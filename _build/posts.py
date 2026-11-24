"""Blog post registry (both languages) and the "From the blog" block used on service pages."""
from lib import img, sec_head

POSTS = {
    'blush': {
        'date': '2026-11-23', 'img': 'commercial-4', 'video': 'qIsRGQgTsOk',
        'cs': dict(path='/blog/transition-blush-jak-na-to/', crumb='Transition blush', tag='Návod',
                   title='Transition blush: jak na rozmazanou tvářenku bez nové kolekce',
                   seo_title='Transition blush: jak na to krok za krokem | Nikol Pavlova',
                   desc='Co je transition blush, kdo ho vymyslel (Kevyn Aucoin, Paint By Ester, Patrick Ta) a jak ho udělat z korektoru a tvářenky, které už máte. Interaktivní návod od vizážistky.',
                   card='Transition blush bez kolekce za 120 dolarů: kdo techniku vymyslel, jak si namíchat přechod z korektoru a tvářenky a kam ji dát podle tvaru obličeje.'),
        'en': dict(path='/en/blog/transition-blush-how-to/', crumb='Transition blush', tag='How-to',
                   title='Transition Blush: How to Get the Blurred Blush Without a New Kit',
                   seo_title='Transition Blush: How to Do It Step by Step | Nikol Pavlova',
                   desc='What transition blush is, who came up with it (Kevyn Aucoin, Paint By Ester, Patrick Ta) and how to do it with the concealer and blush you already own. An interactive guide by a makeup artist.',
                   card='Transition blush without a $120 kit: who came up with the technique, how to mix the transition from concealer and blush, and where to place it for your face shape.'),
    },
    'travel': {
        'date': '2026-11-17', 'img': 'travel-hero', 'video': 'Sb-Sg-GVoVM',
        'cs': dict(path='/blog/jak-sbalit-kosmeticku-na-cesty/', crumb='Jak sbalit kosmetičku na cesty', tag='Návod',
                   title='Jak sbalit kosmetičku na cesty: návod vizážistky',
                   seo_title='Jak sbalit kosmetičku na cesty: návod vizážistky | Nikol Pavlova',
                   desc='Jak sbalit kosmetičku na cesty: co si vzít, pět štětců, které stačí, a jak z malé kosmetičky udělat denní i večerní make-up. Návod krok za krokem od vizážistky Nikol Pavlové.',
                   card='Co si sbalit do kosmetičky na cesty, aby z ní šel denní i večerní make-up: seznam na odškrtání, pět štětců a interaktivní návod krok za krokem.'),
        'en': dict(path='/en/blog/how-to-pack-a-makeup-bag-for-travel/', crumb='How to pack a makeup bag', tag='How-to',
                   title="How to Pack a Makeup Bag for Travel: A Makeup Artist's Guide",
                   seo_title='How to Pack a Makeup Bag for Travel | Nikol Pavlova, Makeup Artist',
                   desc='How to pack a makeup bag for travel: what to take, the five brushes you need and how to turn one small bag into a day or evening look. A step-by-step guide by makeup artist Nikol Pavlova.',
                   card='What to pack in a travel makeup bag so it covers a day and an evening look: a tick-off list, five brushes and an interactive step-by-step guide.'),
    },
    'brushes': {
        'date': '2026-11-16', 'img': 'brushes-hero', 'video': 'gc_bq04a_G0',
        'cs': dict(path='/blog/jak-myt-stetce-na-make-up/', crumb='Jak mýt štětce', tag='Tutoriál',
                   title='Jak mýt štětce na make-up: postup vizážistky',
                   seo_title='Jak mýt štětce na make-up: rychle, levně a šetrně | Nikol Pavlova',
                   desc='Vizážistka Nikol Pavlova z Prahy ukazuje, jak myje štětce na make-up: tuhé mýdlo, technika podle tvaru štětce, olej na make-up a rtěnku a správné sušení, aby štětce vydržely roky.',
                   card='Jak myju desítky štětců denně: tuhé mýdlo, krouživě nebo tahy podle tvaru, olej na rtěnku a sušení naplocho. A proč nikdy štětinami nahoru.'),
        'en': dict(path='/en/blog/how-to-wash-makeup-brushes/', crumb='How to wash makeup brushes', tag='Tutorial',
                   title='How to Wash Makeup Brushes: A Makeup Artist\'s Routine',
                   seo_title='How to Wash Makeup Brushes: Fast, Cheap and Gentle | Nikol Pavlova',
                   desc='Prague makeup artist Nikol Pavlova shows how she washes makeup brushes: bar soap, technique by brush shape, oil for foundation and lipstick, and drying them right so they last for years.',
                   card='How I wash dozens of brushes a day: bar soap, circles or strokes by shape, oil for lipstick and drying flat. And why never bristles-up.'),
    },
    'catrice': {
        'date': '2026-10-28', 'img': 'nikol-portrait', 'video': 'lJGqeU8JfXA',
        'cs': dict(path='/blog/recenze-catrice-cely-oblicej/', crumb='Celý obličej Catrice', tag='Recenze',
                   title='Celý obličej Catrice: poctivá recenze vizážistky',
                   seo_title='Recenze Catrice: celý obličej a adventní kalendář | Nikol Pavlova',
                   desc='Vizážistka Nikol Pavlova z Prahy testuje celý obličej Catrice: make-up HD Liquid Coverage, bronzer Melted Sun, pečenou tvářenku, toppery, tužky a rty z adventního kalendáře.',
                   card='Celý obličej Catrice z adventního kalendáře: pečená tvářenka a topper nadchly, tužky na oči zklamaly a make-up dostal 6 z 10.'),
        'en': dict(path='/en/blog/full-face-of-catrice-review/', crumb='Full Face of Catrice', tag='Reviews',
                   title="Full Face of Catrice: A Makeup Artist's Honest Review",
                   seo_title="Full Face of Catrice: A Makeup Artist's Honest Review | Nikol Pavlova",
                   desc='Prague makeup artist Nikol Pavlova tests a full face of Catrice: HD Liquid Coverage foundation, Melted Sun bronzer, baked blush, glitter topper, pencils and lip products from the advent calendar.',
                   card='A full face of Catrice from the advent calendar: the baked blush and topper impressed, the eye pencils disappointed and the foundation scored 6/10.'),
    },
    'empties': {
        'date': '2026-10-22', 'img': 'nikol-header', 'video': 'pKt5euLMl9g',
        'cs': dict(path='/blog/dopotrebovana-kosmetika/', crumb='Dopotřebovaná kosmetika', tag='Recenze',
                   title='Dopotřebovaná kosmetika: co si koupím znovu a co už ne',
                   seo_title='Dopotřebovaná kosmetika: co si vizážistka koupí znovu | Nikol Pavlova',
                   desc='Vizážistka Nikol Pavlova z Prahy hodnotí 25 dopotřebovaných produktů: péče o pleť, SPF, vlasy, tělo i make-up. Co si koupí znovu a co už nikdy.',
                   card='Pětadvacet produktů, které jsem dopotřebovala do poslední kapky: péče, SPF, vlasy, tělo i make-up, a upřímně, co si koupím znovu.'),
        'en': dict(path='/en/blog/beauty-empties-repurchase/', crumb='Beauty empties', tag='Reviews',
                   title="Beauty Empties: What I'd Repurchase and What I Wouldn't",
                   seo_title="Beauty Empties: What a Makeup Artist Would Repurchase | Nikol Pavlova",
                   desc='Prague makeup artist Nikol Pavlova reviews 25 products she used up: skincare, SPF, hair, body and makeup, and says honestly what she would buy again.',
                   card="Twenty-five products I used up to the last drop: skincare, SPF, hair, body and makeup, and an honest verdict on what I'd buy again."),
    },
    'summer': {
        'date': '2026-10-21', 'img': 'nude-3', 'video': 'pg2rs7CB6lA',
        'cs': dict(path='/blog/letni-make-up-bez-make-upu/', crumb='Letní make-up bez make-upu', tag='Tutoriál',
                   title='Letní make-up bez make-upu: rutina vizážistky na horké dny',
                   seo_title='Letní make-up bez make-upu: rutina vizážistky | Nikol Pavlova',
                   desc='Vizážistka z Prahy ukazuje lehký letní make-up: péče s SPF, odstín make-upu pro pihovatou pleť, blur místo lesku, krémové barvy prsty a fixační spreje, které se vyplatí.',
                   card='Lehký letní make-up, který se nebojí horka: odstín pro pihovatou pleť, blur jen tam, kde je potřeba, a test fixačních sprejů.'),
        'en': dict(path='/en/blog/summer-no-makeup-makeup/', crumb='Summer no-makeup makeup', tag='Tutorial',
                   title="Summer No-Makeup Makeup: A Makeup Artist's Routine for Hot Days",
                   seo_title='Summer No-Makeup Makeup Routine | Nikol Pavlova, Prague MUA',
                   desc='Prague makeup artist Nikol Pavlova shares her light summer routine: SPF skin prep, matching foundation on freckled skin, blur instead of shine, cream colour with fingers and the setting sprays worth buying.',
                   card='A light summer face that copes with heat: foundation shades for freckled skin, blur only where you need it, and a setting spray test.'),
    },
    'nyx': {
        'date': '2026-03-20', 'img': 'nikol-hero', 'video': 'U89IYdxyJy4',
        'cs': dict(path='/blog/recenze-nyx-cely-oblicej/', crumb='Celý obličej NYX', tag='Recenze',
                   title='Celý obličej NYX: poctivá recenze vizážistky',
                   seo_title='Recenze NYX: celý obličej očima vizážistky | Nikol Pavlova',
                   desc='Vizážistka Nikol Pavlova z Prahy testuje celý obličej NYX: bázi, korektor, obočí, bronzer, oční stíny, linky, řasenku a fixační sprej, včetně celodenního testu výdrže.',
                   card='Otestovala jsem celý obličej NYX a nosila ho celý pracovní den: co si zasloužilo místo v mém kufru a co bych vynechala.'),
        'en': dict(path='/en/blog/full-face-of-nyx-review/', crumb='Full Face of NYX', tag='Reviews',
                   title="Full Face of NYX: A Makeup Artist's Honest Review",
                   seo_title="Full Face of NYX: A Makeup Artist's Honest Review | Nikol Pavlova",
                   desc='Prague makeup artist Nikol Pavlova tests a full face of NYX – primer, concealer, brows, bronzer, eyeshadow, liner, mascara and setting spray – with an honest all-day wear test.',
                   card='I tested a full face of NYX and wore it through a working day: what earned a place in my kit and what I would skip.'),
    },
}
ORDER = ['blush', 'travel', 'brushes', 'catrice', 'empties', 'summer', 'nyx']   # newest first

