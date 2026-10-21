"""Open Graph images (1200x630) for every page.

    python3 _build/og.py          # needs a local server on :8765 and Playwright (node)

Writes one HTML card per page to _build/og_tmp/, screenshots them with _build/og.js
and saves /assets/og/<slug>.jpg. Titles come from each page's H1.
"""
import os, re, json, html, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import ROOT, og_slug

# path: (photo, tone, object-position, eyebrow, sub override)
PAGES = {
    '/': ('nikol-hero-1280', 'paper', '50% 28%', 'Vizážistka · Praha', None),
    '/svatebni-liceni/': ('wedding-5-800', 'paper', '50% 30%', 'Svatby · Praha a Evropa', None),
    '/vecerni-liceni/': ('evening-5-800', 'ox', '50% 25%', 'Plesy · galavečery · večírky', None),
    '/nude-liceni/': ('nude-1-800', 'blush', '50% 30%', 'Přirozený look', None),
    '/komercni-liceni/': ('commercial-4-800', 'ink', '50% 30%', 'Focení · kampaně · editorial', None),
    '/kurzy-liceni/': ('course-1000', 'sand', '50% 15%', 'Individuální lekce', None),
    '/portfolio/': ('collage', 'paper', '', 'Svatební · večerní · nude · komerční', None),
    '/en/': ('nikol-hero-1280', 'paper', '50% 28%', 'Makeup artist · Prague', None),
    '/en/wedding/': ('wedding-5-800', 'paper', '50% 30%', 'Weddings · Prague & Europe', None),
    '/en/evening-makeup/': ('evening-5-800', 'ox', '50% 25%', 'Balls · galas · parties', None),
    '/en/nude-makeup/': ('nude-1-800', 'blush', '50% 30%', 'Natural look', None),
    '/en/commercial-makeup/': ('commercial-4-800', 'ink', '50% 30%', 'Shoots · campaigns · editorial', None),
    '/en/courses/': ('course-1000', 'sand', '50% 15%', 'One-on-one lessons', None),
    '/en/portfolio/': ('collage', 'paper', '', 'Bridal · evening · nude · commercial', None),
    '/blog/': ('nude-3-800', 'blush', '50% 30%', 'Tutoriály · recenze · tipy', None),
    '/blog/letni-make-up-bez-make-upu/': ('nude-1-800', 'paper', '50% 30%', 'Tutoriál · léto', 'SPF, blur, krémové barvy a test fixačních sprejů'),
    '/en/blog/': ('nude-3-800', 'blush', '50% 30%', 'Tutorials · reviews · tips', None),
    '/en/blog/summer-no-makeup-makeup/': ('nude-1-800', 'paper', '50% 30%', 'Tutorial · summer', 'SPF, blur, cream colour and setting sprays tested'),
    '/blog/recenze-nyx-cely-oblicej/': ('nikol-hero-1280', 'ink', '50% 28%', 'Recenze · celodenní test', 'Báze, korektor, obočí, bronzer, oči a celodenní test'),
    '/en/blog/full-face-of-nyx-review/': ('nikol-hero-1280', 'ink', '50% 28%', 'Review · 9 min read', 'Primer to setting spray, tested all day'),
}

TONES = {  # background, text, accent, sub
    'paper': ('#FBF7F5', '#171213', '#A8232F', '#4E4442'),
    'blush': ('#F5E4DF', '#171213', '#A8232F', '#4E4442'),
    'sand': ('#EDE6E1', '#171213', '#A8232F', '#4E4442'),
    'ox': ('#3E1016', '#FBF7F5', '#F4B9AE', '#E9DCD8'),
    'ink': ('#171213', '#FBF7F5', '#F4B9AE', '#E9DCD8'),
}

