"""About page (/o-mne/, /en/about/): full-bleed hero, story, services, how I work, moving gallery.
Styles live in src/site.css under "about page"."""
from lib import *
from lib import img as I
import schema as S
from pages_blog import BL_FONTS

PATHS = {'cs': '/o-mne/', 'en': '/en/about/'}

T = {
    'cs': dict(
        title='O mně – Nikol Pavlova, vizážistka v Praze',
        desc='Jsem Nikol Pavlova, vizážistka v Praze od roku 2021. Svatební, večerní a komerční líčení a individuální kurzy. Líčím česky, anglicky i ukrajinsky.',
        crumb='O mně', h1=('Jsem', 'Nikol'), hero_sub='Vizážistka v Praze.<br>Svatby, večery, editorial a kurzy.',
        strip=['5,0 ★ na Googlu', 'Praha 8 – Karlín', 'Česky · English · Українська', 'Svatby · Editorial · Kurzy', 'Nové video na YouTube každý týden'],
        story_h=('Můj', 'příběh'), story_meta='(Praha, od roku 2021)',
        story=['V Praze žiju od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy.',
               'Můj styl spojuje precizní techniku, kreativitu a cit pro barvy i textury. Ať chceš jemný svatební vzhled, odvážný večerní make-up nebo editoriální look, baví mě proměnit tvou vizi ve skutečnost.',
               'Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.'],
        do_h=('Co', 'dělám'),
        cards=[('Svatby', 'Dlouhotrvající &amp; zářivé', '/svatebni-liceni/'),
               ('Večer &amp; plesy', 'Plesy a večírky · od 2 500 Kč', '/vecerni-liceni/'),
               ('Editorial &amp; komerce', 'Focení a reklama', '/komercni-liceni/'),
               ('Kurzy 1 na 1', 'Naučte se líčit jako profík', '/kurzy-liceni/')],
        how_h=('Jak', 'pracuju'),
        how=['Líčení, ve kterém se cítíš <em>jako ty</em> — jen ve své nejlepší verzi.',
             'Nejdřív se ptám, jak se chceš cítit a co tě čeká. Pak ladím look podle tvé pleti a tvaru obličeje, v klidu a bez spěchu.',
             'Klientky v recenzích nejčastěji zmiňují klidnou atmosféru a make-up, který vydrží celý den. Líčím česky, anglicky i ukrajinsky.'],
        book='Rezervovat termín +', portfolio='Portfolio',
        cta=('Kontaktujte mě', 'Potřebujete pomoc s líčením?', 'Profesionální vizážistka v Praze.')),
    'en': dict(
        title='About – Nikol Pavlova, makeup artist in Prague',
        desc='I am Nikol Pavlova, a makeup artist based in Prague since 2021. Bridal, evening and commercial makeup and one-on-one courses, in English, Czech and Ukrainian.',
        crumb='About', h1=('I’m', 'Nikol'), hero_sub='Makeup artist in Prague.<br>Weddings, evenings, editorial and courses.',
        strip=['5.0 ★ on Google', 'Prague 8 – Karlín', 'English · Česky · Українська', 'Weddings · Editorial · Courses', 'New YouTube video every week'],
        story_h=('My', 'story'), story_meta='(Prague, since 2021)',
        story=['I have lived in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses.',
               'My style combines precise technique, creativity and a feel for colour and texture. Whether you want a soft bridal look, a bold evening face or an editorial idea, I love turning your vision into reality.',
               'Every week on YouTube I show how I do makeup and which products I genuinely use.'],
        do_h=('What', 'I do'),
        cards=[('Weddings', 'Long-lasting &amp; radiant', '/en/wedding/'),
               ('Evenings &amp; balls', 'Balls and parties · from CZK 2,500', '/en/evening-makeup/'),
               ('Editorial &amp; commercial', 'Shoots and campaigns', '/en/commercial-makeup/'),
               ('1:1 courses', 'Learn to do it like a pro', '/en/courses/')],
        how_h=('How', 'I work'),
        how=['Makeup in which you feel <em>like yourself</em> — just the best version.',
             'First I ask how you want to feel and what your day looks like. Then I tune the look to your skin and face shape, calmly and without rushing.',
             'In their reviews clients most often mention the calm atmosphere and makeup that lasts all day. I work in English, Czech and Ukrainian.'],
        book='Book online +', portfolio='Portfolio',
        cta=('Contact me', 'Do you need help with creative make-up?', 'Professional makeup artist based in Prague.')),
}

# (image, crop class, colour class) — photos from the home page hero for now
CARD_IMG = [('nikol-hero', 'ab-pos-a', 'ab-gel--1'), ('nikol-portrait', 'ab-pos-b', 'ab-gel--2'),
            ('nikol-header', 'ab-pos-c', 'ab-gel--3'), ('nikol-hero', 'ab-pos-d', 'ab-gel--4')]
GALLERY = [('nikol-hero', 'ab-pos-a', 1), ('nikol-portrait', 'ab-pos-b', 2), ('nikol-header', 'ab-pos-c', 3), ('nikol-hero', 'ab-pos-d', 4),
           ('nikol-portrait', 'ab-pos-c', 5), ('nikol-header', 'ab-pos-b', 6), ('nikol-hero', 'ab-pos-a', 7), ('nikol-portrait', 'ab-pos-b', 8)]