MONTHS = {
    'cs': ['ledna', 'února', 'března', 'dubna', 'května', 'června', 'července', 'srpna', 'září', 'října', 'listopadu', 'prosince'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
}


def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split('-'))
    mn = MONTHS[lang][m - 1]
    return f'{d}. {mn} {y}' if lang == 'cs' else f'{d} {mn} {y}'


def cards(lang, keys):
    """Blog teaser on service pages: blog cover + article title only."""
    out = ''
    for k in keys:
        m = POSTS[k][lang]
        out += (f'<li><article><a class="bl-card bl-card--teaser" href="{m["path"]}">'
                f'{cover(k, lang, "(max-width: 900px) 100vw, 33vw")}<h3>{m["title"]}</h3></a></article></li>')
    return f'<ul class="cards3" role="list">{out}</ul>'


def teaser(lang, keys, title=None, sub=None, hid='blog-h'):
    """Related articles block for service and article pages."""
    if not keys:
        return ''
    title = title or ('Z blogu' if lang == 'cs' else 'From the blog')
    sub = sub or ('tipy k tomuto tématu' if lang == 'cs' else 'tips on this topic')
    allp = ('/blog/', 'Všechny články →') if lang == 'cs' else ('/en/blog/', 'All articles →')
    return f'''<section class="sec--tight" aria-labelledby="{hid}"><div class="wrap">
<div class="tz-head"><div><p class="tz-label">({sub})</p><h2 class="tz-h2" id="{hid}">{title.split(' ', 1)[0]} <em>{title.split(' ', 1)[1] if ' ' in title else ''}</em></h2></div><a class="tz-link" href="{allp[0]}">{allp[1]}</a></div>
{cards(lang, keys)}
</div></section>
'''