CSS = '''
@font-face{font-family:Archivo;font-weight:400 700;font-stretch:100% 125%;src:url(/assets/fonts/archivo-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+2013-2014,U+2018-201E,U+2022,U+2026}
@font-face{font-family:Archivo;font-weight:400 700;font-stretch:100% 125%;src:url(/assets/fonts/archivo-latin-ext.woff2) format("woff2");unicode-range:U+0100-017F}
@font-face{font-family:Lora;font-weight:400 600;src:url(/assets/fonts/lora-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+2013-2014,U+2018-201E,U+2022,U+2026}
@font-face{font-family:Lora;font-weight:400 600;src:url(/assets/fonts/lora-latin-ext.woff2) format("woff2");unicode-range:U+0100-017F}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden}
body{display:grid;grid-template-columns:1fr 470px;background:var(--bg);color:var(--fg);font-family:Archivo,sans-serif}
.l{display:flex;flex-direction:column;justify-content:space-between;padding:56px 56px 52px 64px;min-width:0}
.top{display:flex;justify-content:space-between;align-items:center;font:600 20px/1 Archivo;font-stretch:125%;text-transform:uppercase;letter-spacing:.01em}
.eb{font:600 15px/1.2 Archivo;font-stretch:112%;letter-spacing:.14em;text-transform:uppercase;color:var(--ac);margin-bottom:22px}
h1{font:500 96px/.94 Archivo;font-stretch:125%;text-transform:uppercase;letter-spacing:-.03em}
.sub{font:400 32px/1.2 Lora;color:var(--sub);margin-top:24px;max-width:600px}
.bot{display:flex;justify-content:space-between;align-items:center;font:600 15px/1 Archivo;font-stretch:112%;letter-spacing:.12em;text-transform:uppercase}
.pill{background:var(--ac);color:var(--bg);padding:14px 20px;border-radius:999px}
.dark .pill{color:#3E1016}
.r{position:relative;overflow:hidden}
.r img{width:100%;height:100%;object-fit:cover;display:block}
.col{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px;height:100%;background:var(--bg)}
.col img:first-child{grid-row:span 2}
'''


def page_text(path):
    f = os.path.join(ROOT, path.lstrip('/'), 'index.html')
    h = open(f, encoding='utf-8').read()
    lang = re.search(r'<html lang="(\w+)"', h).group(1)
    m = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
    inner = m.group(1)
    big = re.search(r'<span class="big[^"]*">(.*?)</span>', inner, re.S)
    sub = re.search(r'<span class="sub[^"]*">(.*?)</span>', inner, re.S)
    strip = lambda s: html.unescape(re.sub(r'<br\s*/?>', ' ', re.sub(r'<(?!br)[^>]+>', '', s))).strip()
    if big:
        return lang, strip(big.group(1)), strip(sub.group(1)).lstrip('–— ').strip() if sub else ''
    return lang, strip(inner), ''


def card(path):
    photo, tone, pos, eyebrow, sub_over = PAGES[path]
    lang, title, sub = page_text(path)
    if sub_over:
        sub = sub_over
    bg, fg, ac, sb = TONES[tone]
    dark = tone in ('ox', 'ink')
    if photo == 'collage':
        right = ('<div class="col"><img src="/assets/img/wedding-14-800.webp"><img src="/assets/img/evening-3-800.webp">'
                 '<img src="/assets/img/commercial-6-800.webp"></div>')
    else:
        right = f'<img src="/assets/img/{photo}.webp" style="object-position:{pos}">'
    cta = 'Rezervace online' if lang == 'cs' else 'Book online'
    loc = 'Praha · Česká republika' if lang == 'cs' else 'Prague · Czech Republic'
    e = html.escape
    maxh = 270 if sub else 330
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>:root{{--bg:{bg};--fg:{fg};--ac:{ac};--sub:{sb}}}{CSS}</style></head>
<body class="{'dark' if dark else ''}"><div class="l">
<div class="top"><span>Nikol Pavlova</span><span style="font-size:14px;letter-spacing:.14em;color:var(--sub)">{e(loc)}</span></div>
<div><p class="eb">{e(eyebrow)}</p><h1 id="t">{e(title)}</h1>{f'<p class="sub">{e(sub)}</p>' if sub else ''}</div>
<div class="bot"><span>nikolmakeup.cz</span><span class="pill">{e(cta)} +</span></div>
</div><div class="r">{right}</div>
<script>document.fonts.ready.then(function(){{var t=document.getElementById('t'),s=96;t.style.fontSize=s+'px';while((t.offsetHeight>{maxh}||t.scrollWidth>t.clientWidth+1)&&s>40){{s-=2;t.style.fontSize=s+'px'}}document.body.dataset.ready=1}})</script>
</body></html>'''


def main():
    tmp = os.path.join(ROOT, '_build', 'og_tmp')
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'assets', 'og'), exist_ok=True)
    jobs = []
    for path in PAGES:
        slug = og_slug(path)
        open(os.path.join(tmp, slug + '.html'), 'w', encoding='utf-8').write(card(path))
        jobs.append([f'http://localhost:8765/_build/og_tmp/{slug}.html', os.path.join(ROOT, 'assets', 'og', slug + '.png')])
    subprocess.run(['node', os.path.join(ROOT, '_build', 'og.js'), json.dumps(jobs)], check=True)
    from PIL import Image
    for _, png in jobs:
        Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=86, optimize=True, progressive=True)
        os.remove(png)
    print(len(jobs), 'OG images')


if __name__ == '__main__':
    main()
