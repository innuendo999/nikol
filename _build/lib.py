"""Shared components for the static site generator. Pure Python, no dependencies."""
import json, os, html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://nikolmakeup.cz'
CAL = 'https://calendly.com/pavlovanikol/makeup-hair'
TEL = '+420608178390'
TEL_H = '+420 608 178 390'
MAIL = 'pavlovanikol@gmail.com'
IG = 'https://www.instagram.com/nikol__mua'
FB = 'https://www.facebook.com/nikki.yumi'
TH = 'https://www.threads.net/@nikol_pavlova_mua'
GBP = 'https://g.page/r/CVT7YlUrAr22EBM/'          # Google Business Profile
GBP_REVIEW = GBP + 'review'
VERSION = '20261019'
IMG = json.load(open(os.path.join(ROOT, '_build', 'images.json')))


def a(text):
    return _html.escape(text, quote=True)


def img(name, alt, sizes='(max-width: 900px) 50vw, 25vw', cls='', eager=False, style='', priority=False):
    variants = IMG[name]
    srcset = ', '.join(f'/assets/img/{name}-{w}.webp {w}w' for w, h in variants)
    w, h = variants[-1]
    src = f'/assets/img/{name}-{variants[0][0]}.webp'
    attrs = [f'src="{src}"', f'srcset="{srcset}"', f'sizes="{sizes}"', f'width="{w}"', f'height="{h}"', f'alt="{a(alt)}"']
    if priority:
        attrs.append('fetchpriority="high"')
    if not eager and not priority:
        attrs.append('loading="lazy"')
    attrs.append('decoding="async"')
    if cls:
        attrs.append(f'class="{cls}"')
    if style:
        attrs.append(f'style="{style}"')
    return '<img ' + ' '.join(attrs) + '>'


def preload(name, sizes):
    variants = IMG[name]
    srcset = ', '.join(f'/assets/img/{name}-{w}.webp {w}w' for w, h in variants)
    return f'<link rel="preload" as="image" type="image/webp" imagesrcset="{srcset}" imagesizes="{sizes}" fetchpriority="high">'


ICON_CHEV = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6"/></svg>'
ICON_MENU = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

L = {
    'cs': dict(
        skip='Přeskočit na obsah', home='Domů', about='O mně', portfolio='Portfolio', services='Služby', blog='Blog',
        contact='Kontakt', book='Rezervovat', menu='Menu', main_nav='Hlavní navigace', other='EN', other_label='EN – English version',
        crumbs='Drobečková navigace', services_list=[
            ('Svatební líčení', '/svatebni-liceni/'), ('Večerní líčení', '/vecerni-liceni/'), ('Nude makeup', '/nude-liceni/'),
            ('Komerční líčení', '/komercni-liceni/'), ('Kurzy líčení', '/kurzy-liceni/')],
        blog_href='/en/blog/', home_href='/', portfolio_href='/portfolio/',
        f_services='Služby', f_location='Lokace', f_write='Napište mi', f_call='Telefon / WhatsApp',
        f_loc_text='Praha 7, Česká republika<br>(Možnost dojezdu po Praze, ČR i Evropě)',
        rights='Všechna práva vyhrazena', top='Nahoru ↑', online='Rezervace online +', email='E-mail',
        reviews_title='Recenze z Google', reviews_all='Všechny recenze na Google →', stars='Hodnocení 5 z 5', g_review='Recenze Google', review_write='Napsat recenzi', f_gbp='Google profil',
        faq_title='Časté dotazy', related='Související služba',
    ),
    'en': dict(
        skip='Skip to content', home='Home', about='About', portfolio='Portfolio', services='Services', blog='Blog',
        contact='Contact', book='Book online', menu='Menu', main_nav='Main navigation', other='CZ', other_label='CZ – Česká verze',
        crumbs='Breadcrumb', services_list=[
            ('Wedding makeup', '/en/wedding/'), ('Evening makeup', '/en/evening-makeup/'), ('Nude makeup', '/en/nude-makeup/'),
            ('Commercial makeup', '/en/commercial-makeup/'), ('Makeup courses', '/en/courses/')],
        blog_href='/en/blog/', home_href='/en/', portfolio_href='/en/portfolio/',
        f_services='Services', f_location='Location', f_write='Write to me', f_call='Phone / WhatsApp',
        f_loc_text='Prague 7, Czech Republic<br>(Available across Prague, Czechia &amp; Europe)',
        rights='All rights reserved', top='Back to top ↑', online='Book online +', email='Email',
        reviews_title='Google reviews', reviews_all='All reviews on Google →', stars='Rated 5 out of 5', g_review='Google review', review_write='Write a review', f_gbp='Google profile',
        faq_title='FAQ', related='Related service',
    ),
}


