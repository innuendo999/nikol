"""Blog post registry (both languages) and the "From the blog" block used on service pages."""
from lib import img, sec_head

POSTS = {
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
ORDER = ['empties', 'summer', 'nyx']   # newest first

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
