"""Service-page components in the 2026-11 style (Inter Tight + Instrument Serif, pastel, glass).
Same data as the lib.py components they replace, so pages can switch one by one."""
from lib import *
from lib import img as I


def _h2(title, hid, label=''):
    """Title like 'Balíčky svatebního líčení': last words go italic when a '|' marks the split."""
    a, _, b = title.partition('|')
    em = f' <em>{b.strip()}</em>' if b else ''
    lab = f'<p class="u-label">({label})</p>' if label else ''
    return f'{lab}<h2 class="u-h2" id="{hid}">{a.strip()}{em}</h2>'


def hero_svc(lang, crumb_items, big, sub, desc, cta, photos, quote=None):
    """Split hero: text on a pastel field, two photos on the right. photos: [(name, alt, crop_class), ...]."""
    (p1, a1, c1), (p2, a2, c2) = photos
    q = ''
    if quote:
        q = f'<figure class="u-quote"><span class="u-stars" aria-hidden="true">★★★★★</span><blockquote>{quote[0]}</blockquote><figcaption>{quote[1]}</figcaption></figure>'
    return f'''<div class="u">
<section class="u-hero" aria-labelledby="page-h1">
<div class="u-hero-txt">
{crumbs(lang, crumb_items, cls='u-crumbs')}
<h1 class="u-h1" id="page-h1"><span class="big">{big}</span><span class="sub">{sub}</span></h1>
<p class="u-lead">{desc}</p>
<p><a class="u-btn u-btn--dark" href="{cta[0]}">{cta[1]}</a></p>
</div>
<div class="u-hero-ph">
<span class="u-ph u-ph--a">{I(p1, a1, sizes='(max-width: 900px) 60vw, 30vw', cls=c1, priority=True)}<span class="u-ph-gel" aria-hidden="true"></span></span>
<div class="u-hero-col"><span class="u-ph u-ph--b">{I(p2, a2, sizes='(max-width: 900px) 40vw, 22vw', cls=c2)}</span>{q}</div>
</div>
</section>
</div>
'''


def strip(items):
    s = ''.join(f'<span>{x}</span><span class="u-dot" aria-hidden="true">✦</span>' for x in items)
    return f'<div class="u u-strip" aria-hidden="true"><div class="u-mq">{s}{s}</div></div>\n'


def intro2(label, title, tag, imgs, body, chips, cta=None):
    phs = ''.join(f'<span class="u-ph u-ph--i{k}">{I(n, alt, sizes="(max-width: 900px) 50vw, 25vw")}</span>' for k, (n, alt) in enumerate(imgs or []))
    ticks = ''.join(f'<li><span class="u-tick" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12l5 5 9-10"/></svg></span>{c}</li>' for c in chips or [])
    cta_html = f'<p><a class="u-btn u-btn--dark" href="{cta[0]}">{cta[1]}</a></p>' if cta else ''
    ph_html = f'<div class="u-intro-ph">{phs}</div>' if phs else ''
    return f'''<section class="u wrap u-intro{'' if phs else ' u-intro--solo'}" aria-labelledby="intro-h">
{ph_html}
<div class="u-intro-txt">
<p class="u-label">({label})</p>
<h2 class="u-h2" id="intro-h">{title}</h2>
<p class="u-tag"><em>{tag}</em></p>
<p class="u-p">{body}</p>
<ul class="u-ticks" role="list">{ticks}</ul>
{cta_html}
</div>
</section>
'''


def features2(title, sub, cells, hid='grid-h'):
    """Same cells as lib.checker: images and panels are paired in order."""
    imgs = [c for c in cells if c[0] == 'img']
    panels = [c for c in cells if c[0] == 'panel']
    out = ''
    for k, (p, im) in enumerate(zip(panels, imgs)):
        _, num, h, txt, _alt = p
        out += (f'<li class="u-ft"><span class="u-ph u-ph--ft">{I(im[1], im[2], sizes="(max-width: 700px) 100vw, 25vw")}'
                f'<span class="u-ph-gel u-gel--{k + 1}" aria-hidden="true"></span><span class="u-num" aria-hidden="true">{num}</span></span>'
                f'<h3>{h}</h3><p>{txt}</p></li>')
    return f'''<section class="u wrap u-sec" aria-labelledby="{hid}">
<div class="u-head"><div>{_h2(title, hid, sub)}</div></div>
<ul class="u-feats" role="list">{out}</ul>
</section>
'''