def font_preloads(lang):
    files = ['archivo-latin', 'archivo-latin-ext', 'lora-latin'] + (['lora-latin-ext'] if lang == 'cs' else [])
    return '\n'.join(f'<link rel="preload" href="/assets/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>' for f in files)


def head(lang, title, desc, path, alternates, og_image, schema, preload_html='', og_type='website', extra=''):
    url = SITE + path
    alt_html = '\n'.join(f'<link rel="alternate" hreflang="{hl}" href="{SITE}{p}">' for hl, p in alternates)
    ld = '\n'.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False, separators=(',', ':')) + '</script>' for s in schema)
    locale = 'cs_CZ' if lang == 'cs' else 'en_GB'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a(title)}</title>
<meta name="description" content="{a(desc)}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<link rel="canonical" href="{url}">
{alt_html}
<meta name="theme-color" content="#FBF7F5">
<meta name="geo.region" content="CZ-PR">
<meta name="geo.placename" content="Praha">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Nikol Pavlova">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{a(title)}">
<meta property="og:description" content="{a(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/images/favicon.png" type="image/png">
{font_preloads(lang)}
{preload_html}
<link rel="stylesheet" href="/assets/css/site.css?v={VERSION}">
<script src="/assets/js/site.js?v={VERSION}" defer></script>
{extra}
{ld}
</head>
<body>
'''


def header(lang, active, other_href):
    t = L[lang]
    def cur(key, href, label):
        attr = ' aria-current="page"' if active == key else ''
        return f'<li><a class="nav-link" href="{href}"{attr}>{label}</a></li>'
    svc_items = ''.join(
        f'<li><a href="{u}"{" aria-current=" + chr(34) + "page" + chr(34) if active == u else ""}>{n}</a></li>' for n, u in t['services_list'])
    svc_active = ' is-active' if active in [u for n, u in t['services_list']] else ''
    blog_lang = ' hreflang="en"' if lang == 'cs' else ''
    other_lang = 'en' if lang == 'cs' else 'cs'
    return f'''<a class="skip-link" href="#main">{t['skip']}</a>
<header class="site-header">
<div class="wrap">
<div class="bar glass">
<a class="logo" href="{t['home_href']}">Nikol Pavlova</a>
<nav class="nav" id="site-nav" aria-label="{t['main_nav']}">
<ul>
{cur('home', t['home_href'], t['home'])}
<li><a class="nav-link" href="{t['home_href']}#about">{t['about']}</a></li>
{cur('portfolio', t['portfolio_href'], t['portfolio'])}
<li class="dd"><button class="nav-link dd-btn{svc_active}" type="button" aria-expanded="false" aria-controls="dd-services">{t['services']} {ICON_CHEV}</button>
<ul class="dd-menu glass" id="dd-services">{svc_items}</ul></li>
{cur('blog', t['blog_href'], t['blog']).replace('<a ', '<a' + blog_lang + ' ', 1) if blog_lang else cur('blog', t['blog_href'], t['blog'])}
<li><a class="nav-link" href="#contact">{t['contact']}</a></li>
</ul>
</nav>
<div class="bar-end">
<a class="lang lbl" href="{other_href}" hreflang="{other_lang}" lang="{other_lang}" aria-label="{t['other_label']}">{t['other']}</a>
<a class="btn" href="{CAL}">{t['book']} <span aria-hidden="true">+</span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{t['menu']}">{ICON_MENU}</button>
</div>
</div>
</div>
</header>
<main id="main">
'''


def footer(lang, cta_label, cta_title, cta_text, primary=None):
    t = L[lang]
    primary = primary or (CAL, t['online'])
    svc = ''.join(f'<a href="{u}">{n}</a>' for n, u in t['services_list'])
    return f'''</main>
