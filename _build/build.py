"""Static site generator: python3 _build/build.py  (run from repo root or anywhere)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import pages_cs, pages_en

LASTMOD = '2026-10-19'

# (cs path, en path) pairs; None = single-language page
PAIRS = [
    ('/', '/en/', '1.0'),
    ('/svatebni-liceni/', '/en/wedding/', '0.9'),
    ('/vecerni-liceni/', '/en/evening-makeup/', '0.8'),
    ('/nude-liceni/', '/en/nude-makeup/', '0.8'),
    ('/komercni-liceni/', '/en/commercial-makeup/', '0.8'),
    ('/kurzy-liceni/', '/en/courses/', '0.8'),
    ('/portfolio/', '/en/portfolio/', '0.7'),
    (None, '/en/blog/', '0.6'),
    (None, '/en/blog/full-face-of-nyx-review/', '0.6'),
]


def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for cs, en, pr in PAIRS:
        alts = []
        if cs:
            alts = [('cs', cs), ('en', en), ('x-default', cs)]
        for p in [x for x in (cs, en) if x]:
            out.append('  <url>')
            out.append(f'    <loc>{SITE}{p}</loc>')
            out.append(f'    <lastmod>{LASTMOD}</lastmod>')
            out.append(f'    <priority>{pr}</priority>')
            for hl, ap in alts:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{SITE}{ap}"/>')
            out.append('  </url>')
    out.append('</urlset>\n')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(out))


def robots():
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /v2/\n\nSitemap: {SITE}/sitemap.xml\n')


def llms():
    s = SITE
    txt = f'''# Nikol Pavlova — Vizážistka Praha / Professional Makeup Artist in Prague

> Nikol Pavlova is a professional, English-speaking makeup artist (vizážistka) based in Prague 7, Czech Republic. She specialises in bridal and wedding makeup, evening and cocktail styling, natural "nude" looks, commercial and editorial makeup for photo shoots, makeup and hairstyling for special occasions, and personalised one-on-one makeup courses. Services are offered in Czech, English and Ukrainian, and she travels across the Czech Republic and Europe for destination weddings, shoots and events.

Key facts for accurate reference:

- **Business name:** Vizážistka Nikol Pavlova (Google Business Profile) — Nikol Pavlova, makeup artist Prague.
- **Location:** Prague 7, Czech Republic (works across all Prague districts and travels for destination work).
- **Languages:** Czech, English, Ukrainian.
- **Specialties:** Bridal/wedding makeup (bridal trial, lashes and touch-up kit included), evening and cocktail styling, prom/ball makeup, nude/natural looks, commercial and editorial makeup, private makeup courses.
- **Reviews:** Rated 5.0 on Google by clients for long-lasting makeup, a calm approach and fluent English.
- **Booking:** Online via Calendly ({CAL}), phone/SMS/WhatsApp at {TEL_H}, email {MAIL}, or Instagram DM. Personalised quotes within 24 hours.
- **Booking lead time:** Weddings 6–12 months ahead (peak season May–September); evening makeup and shoots usually 2–3 weeks.
- **Site languages:** Czech (default) at the root, English under /en/.

## Main pages

- [Domů (Czech home)]({s}/): Vizážistka Praha — overview of services, about, pricing, Google reviews and FAQ.
- [Home (English)]({s}/en/): English-speaking makeup artist in Prague — services, about, pricing, reviews and FAQ.
- [Portfolio (CZ)]({s}/portfolio/) · [Portfolio (EN)]({s}/en/portfolio/): Bridal, evening, nude, commercial and course work.

## Services

- [Svatební líčení]({s}/svatebni-liceni/) · [Wedding makeup]({s}/en/wedding/): Bridal trial, wedding-day application, lashes, touch-up kit; bride, bridesmaids and mother of the bride; destination weddings.
- [Večerní líčení]({s}/vecerni-liceni/) · [Evening makeup]({s}/en/evening-makeup/): Galas, balls, proms, cocktail parties — soft glam to smoky eyes.
- [Nude líčení]({s}/nude-liceni/) · [Nude makeup]({s}/en/nude-makeup/): Natural skin-first looks for engagement shoots, portraits and civil ceremonies.
- [Komerční líčení]({s}/komercni-liceni/) · [Commercial makeup]({s}/en/commercial-makeup/): Photo shoots, campaigns, lookbooks, editorials and video with on-set touch-ups.
- [Kurzy líčení]({s}/kurzy-liceni/) · [Makeup courses]({s}/en/courses/): One-on-one lessons — skin prep, colour theory, technique, product selection.

## Blog

- [Blog]({s}/en/blog/): Honest makeup reviews and pro tips.
- [Full Face of NYX: A Makeup Artist's Honest Review]({s}/en/blog/full-face-of-nyx-review/): Full-face test with an all-day wear test.

## Booking & contact

- [Book online (Calendly)]({CAL})
- Phone / SMS / WhatsApp: {TEL_H}
- Email: {MAIL}
- [Instagram @nikol__mua]({IG})
- [Facebook]({FB})
- [Threads @nikol_pavlova_mua]({TH})

## Optional

- [Sitemap]({s}/sitemap.xml)
'''
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(txt)


def not_found():
    h = head('cs', 'Stránka nenalezena (404) | Nikol Pavlova', 'Tato stránka neexistuje. Pokračujte na hlavní stránku, služby nebo portfolio.', '/404.html', [], SITE + '/img/nikol.jpg', [])
    h = h.replace('content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"', 'content="noindex, follow"')
    h = h.replace(f'<link rel="canonical" href="{SITE}/404.html">\n', '')
    h += header('cs', '', '/en/')
    h += f'''<section class="page-head" aria-labelledby="page-h1" style="min-height:60vh"><div class="wrap" style="display:flex;flex-direction:column;gap:28px">
<p class="lbl red">Chyba 404 · Error 404</p>
<h1 class="h1" id="page-h1"><span class="big wide" style="font-size:clamp(34px,9vw,150px)">Stránka nenalezena</span><span class="sub serif">— this page could not be found</span></h1>
<p class="body" style="max-width:640px">Odkaz je možná zastaralý nebo stránka byla přesunuta. Zkuste hlavní stránku, služby nebo portfolio. · The link may be outdated or the page has moved.</p>
<ul style="display:flex;flex-wrap:wrap;gap:10px;list-style:none;padding:0">
<li><a class="btn" href="/">Domů</a></li><li><a class="btn btn--outline" href="/svatebni-liceni/">Svatební líčení</a></li><li><a class="btn btn--outline" href="/portfolio/">Portfolio</a></li><li><a class="btn btn--outline" href="/en/">English</a></li><li><a class="btn btn--outline" href="{CAL}" rel="noopener">Rezervace online +</a></li>
</ul></div></section>
'''
    h += footer('cs', 'Kontaktujte mě', 'Potřebujete pomoc s líčením?', 'Napište mi a do 24 hodin vám pošlu nabídku.')
    # absolute asset paths already; 404 is served from any depth
    open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8').write(h)


if __name__ == '__main__':
    pages_cs.build()
    pages_en.build()
    sitemap(); robots(); llms(); not_found()
    print('built')