def build_lang(lang):
    t, L_ = T[lang], L[lang]
    path = PATHS[lang]
    other = PATHS['en' if lang == 'cs' else 'cs']
    url = SITE + path
    graph = [{'@type': 'AboutPage', '@id': url + '#webpage', 'url': url, 'name': t['title'], 'description': t['desc'], 'inLanguage': lang,
              'isPartOf': {'@id': SITE + '/#website'}, 'mainEntity': {'@id': SITE + '/#person'}, 'about': {'@id': SITE + '/#person'},
              'breadcrumb': {'@id': url + '#breadcrumb'}, 'primaryImageOfPage': SITE + '/assets/img/nikol-hero-1280.webp'},
             S.person(lang), S.business_ref(lang),
             S.breadcrumb(path, [(L_['home'], L_['home_href']), (t['crumb'], path)])]
    alt = [('cs', PATHS['cs']), ('en', PATHS['en']), ('x-default', PATHS['cs'])]
    h = head(lang, t['title'], t['desc'], path, alt, '', [{'@context': 'https://schema.org', '@graph': graph}],
             preload('nikol-hero', '100vw') + '\n' + BL_FONTS)
    h += header(lang, 'about', other)
    strip = ''.join(f'<span>{x}</span><span class="ab-dot" aria-hidden="true">✦</span>' for x in t['strip'])
    story = (f'<p class="ab-big ab-rv">{t["story"][0]}</p>' + ''.join(f'<p class="ab-muted ab-rv">{x}</p>' for x in t['story'][1:]))
    cards = ''.join(f'<li><a class="ab-card" href="{u}"><span class="ab-ph">{I(im, "", sizes="(max-width: 700px) 100vw, 25vw", cls=pos)}'
                    f'<span class="ab-gel {gel}" aria-hidden="true"></span><span class="ab-shine" aria-hidden="true"></span></span>'
                    f'<span class="ab-card-t"><b>{n}</b><small>{d}</small></span></a></li>'
                    for (n, d, u), (im, pos, gel) in zip(t['cards'], CARD_IMG))
    tiles = ''.join(f'<span class="ab-tile ab-tile--{k}">{I(im, "", sizes="240px", cls=pos)}<span class="ab-tgel" aria-hidden="true"></span></span>'
                    for im, pos, k in GALLERY)
    how = f'<p class="ab-big ab-rv">{t["how"][0]}</p>' + ''.join(f'<p class="ab-muted ab-rv">{x}</p>' for x in t['how'][1:])
    w1, w2 = t['h1']
    h += f'''<div class="ab">
<section class="ab-hero" aria-labelledby="page-h1">
{I('nikol-hero', 'Nikol Pavlova', sizes='100vw', cls='ab-hero-img', priority=True)}
<span class="ab-hero-gel" aria-hidden="true"></span><span class="ab-rays" aria-hidden="true"></span><span class="ab-hero-shade" aria-hidden="true"></span>
<div class="wrap ab-hero-txt">
<h1 class="ab-h1" id="page-h1"><span class="ab-word">{w1}</span> <span class="ab-word ab-d2">{w2}</span><span class="ab-word ab-d3 ab-dotc">.</span></h1>
<p class="ab-word ab-d4 ab-hero-sub">{t['hero_sub']}</p>
</div>
</section>
<div class="ab-strip" aria-label="{t['crumb']}"><div class="ab-mq">{strip}<span class="ab-dup" aria-hidden="true">{strip}</span></div></div>
<section class="wrap ab-story" aria-labelledby="story-h">
<div class="ab-story-l"><h2 class="ab-h2 ab-rv" id="story-h">{t['story_h'][0]} <em>{t['story_h'][1]}</em></h2><p class="ab-meta">{t['story_meta']}</p></div>
<div class="ab-story-r">{story}</div>
</section>
<section class="ab-do" aria-labelledby="do-h">
<h2 class="wrap ab-h2 ab-rv" id="do-h">{t['do_h'][0]} <em>{t['do_h'][1]}</em></h2>
<ul class="ab-cards" role="list">{cards}</ul>
</section>
<section class="wrap ab-how" aria-labelledby="how-h">
<div class="ab-how-txt">{how}</div>
<h2 class="ab-h2 ab-h2--s ab-rv" id="how-h">{t['how_h'][0]} <em>{t['how_h'][1]}</em></h2>
</section>
<div class="ab-gallery" aria-hidden="true"><div class="ab-mq ab-mq--slow">{tiles}{tiles}</div></div>
<section class="wrap ab-end">
<a class="btn btn--pink" href="{CAL}">{t['book']}</a>
<a class="ab-biglink" href="{L_['portfolio_href']}">{t['portfolio']} <span aria-hidden="true">→</span></a>
</section>
</div>
'''
    h += footer(lang, *t['cta'])
    write(path, h)


def build():
    for lang in ('cs', 'en'):
        build_lang(lang)