<footer class="site-footer" id="contact">
<div class="wrap">
<div class="cols-f">
<div class="cta-f">
<p class="lbl pink">{cta_label}</p>
<h2 class="mid-h">{cta_title}</h2>
<p>{cta_text}</p>
<p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn--pink" href="{primary[0]}">{primary[1]}</a><a class="btn btn--ghost" href="mailto:{MAIL}">{t['email']}</a></p>
</div>
<nav class="f-col" aria-label="{t['f_services']}"><h3 class="lbl">{t['f_services']}</h3>{svc}</nav>
<div class="f-col"><h3 class="lbl">{t['f_location']}</h3><address>{t['f_loc_text']}</address></div>
<div class="f-col"><h3 class="lbl">{t['f_write']}</h3><a href="mailto:{MAIL}">{MAIL}</a><a href="{IG}">Instagram @nikol__mua</a><a href="{FB}">Facebook</a><a href="{TH}">Threads</a><a href="{GBP}">{t['f_gbp']}</a></div>
<div class="f-col"><h3 class="lbl">{t['f_call']}</h3><a class="tel" href="tel:{TEL}">{TEL_H}</a></div>
</div>
<div class="f-bar lbl"><span>Nikol Pavlova · {'vizážistka Praha' if lang == 'cs' else 'makeup artist Prague'}</span><span>2026 © {t['rights']}</span><a href="{t['portfolio_href']}">{t['portfolio']}</a><a href="{t['blog_href']}"{' hreflang="en"' if lang == 'cs' else ''}>{t['blog']}</a><a href="#main">{t['top']}</a></div>
</div>
<div class="f-name" aria-hidden="true">{img('nikol-footer', '', sizes='100vw')}<div class="mesh"></div><span>Nikol Pavlova</span></div>
</footer>
</body>
</html>
'''


def marquee(items):
    seq = ''.join(f'<span>{i}</span><span>✦</span>' for i in items)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee__track">{seq}{seq}</div></div>\n'


def sec_head(title, sub='', right='', hid='', tag='h2'):
    sub_html = f' <span class="serif">– {sub}</span>' if sub else ''
    idattr = f' id="{hid}"' if hid else ''
    return f'<div class="sec-head"><{tag} class="sec-title"{idattr}>{title}{sub_html}</{tag}>{right}</div>\n'


def crumbs(lang, items, cls='lbl'):
    """items: list of (label, href or None for current)."""
    lis = ''.join(
        f'<li><a href="{h}">{n}</a></li>' if h else f'<li><span aria-current="page">{n}</span></li>' for n, h in items)
    return f'<nav class="crumbs {cls}" aria-label="{L[lang]["crumbs"]}"><ol>{lis}</ol></nav>'


def faq(lang, title_sub, items, hid='faq'):
    det = ''
    for i, (q, ans) in enumerate(items):
        op = ' open' if i == 0 else ''
        det += f'<details{op}><summary><h3>{q}</h3><span class="pm" aria-hidden="true">+</span></summary><div><p>{ans}</p></div></details>\n'
    return f'''<section class="sec sec--blush" aria-labelledby="{hid}-h">
<div class="wrap">
{sec_head(L[lang]['faq_title'], title_sub, hid=hid + '-h')}
<div class="faq">
{det}</div>
</div>
</section>
'''


def reviews(lang, sub, items, top=True):
    t = L[lang]
    figs = ''
    for r in items:
        figs += (f'<figure class="rv"><span class="st" role="img" aria-label="{t["stars"]}">★★★★★</span>'
                 f'<blockquote lang="{r["lang"]}"><p>{r["text"]}</p></blockquote>'
                 f'<figcaption><span class="av" aria-hidden="true">{r["ini"]}</span><span><cite class="lbl">{r["name"]}</cite><br><span class="src">{t["g_review"]}{r.get("extra", "")}</span></span></figcaption></figure>\n')
    pad = 'sec' if top else 'sec--tight'
    right = (f'<p class="actions"><a class="btn" href="{GBP}">{t["reviews_all"]}</a>'
             f'<a class="btn btn--outline" href="{GBP_REVIEW}">{t["review_write"]}</a></p>')
    return f'''<section class="{pad}" aria-labelledby="reviews-h">
<div class="wrap">
{sec_head(t['reviews_title'], sub, right, hid='reviews-h')}
<div class="rvs">
{figs}</div>
</div>
</section>
'''


def steps(title, sub, items, aside=''):
    lis = ''.join(f'<li><span class="n" aria-hidden="true">{i + 1:02d}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(items))
    right = f'<p class="body" style="max-width:460px">{aside}</p>' if aside else ''
    return f'''<section class="sec" aria-labelledby="steps-h">
<div class="wrap">
{sec_head(title, sub, right, hid='steps-h')}
<ol class="steps">{lis}</ol>
</div>
</section>
'''


def tiles(lang, items):
    t = L[lang]
    out = ''
    for label, href, imgname in items:
        out += f'<a href="{href}">{img(imgname, "", sizes="(max-width: 900px) 100vw, 50vw")}<span class="cap"><span class="lbl pink">{t["related"]}</span><span class="wide">{label} →</span></span></a>'
    return f'<section class="tiles" aria-label="{t["related"]}">{out}</section>\n'


def ox_pricing(label, title, note, cols, cta_href='#contact', cta=None):
    """cols: list of (heading, badge, [items], button_label)."""
    if len(cols) == 1:
        h, badge, items, btn = cols[0]
        lis = ''.join(f'<li>{i}</li>' for i in items)
        return f'''<section class="sec sec--ox" id="packages" aria-labelledby="pkg-h">