# ---------------------------------------------------------------- blog covers (tinted photo + glass card)
# kind: 'panel' (wide card with bar and two stats) or 'pill' (tall card); texts per language, facts from the articles only
COVERS = {
    'blush': dict(tint='#C8701E', ratio='10/9', kind='panel', pct=64,
                  cs=dict(k='Tvářenka', sub='korektor → tvářenka', big='Přechod', s1='Umístění', v1='podle tvaru tváře', s2='Nová kolekce', v2='netřeba'),
                  en=dict(k='Blush', sub='concealer → blush', big='Blend', s1='Placement', v1='by face shape', s2='New kit', v2='not needed')),
    'travel': dict(tint='#14244F', ratio='4/5', kind='pill', glow='#3B7BFF',
                   cs=dict(k='kosmetička<br>na cesty', big='5 štětců', sub='den · večer'),
                   en=dict(k='travel<br>makeup bag', big='5 brushes', sub='day · night')),
    'brushes': dict(tint='#D9708F', ratio='1/1', kind='panel', pct=82,
                    cs=dict(k='Mytí štětců', sub='sušení', big='Naplocho', s1='Mýdlo', v1='tuhé', s2='Na rtěnku', v2='olej'),
                    en=dict(k='Brush care', sub='drying', big='Flat', s1='Soap', v1='bar', s2='For lipstick', v2='oil')),
    'catrice': dict(tint='#C9473F', ratio='3/4', kind='pill', glow='#FF8A7A',
                    cs=dict(k='Recenze<br>Catrice', big='6 / 10', sub='make-up'),
                    en=dict(k='Catrice<br>review', big='6 / 10', sub='foundation')),
    'empties': dict(tint='#2F5FA8', ratio='4/5', kind='panel', pct=100,
                    cs=dict(k='Dopotřebováno', sub='do poslední kapky', big='25', s1='Péče · SPF', v1='vlasy · tělo', s2='Make-up', v2='znovu / ne'),
                    en=dict(k='Used up', sub='to the last drop', big='25', s1='Skin · SPF', v1='hair · body', s2='Makeup', v2='again / no')),
    'summer': dict(tint='#D98A55', ratio='4/5', kind='pill', glow='#FFD2A6',
                   cs=dict(k='letní rutina', big='Bez<br>make-upu', sub='odolá horku'),
                   en=dict(k='summer routine', big='No-makeup<br>makeup', sub='heat-proof')),
    'nyx': dict(tint='#5E2A5C', ratio='1/1', kind='panel', pct=50,
                cs=dict(k='Celý obličej NYX', sub='jeden pracovní den', big='1 den', s1='Do kufru', v1='ano', s2='Vynechat', v2='v článku'),
                en=dict(k='Full face NYX', sub='one working day', big='1 day', s1='In my kit', v1='yes', s2='Skip', v2='see article')),
}


