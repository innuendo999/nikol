"""Open Graph images (1200x630) for every page.

    python3 _build/og.py [blog]   # needs a local server on :8765 and Playwright (node); 'blog' = blog cards only

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
    '/vecerni-liceni/': ('evening-5-800', 'ox', '50% 25%', 'Glam · smoky eyes · výrazné rty', None),
    '/plesove-liceni/': ('evening-14-800', 'ox', '50% 20%', 'Plesová sezóna · líčení i účes', None),
    '/liceni-na-akce/': ('evening-1-800', 'sand', '50% 20%', 'Galavečery · firemní akce · skupiny', None),
    '/nude-liceni/': ('nude-1-800', 'blush', '50% 30%', 'Přirozený look', None),
    '/komercni-liceni/': ('commercial-4-800', 'ink', '50% 30%', 'Focení · kampaně · editorial', None),
    '/kurzy-liceni/': ('course-1000', 'sand', '50% 15%', 'Individuální lekce', None),
    '/o-mne/': ('nikol-hero-1280', 'ox', '62% 28%', 'O mně · vizážistka Praha', 'Svatby, večery, editorial a kurzy'),
    '/en/about/': ('nikol-hero-1280', 'ox', '62% 28%', 'About · makeup artist Prague', 'Weddings, evenings, editorial and courses'),
    '/portfolio/': ('collage', 'paper', '', 'Svatební · večerní · nude · komerční', None),
    '/en/': ('nikol-hero-1280', 'paper', '50% 28%', 'Makeup artist · Prague', None),
    '/en/wedding/': ('wedding-5-800', 'paper', '50% 30%', 'Weddings · Prague & Europe', None),
    '/en/evening-makeup/': ('evening-5-800', 'ox', '50% 25%', 'Balls · galas · parties', None),
    '/en/nude-makeup/': ('nude-1-800', 'blush', '50% 30%', 'Natural look', None),
    '/en/commercial-makeup/': ('commercial-4-800', 'ink', '50% 30%', 'Shoots · campaigns · editorial', None),
    '/en/courses/': ('course-1000', 'sand', '50% 15%', 'One-on-one lessons', None),
    '/en/portfolio/': ('collage', 'paper', '', 'Bridal · evening · nude · commercial', None),
    '/blog/': ('nude-3-800', 'blush', '50% 30%', 'Tutoriály · recenze · tipy', None),
    '/blog/transition-blush-jak-na-to/': ('commercial-4-800', 'blush', '50% 35%', 'Návod · tvářenka', 'Přechod z korektoru a tvářenky, kterou už máte'),
    '/en/blog/transition-blush-how-to/': ('commercial-4-800', 'blush', '50% 35%', 'How-to · blush', 'A transition from the concealer and blush you already own'),
    '/blog/jak-sbalit-kosmeticku-na-cesty/': ('travel-hero-1280', 'blush', '50% 50%', 'Návod · na cesty', 'Co si vzít a jak z toho udělat denní i večerní make-up'),
    '/en/blog/how-to-pack-a-makeup-bag-for-travel/': ('travel-hero-1280', 'blush', '50% 50%', 'How-to · travel', 'What to take and how to turn it into a day or evening look'),
    '/blog/jak-myt-stetce-na-make-up/': ('brushes-hero-1280', 'blush', '40% 60%', 'Tutoriál · péče o štětce', 'Tuhé mýdlo, technika podle tvaru, olej a správné sušení'),
    '/en/blog/how-to-wash-makeup-brushes/': ('brushes-hero-1280', 'blush', '40% 60%', 'Tutorial · brush care', 'Bar soap, technique by shape, oil and drying right'),
    '/blog/recenze-catrice-cely-oblicej/': ('nikol-portrait-800', 'ox', '50% 22%', 'Recenze · celý obličej', 'Make-up, bronzer, pečená tvářenka a rty z adventního kalendáře'),
    '/en/blog/full-face-of-catrice-review/': ('nikol-portrait-800', 'ox', '50% 22%', 'Reviews · full face', 'Foundation, bronzer, baked blush and lips from the advent calendar'),
    '/blog/dopotrebovana-kosmetika/': ('nikol-header-800', 'blush', '50% 20%', 'Recenze · 25 produktů', 'Co si koupím znovu a co už ne'),
    '/en/blog/beauty-empties-repurchase/': ('nikol-header-800', 'blush', '50% 20%', 'Reviews · 25 products', "What I'd buy again and what I wouldn't"),
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


BLOG_CSS = '''
html,body{margin:0;width:1200px;height:630px;overflow:hidden;background:#fff}
.og{display:grid;grid-template-columns:1fr 520px;gap:28px;height:630px;padding:28px;box-sizing:border-box;font-family:var(--f-tight);color:#111}
.og-l{display:flex;flex-direction:column;justify-content:space-between;padding:28px 8px 20px 28px;min-width:0}
.og-top{display:flex;justify-content:space-between;align-items:baseline;font-size:26px;font-weight:600;letter-spacing:-.02em}
.og-top em{font-family:var(--f-disp);font-style:italic;font-weight:400;font-size:31px}
.og-top small{font-size:16px;font-weight:400;color:#6E6E6E;letter-spacing:0}
.og-lab{font-size:20px;margin-bottom:18px}
.og h1{font-weight:500;font-size:64px;line-height:1.04;letter-spacing:-.035em;margin:0}
.og h1 em{font-family:var(--f-disp);font-style:italic;font-weight:400;font-size:1.12em;letter-spacing:-.01em}
.og-sub{font-size:22px;line-height:1.35;color:#6E6E6E;margin-top:18px;max-width:560px}
.og-bot{display:flex;justify-content:space-between;align-items:center;font-size:18px;color:#6E6E6E}
.og-bot b{background:#111;color:#fff;font-weight:500;padding:12px 20px;border-radius:999px;font-size:17px}
.og .cvover,.og .bcover{height:574px;border-radius:24px;aspect-ratio:auto!important}
.og .cv-panel{left:8%;right:8%;padding:24px 26px;border-radius:28px;gap:18px}
.og .cv-k b{font-size:21px}.og .cv-k small{font-size:13px}.og .cv-big{font-size:42px}.og .cv-bar{height:13px}
.og .cv-stats small{font-size:12px}.og .cv-stats b{font-size:17px}
.og .cv-pill{left:22%;right:22%;top:12%;bottom:12%;border-radius:56px}.og .cv-pill small{font-size:17px}.og .cv-pill b{font-size:44px}
'''


def card_blog(path):
    """Blog index and articles: same look as the blog (title left, tinted cover with glass card right)."""
    from posts import POSTS, ORDER, cover
    lang = 'en' if path.startswith('/en/') else 'cs'
    cs = lang == 'cs'
    key = next((k for k in POSTS if POSTS[k][lang]['path'] == path), None)
    e = html.escape
    if key:
        m = POSTS[key][lang]
        lab, title_html, sub = m['tag'], e(m['title']), PAGES[path][4] or ''
        art = cover(key, lang, '520px', priority=True)
    else:
        lab = 'Blog'
        title_html = 'Líčení, které <em>vydrží.</em>' if cs else 'Makeup that <em>lasts.</em>'
        sub = ('Návody, recenze a zkušenosti z praxe pražské vizážistky.' if cs
               else 'How-tos, reviews and lessons from a Prague makeup artist.')
        art = cover('nyx', lang, '520px', priority=True)
    loc = 'vizážistka · Praha' if cs else 'makeup artist · Prague'
    cta = 'Číst na blogu' if cs else 'Read on the blog'
    maxh = 300 if sub else 380
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><link rel="stylesheet" href="/assets/css/site.css"><style>{BLOG_CSS}</style></head>
<body><div class="og"><div class="og-l">
<div class="og-top"><span>Nikol <em>Pavlova</em></span><small>{e(loc)}</small></div>
<div><p class="og-lab">({e(lab)})</p><h1 id="t">{title_html}</h1>{f'<p class="og-sub">{e(sub)}</p>' if sub else ''}</div>
<div class="og-bot"><span>nikolmakeup.cz/{'blog' if cs else 'en/blog'}</span><b>{e(cta)} →</b></div>
</div>{art}</div>
<script>Promise.all([document.fonts.ready].concat([].map.call(document.images,function(i){{return i.decode().catch(function(){{}})}}))).then(function(){{var t=document.getElementById('t'),s=64;while(t.offsetHeight>{maxh}&&s>36){{s-=2;t.style.fontSize=s+'px'}}document.body.dataset.ready=1}})</script>
</body></html>'''


def card_home(path):
    """Home pages: same layout as the blog cards, Nikol's photo with soft pastel light on the right."""
    cs = path == '/'
    e = html.escape
    sub = 'profesionální vizážistka v Praze' if cs else 'English-speaking makeup artist in Prague'
    chips = (['Svatby', 'Večery', 'Editorial', 'Kurzy'] if cs else ['Weddings', 'Evenings', 'Editorial', 'Courses'])
    cta = 'Rezervovat termín +' if cs else 'Book online +'
    chip_html = ''.join(f'<span class="og-chip">{c}</span>' for c in chips)
    return f'''<!doctype html><html lang="{'cs' if cs else 'en'}"><head><meta charset="utf-8"><link rel="stylesheet" href="/assets/css/site.css"><style>{BLOG_CSS}
.og-ph{{position:relative;overflow:hidden;border-radius:24px;height:574px}}.og-ph img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 28%}}
.og-ph i{{position:absolute;inset:0;background:linear-gradient(120deg,#F6C9C2,#EBC7DA 50%,#F7D9BF);mix-blend-mode:soft-light;opacity:.7}}
.og-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}}.og-chip{{border:1px solid #E6E6E6;border-radius:999px;padding:8px 14px;font-size:17px}}
.og h1{{font-size:84px;line-height:.95}}</style></head>
<body><div class="og"><div class="og-l">
<div class="og-top"><span>{'5,0' if cs else '5.0'} ★ Google</span><small>{'Praha 8 – Karlín' if cs else 'Prague 8 – Karlín'}</small></div>
<div><p class="og-lab">({e(sub)})</p><h1 id="t">Nikol <em>Pavlova</em></h1><div class="og-chips">{chip_html}</div></div>
<div class="og-bot"><span>nikolmakeup.cz{'' if cs else '/en'}</span><b>{e(cta)}</b></div>
</div><div class="og-ph"><img src="/assets/img/nikol-hero-1280.webp"><i></i></div></div>
<script>Promise.all([document.fonts.ready,document.images[0].decode().catch(function(){{}})]).then(function(){{document.body.dataset.ready=1}})</script>
</body></html>'''


