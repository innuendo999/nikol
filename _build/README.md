# Site generator

Static pages are generated from Python templates (no dependencies beyond the standard library).

```
python3 _build/build.py      # rebuilds every page, sitemap.xml, robots.txt, llms.txt, 404.html
python3 _build/images.py     # (needs Pillow) regenerates responsive WebP images in /assets/img
```

- `lib.py` – shared layout (head, header, footer, sections), constants (Calendly, phone, e-mail, socials)
- `pages_cs.py` / `pages_en.py` – page content
- `reviews.py` – Google reviews shown on the pages
- `schema.py`, `schema/` – JSON-LD structured data

Edit content in the Python files, then rerun `build.py` and commit the generated HTML.
The `_build` folder is not published by GitHub Pages (folders starting with `_` are ignored).