def cover(key, lang, sizes, big=False, priority=False):
    """Tinted, blurred photo with a glass card. Decorative: the card text repeats facts from the title/excerpt."""
    cv, p = COVERS[key], POSTS[key]
    t = cv[lang]
    pic = img(p['img'], '', sizes=sizes, cls='cv-img', priority=priority)
    ghost = img(p['img'], '', sizes=sizes, cls='cv-ghost')
    if cv['kind'] == 'panel':
        card = (f'<span class="cv-panel"><span class="cv-top"><span class="cv-k"><b>{t["k"]}</b><small>{t["sub"]}</small></span><span class="cv-big">{t["big"]}</span></span>'
                f'<span class="cv-bar"><i></i></span>'
                f'<span class="cv-stats"><span><small>{t["s1"]}</small><b>{t["v1"]}</b></span><span><small>{t["s2"]}</small><b>{t["v2"]}</b></span></span></span>')
    else:
        card = f'<span class="cv-pill"><small>{t["k"]}</small><b>{t["big"]}</b><small>{t["sub"]}</small></span>'
    return (f'<span class="bcover cv--{key}{" bcover--big" if big else ""}">{pic}{ghost}'
            f'<span class="cv-wash" aria-hidden="true"></span><span class="cv-glass" aria-hidden="true">{card}</span></span>')


def bl_grid(lang, keys, excerpt=True):
    out = ''
    for k in keys:
        p, m = POSTS[k], POSTS[k][lang]
        ex = f'<p class="bl-ex">{m["card"]}</p>' if excerpt else ''
        out += (f'<li><article><a class="bl-card" href="{m["path"]}">{cover(k, lang, "(max-width: 700px) 100vw, (max-width: 1200px) 50vw, 25vw")}'
                f'<p class="bl-meta">{m["tag"]} • <time datetime="{p["date"]}">{fmt_date(lang, p["date"])}</time></p>'
                f'<h3>{m["title"]}</h3>{ex}</a></article></li>')
    return f'<ul class="bl-grid" role="list">{out}</ul>'