<div class="wrap ox-split">
<div style="display:flex;flex-direction:column;gap:18px"><p class="lbl pink">{label}</p><h2 class="big-h" id="pkg-h">{title}</h2><p class="serif ox-note">{note}</p></div>
<div style="display:flex;flex-direction:column;gap:24px"><div class="row" style="display:flex;justify-content:space-between;gap:16px;align-items:baseline"><h3 class="wide" style="font-size:24px;font-weight:500">{h}</h3><span class="lbl pink">{badge}</span></div><ul class="ox-list">{lis}</ul><a class="btn btn--pink" href="{cta_href}" style="align-self:flex-start">{btn}</a></div>
</div>
</section>
'''
    colhtml = ''
    for h, badge, items, btn in cols:
        lis = ''.join(f'<li>{i}</li>' for i in items)
        colhtml += f'<div class="ox-col"><div class="row"><h3>{h}</h3><span class="lbl pink">{badge}</span></div><ul class="ox-list">{lis}</ul><a class="btn btn--pink" href="{cta_href}" style="align-self:flex-start">{btn}</a></div>'
    return f'''<section class="sec sec--ox" id="packages" aria-labelledby="pkg-h">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div class="sec-head" style="margin:0"><div><p class="lbl pink">{label}</p><h2 class="big-h" id="pkg-h" style="margin-top:8px">{title}</h2></div><p class="serif ox-note" style="max-width:460px">{note}</p></div>
<div class="ox-grid">{colhtml}</div>
</div>
</section>
'''


def intro(label, title, tag, imgs, body, chips, cta=None):
    pair = ''.join(img(n, alt, sizes='260px') for n, alt in imgs) if imgs else ''
    pair_html = f'<div class="pair">{pair}</div>' if pair else ''
    chips_html = '<ul class="chips">' + ''.join(f'<li>{c}</li>' for c in chips) + '</ul>' if chips else ''
    cta_html = f'<a class="btn" href="{cta[0]}">{cta[1]}</a>' if cta else ''
    return f'''<section class="wrap intro" aria-labelledby="intro-h">
<div class="head"><p class="lbl red">{label}</p><h2 class="mid-h" id="intro-h">{title}</h2><p class="serif tag">{tag}</p></div>
{pair_html}
<p class="body">{body}</p>
{chips_html}
{cta_html}
</section>
'''


def checker(title, sub, cells, hid='grid-h'):
    """cells: ('img', name, alt) or ('panel', num, h3, text, alt_bg)"""
    out = ''
    for c in cells:
        if c[0] == 'img':
            out += img(c[1], c[2], sizes='(max-width: 900px) 50vw, 25vw')
        else:
            _, num, h, txt, alt = c
            out += f'<div class="tile-panel{" alt" if alt else ""}"><span class="lbl red">{num}</span><h3>{h}</h3><p class="serif">{txt}</p></div>'
    return f'''<section aria-labelledby="{hid}">
<div class="wrap">{sec_head(title, sub, hid=hid)}</div>
<div class="g4">{out}</div>
</section>
'''


def gallery(title, sub, right_label, right_href, items, c3=False):
    imgs = ''.join(img(n, alt, sizes='(max-width: 900px) 50vw, 25vw') for n, alt in items)
    right = f'<a class="link-arrow" href="{right_href}">{right_label} →</a>'
    return f'''<section class="sec--tight" aria-labelledby="gal-h">
<div class="wrap">
{sec_head(title, sub, right, hid='gal-h')}
<div class="cols{' c3' if c3 else ''}">{imgs}</div>
</div>
</section>
'''


def hero_split(lang, tone, crumb_items, big, sub, desc, buttons, imgname, imgalt, obj_pos='50% 30%'):
    btns = ''
    for i, (label, href) in enumerate(buttons):
        if i == 0:
            cls = 'btn btn--pink' if tone in ('tone-ox', 'tone-ink') else 'btn'
        else:
            cls = 'btn btn--ghost' if tone in ('tone-ox', 'tone-ink') else 'btn btn--outline'
        btns += f'<a class="{cls}" href="{href}"{" rel=" + chr(34) + "noopener" + chr(34) if href.startswith("http") else ""}>{label}</a>'
    return f'''<section class="hero-split" aria-labelledby="page-h1">
<div class="panel {tone}">
{crumbs(lang, crumb_items)}
<div style="display:flex;flex-direction:column;gap:24px">
<h1 class="h1" id="page-h1"><span class="big">{big}</span><span class="sub">{sub}</span></h1>
<p class="desc">{desc}</p>
<p style="display:flex;gap:12px;flex-wrap:wrap">{btns}</p>
</div>
</div>
{img(imgname, imgalt, sizes='(max-width: 900px) 100vw, 50vw', priority=True, style=f'object-position:{obj_pos}')}
</section>
'''


def write(path, html_str):
    out = os.path.join(ROOT, path.lstrip('/'), 'index.html') if path.endswith('/') else os.path.join(ROOT, path.lstrip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    from utilities import apply
    with open(out, 'w', encoding='utf-8') as f:
        f.write(apply(html_str).replace('', ''))
    return out