def pricing2(label, title, note, cols, cta_href='#contact', imgs=None):
    """Same cols as lib.ox_pricing: (heading, badge, [items], button). imgs: optional photo per column."""
    out = ''
    for k, (h, badge, items, btn) in enumerate(cols):
        ph = ''
        if imgs and k < len(imgs):
            n, alt = imgs[k]
            ph = f'<span class="u-pc-ph">{I(n, alt, sizes="(max-width: 900px) 100vw, 50vw")}</span>'
        lis = ''.join(f'<li>— {i}</li>' for i in items)
        out += (f'<li class="u-pc">{ph}<div class="u-pc-b"><div class="u-pc-row"><h3>{h}</h3><span class="u-price">{badge}</span></div>'
                f'<ul class="u-pc-list" role="list">{lis}</ul><p><a class="u-btn u-btn--dark" href="{cta_href}">{btn}</a></p></div></li>')
    return f'''<section class="u u-pastel" id="packages" aria-labelledby="pkg-h"><div class="wrap">
<div class="u-head"><div>{_h2(title, 'pkg-h', label)}</div><p class="u-note">{note}</p></div>
<ul class="u-pcs" role="list">{out}</ul>
</div></section>
'''


def steps2(title, sub, items, aside=''):
    lis = ''.join(f'<li><span class="u-sn" aria-hidden="true">{i + 1:02d}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(items))
    right = f'<p class="u-note">{aside}</p>' if aside else ''
    return f'''<section class="u wrap u-sec" aria-labelledby="steps-h">
<div class="u-head"><div>{_h2(title, 'steps-h', sub)}</div>{right}</div>
<ol class="u-steps">{lis}</ol>
</section>
'''


def gallery2(title, sub, right_label, right_href, items):
    imgs = ''.join(f'<span class="u-gl u-gl--{k + 1}">{I(n, alt, sizes="(max-width: 900px) 50vw, 25vw")}</span>' for k, (n, alt) in enumerate(items))
    return f'''<section class="u wrap u-sec" aria-labelledby="gal-h">
<div class="u-head"><div>{_h2(title, 'gal-h', sub)}</div><a class="u-link" href="{right_href}">{right_label} →</a></div>
<div class="u-gallery{" u-gallery--3" if len(items) < 4 or (len(items) % 4 and len(items) % 3 == 0) else ""}">{imgs}</div>
</section>
'''


def related2(lang, items):
    t = L[lang]
    out = ''.join(f'<li><a class="u-rel" href="{href}">{I(imgname, "", sizes="(max-width: 900px) 100vw, 50vw")}<span class="u-rel-t">{label} →</span></a></li>'
                  for label, href, imgname in items)
    return f'''<section class="u wrap u-sec" aria-label="{t['related']}">
<p class="u-label">({t['related']})</p>
<ul class="u-rels" role="list">{out}</ul>
</section>
'''


# ---------------------------------------------------------------- photos per service page (new photos 2026-11)
ALT = {  # name: (cs, en)
    'ev-cap': ('Editorial look – výrazné oči a čepice', 'Editorial look – bold eyes and cap'),
    'ev-black': ('Večerní look – přirozená pleť a dlouhé vlasy', 'Evening look – natural skin and long hair'),
    'ev-gold': ('Večerní look – zlaté šaty a drdol', 'Evening look – gold dress and updo'),
    'ev-red': ('Večerní look – zrzavé vlasy a drdol', 'Evening look – red hair and updo'),
    'ev-green-emb': ('Večerní look – vyšívané šaty a kudrliny', 'Evening look – embroidered dress and curls'),
    'ev-green-gown': ('Plesový look – zelené šaty a vysoký culík', 'Ball look – green gown and high ponytail'),
    'ev-stairs': ('Plesový look – sametové šaty na schodech', 'Ball look – velvet gown on the stairs'),
    'ev-pink-gown': ('Večerní look – pudrové šaty a drdol', 'Evening look – blush gown and updo'),
    'hair-waves-back': ('Účes – hollywoodské vlny', 'Hairstyle – Hollywood waves'),
    'hair-waves': ('Účes – velké vlny a večerní make-up', 'Hairstyle – big waves and evening makeup'),
    'hair-red': ('Účes – zrzavé vlny a jemný glam', 'Hairstyle – red waves and soft glam'),
    'hair-brown-waves': ('Účes – lesklé hnědé vlny', 'Hairstyle – glossy brown waves'),
    'hair-curls': ('Účes – objemné kudrliny', 'Hairstyle – voluminous curls'),
    'hair-updo': ('Účes – elegantní drdol', 'Hairstyle – elegant updo'),
}

SVC_PHOTOS = {  # cs path / en path -> hero pair, pricing photos, optional new gallery
    'evening': dict(hero=['ev-black', 'ev-pink-gown'], price=['ev-red', 'hair-waves'],
                    gallery=['ev-cap', 'ev-black', 'ev-gold', 'ev-red', 'ev-green-emb', 'ev-green-gown', 'ev-stairs', 'ev-pink-gown']),
    'plesy': dict(hero=['ev-green-gown', 'hair-updo'], price=['ev-stairs', 'hair-curls'],
                  gallery=['hair-waves-back', 'hair-waves', 'hair-red', 'hair-brown-waves', 'hair-curls', 'hair-updo', 'ev-gold', 'ev-green-emb']),
    'akce': dict(hero=['ev-gold', 'ev-stairs'], price=['ev-red', 'hair-brown-waves']),
    'nude': dict(hero=['nude-1', 'nude-3'], price=['nude-2']),
    'commercial': dict(hero=['ev-cap', 'commercial-6'], price=['commercial-4']),
}
PATH_KEY = {'/vecerni-liceni/': 'evening', '/en/evening-makeup/': 'evening', '/plesove-liceni/': 'plesy', '/liceni-na-akce/': 'akce',
            '/nude-liceni/': 'nude', '/en/nude-makeup/': 'nude', '/komercni-liceni/': 'commercial', '/en/commercial-makeup/': 'commercial'}


def _alt(name, lang, fallback):
    return ALT[name][0 if lang == 'cs' else 1] if name in ALT else fallback


def review_quote(revs, lang):
    """First sentence of the first review, unchanged words; cut at a word if long."""
    import re as _re
    t = _re.sub(r'<[^>]+>', '', revs[0]['text']).strip('„“”"’‘ ')
    t = t.replace('&amp;', '&')
    first = _re.split(r'(?<=[.!?])\s', t)[0]
    if len(first) > 90:
        first = first[:88].rsplit(' ', 1)[0] + '…'
    q = f'„{first}“' if lang == 'cs' else f'“{first}”'
    return q.replace('&', '&amp;'), ('5,0 na Googlu' if lang == 'cs' else '5.0 on Google')


def svc_photos(cfg, lang):
    p = SVC_PHOTOS[PATH_KEY[cfg['path']]]
    hero = [(n, _alt(n, lang, cfg['hero_alt'] if k == 0 else ''), 'u-c2') for k, n in enumerate(p['hero'])]
    price = [(n, _alt(n, lang, '')) for n in p['price']]
    gal = [(n, _alt(n, lang, '')) for n in p['gallery']] if p.get('gallery') else cfg['gallery']
    return hero, price, gal


def banner2(html):
    """Old banner markup, shown in the new style (see .u-bw in site.css)."""
    return f'<div class="u u-bw">{html}</div>\n' if html else ''


SECOND_PHOTO = {'course': ('nude-2', 'u-c2')}


def hero_from_split(lang, tone, crumb_items, big, sub, desc, buttons, imgname, imgalt, obj_pos='50% 30%'):
    """Drop-in for lib.hero_split: same arguments, new split hero with a second photo."""
    n2, c2 = SECOND_PHOTO.get(imgname, (imgname, 'u-c2'))
    return hero_svc(lang, crumb_items, big.replace('<br>', ' '), sub, desc, (buttons[0][1], buttons[0][0]),
                    [(imgname, imgalt, 'u-c3'), (n2, '', c2)])
