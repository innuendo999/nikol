// Paid guide download – Cloudflare Worker.
//
// GET /download?session_id=cs_...&lang=cs|en
//   1. Asks Stripe for the Checkout Session (with line items).
//   2. Checks that it is paid and not older than MAX_AGE_DAYS.
//   3. Maps the bought Price ID to a PDF in the private R2 bucket (FILES) and streams it.
// The PDFs live only in R2 – never in the public site repo.
//
// Bindings / settings (see wrangler.toml and README.md):
//   GUIDES             R2 bucket with the PDFs
//   STRIPE_SECRET_KEY  secret – a restricted key with read access to Checkout Sessions is enough
//   FILES              JSON: {"price_...": {"key": "brush-guide-cs.pdf", "name": "Pruvodce-stetci-Nikol-Pavlova.pdf"}, ...}
//   MAX_AGE_DAYS       how long a session stays valid as a download link (default 30)
//   SITE_URL           https://nikolmakeup.cz

const TEXT = {
  cs: {
    unpaid: 'Platba zatím není potvrzená. Zkuste to prosím za chvíli znovu.',
    expired: 'Platnost odkazu ke stažení vypršela.',
    invalid: 'Odkaz ke stažení není platný.',
    error: 'Stažení se nepodařilo.',
    help: (mail) => `Napište mi na <a href="mailto:${mail}">${mail}</a> e-mail, který jste zadali při platbě, a průvodce vám pošlu.`,
    back: 'Zpět na web',
  },
  en: {
    unpaid: 'The payment is not confirmed yet. Please try again in a moment.',
    expired: 'This download link has expired.',
    invalid: 'This download link is not valid.',
    error: 'The download failed.',
    help: (mail) => `Email me at <a href="mailto:${mail}">${mail}</a> from the address you used at checkout and I’ll send you the guide.`,
    back: 'Back to the site',
  },
};
const MAIL = 'pavlovanikol@gmail.com';

function page(env, lang, status, msg) {
  const t = TEXT[lang];
  const site = env.SITE_URL || 'https://nikolmakeup.cz';
  const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Nikol Pavlova</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#FBF7F5;font:17px/1.6 system-ui,sans-serif;color:#111}
main{max-width:520px;padding:32px}h1{font-size:28px;line-height:1.2;margin:0 0 12px}a{color:#8E2A3A}</style></head>
<body><main><h1>${msg}</h1><p>${t.help(MAIL)}</p><p><a href="${site}${lang === 'cs' ? '/' : '/en/'}">${t.back}</a></p></main></body></html>`;
  return new Response(html, { status, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' } });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const lang = url.searchParams.get('lang') === 'cs' ? 'cs' : 'en';
    const t = TEXT[lang];
    if (request.method !== 'GET' || url.pathname !== '/download') return page(env, lang, 404, t.invalid);

    const id = url.searchParams.get('session_id') || '';
    if (!/^cs_(test|live)_[A-Za-z0-9]+$/.test(id)) return page(env, lang, 400, t.invalid);

    let session;
    try {
      const r = await fetch(`https://api.stripe.com/v1/checkout/sessions/${id}?expand[]=line_items`, {
        headers: { authorization: `Bearer ${env.STRIPE_SECRET_KEY}` },
      });
      if (r.status === 404) return page(env, lang, 404, t.invalid);
      if (!r.ok) return page(env, lang, 502, t.error);
      session = await r.json();
    } catch (e) {
      return page(env, lang, 502, t.error);
    }

    if (session.status !== 'complete' || !['paid', 'no_payment_required'].includes(session.payment_status)) {
      return page(env, lang, 402, t.unpaid);
    }
    const maxAge = Number(env.MAX_AGE_DAYS || 30) * 86400;
    if (Date.now() / 1000 - session.created > maxAge) return page(env, lang, 410, t.expired);

    const files = JSON.parse(env.FILES || '{}');
    const item = (session.line_items?.data || []).find((li) => li.price && files[li.price.id]);
    if (!item) return page(env, lang, 404, t.invalid);
    const file = files[item.price.id];

    const obj = await env.GUIDES.get(file.key);
    if (!obj) return page(env, lang, 500, t.error);
    return new Response(obj.body, {
      headers: {
        'content-type': 'application/pdf',
        'content-disposition': `attachment; filename="${file.name || file.key}"`,
        'cache-control': 'private, no-store',
        'x-robots-tag': 'noindex',
      },
    });
  },
};
