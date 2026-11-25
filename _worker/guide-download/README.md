# Brush guide: payment and download

Pages: `/pruvodce-stetci/` (CZ), `/en/brush-guide/` (EN) and `/uk/gaid-penzlyky/` (UA), built by `_build/pages_guide.py`.
Thank-you pages: `/pruvodce-stetci/dekuji/`, `/en/brush-guide/thank-you/` and `/uk/gaid-penzlyky/dyakuyu/` (noindex).

```
Buy button ──► Stripe Payment Link ──► paid ──► thank-you page ?session_id=cs_…
                                                     │
                                                     ▼
                         guide.nikolmakeup.cz/download?session_id=…  (this Worker)
                         checks the session with Stripe ──► streams the PDF from private R2
```

The PDFs are never in this repository (it is public).

## Setup, once

1. **Stripe**
   - One product per guide with a one-time price: CZ in CZK, EN in EUR, UA in UAH. Note the **Price IDs** (`price_…`).
   - Create a **Payment Link** for each price. Under *After payment*, choose *Don't show confirmation page* and redirect to:
     - CZ: `https://nikolmakeup.cz/pruvodce-stetci/dekuji/?session_id={CHECKOUT_SESSION_ID}`
     - EN: `https://nikolmakeup.cz/en/brush-guide/thank-you/?session_id={CHECKOUT_SESSION_ID}`
     - UA: `https://nikolmakeup.cz/uk/gaid-penzlyky/dyakuyu/?session_id={CHECKOUT_SESSION_ID}`
   - Create a **restricted API key** with *Checkout Sessions: Read*. The Worker needs nothing else.
2. **Cloudflare R2**: create the bucket `nikol-guides` and upload `brush-guide-cs.pdf`, `brush-guide-en.pdf` and `brush-guide-uk.pdf`.
3. **Worker**, from this folder:
   ```
   npx wrangler secret put STRIPE_SECRET_KEY     # paste the restricted key
   npx wrangler deploy
   ```
   Before deploying, put the real Price IDs into `FILES` in `wrangler.toml`. To serve the Worker on `guide.nikolmakeup.cz`, uncomment `routes` (the domain must be on Cloudflare). Otherwise use the `*.workers.dev` URL.
4. **Site**: in `_build/pages_guide.py`, fill in `DOWNLOAD_API`, the `stripe_link` and `price`/`price_num` for each language. Then run `python3 _build/build.py`. The pages become indexable, get hreflang and enter the sitemap.

## Testing

Use Stripe test mode: a test Payment Link, a test restricted key and card `4242 4242 4242 4242`. After payment, the thank-you page's button should download the PDF. A made-up `session_id` should show the "not valid" page.

## Notes

- A download link is the Checkout Session ID: whoever has it can download for `MAX_AGE_DAYS` (30). This is the usual trade-off for instant delivery without accounts.
- EU buyers: for digital content delivered right away, the 14-day withdrawal right only lapses if the buyer agrees to immediate delivery and acknowledges losing that right. You can add that consent with Stripe's *Require customers to accept your terms of service* option, linking to your terms. Check the wording with an accountant or lawyer.