NEW_SVC = {  # service pages already in the 2026-11 design: path -> (photo, object-position)
    '/svatebni-liceni/': ('wedding-15-800', '45% 30%'),
    '/en/wedding/': ('wedding-15-800', '45% 30%'),
}


def card_svc(path):
    """Service pages in the new design: H1 on the left, the hero photo with soft pastel light on the right."""
    lang, title, sub = page_text(path)
    cs = lang == 'cs'
    photo, pos = NEW_SVC[path]
    e = html.escape
    cta = 'Rezervovat termín +' if cs else 'Book online +'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><link rel="stylesheet" href="/assets/css/site.css"><style>{BLOG_CSS}
.og-ph{{position:relative;overflow:hidden;border-radius:24px;height:574px}}.og-ph img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}}}
.og-ph i{{position:absolute;inset:0;background:linear-gradient(150deg,#F7D9BF,#F2CDD6 55%,#DCCFF0);mix-blend-mode:soft-light;opacity:.45}}
.og h1{{font-size:80px;line-height:.95}}</style></head>
<body><div class="og"><div class="og-l">
<div class="og-top"><span>Nikol <em>Pavlova</em></span><small>{'5,0' if cs else '5.0'} ★ Google</small></div>
<div><h1 id="t">{e(title)}</h1><p class="og-sub" style="font-family:var(--f-disp);font-style:italic;font-size:30px;color:#3A3A3A">{e(sub)}</p></div>
<div class="og-bot"><span>nikolmakeup.cz{e(path)}</span><b>{e(cta)}</b></div>
</div><div class="og-ph"><img src="/assets/img/{photo}.webp"><i></i></div></div>
<script>Promise.all([document.fonts.ready,document.images[0].decode().catch(function(){{}})]).then(function(){{var t=document.getElementById('t'),s=80;while(t.offsetHeight>250&&s>40){{s-=2;t.style.fontSize=s+'px'}}document.body.dataset.ready=1}})</script>
</body></html>'''


def main():
    tmp = os.path.join(ROOT, '_build', 'og_tmp')
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'assets', 'og'), exist_ok=True)
    jobs = []
    only = sys.argv[1] if len(sys.argv) > 1 else ''          # e.g. "blog" renders only the blog cards
    for path in PAGES:
        if only and not (only == 'home' and path in ('/', '/en/')) and not (only == 'new' and path in NEW_SVC) and (only in ('home', 'new') or only not in path):
            continue
        slug = og_slug(path)
        html_ = (card_blog(path) if '/blog/' in path else card_home(path) if path in ('/', '/en/')
                 else card_svc(path) if path in NEW_SVC else card(path))
        open(os.path.join(tmp, slug + '.html'), 'w', encoding='utf-8').write(html_)
        jobs.append([f'http://localhost:8765/_build/og_tmp/{slug}.html', os.path.join(ROOT, 'assets', 'og', slug + '.png')])
    subprocess.run(['node', os.path.join(ROOT, '_build', 'og.js'), json.dumps(jobs)], check=True)
    from PIL import Image
    for _, png in jobs:
        Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=86, optimize=True, progressive=True)
        os.remove(png)
    print(len(jobs), 'OG images')


if __name__ == '__main__':
    main()
