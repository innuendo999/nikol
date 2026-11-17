"""Blog post registry (both languages) and the "From the blog" block used on service pages."""
from lib import img, sec_head

POSTS = {
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
ORDER = ['travel', 'brushes', 'catrice', 'empties', 'summer', 'nyx']   # newest first

MONTHS = {
    'cs': ['ledna', 'února', 'března', 'dubna', 'května', 'června', 'července', 'srpna', 'září', 'října', 'listopadu', 'prosince'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
}


def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split('-'))
    mn = MONTHS[lang][m - 1]
    return f'{d}. {mn} {y}' if lang == 'cs' else f'{d} {mn} {y}'


def cards(lang, keys):
    out = ''
    for k in keys:
        p, m = POSTS[k], POSTS[k][lang]
        out += (f'<li><article><a class="pcard" href="{m["path"]}"><div class="ph">{img(p["img"], m["title"], sizes="(max-width: 900px) 100vw, 33vw")}'
                f'<span class="tag lbl glass">{m["tag"]}</span></div><div class="row"><h3>{m["title"]}</h3></div>'
                f'<p class="body"><time datetime="{p["date"]}">{fmt_date(lang, p["date"])}</time> · {m["card"]}</p></a></article></li>')
    return f'<ul class="cards3" role="list">{out}</ul>'


def teaser(lang, keys, title=None, sub=None, hid='blog-h'):
    """Related articles block for service and article pages."""
    if not keys:
        return ''
    title = title or ('Z blogu' if lang == 'cs' else 'From the blog')
    sub = sub or ('tipy k tomuto tématu' if lang == 'cs' else 'tips on this topic')
    allp = ('/blog/', 'Všechny články →') if lang == 'cs' else ('/en/blog/', 'All articles →')
    return f'''<section class="sec--tight" aria-labelledby="{hid}"><div class="wrap">
{sec_head(title, sub, f'<a class="link-arrow" href="{allp[0]}">{allp[1]}</a>', hid=hid)}
{cards(lang, keys)}
</div></section>
'''
