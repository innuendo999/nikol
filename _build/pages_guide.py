"""Paid PDF guide: sales pages (CZ, EN, UA).

How the sale works: the "Buy" buttons open a Stripe Payment Link (stripe_link below).
Payment and delivery of the PDF are handled entirely in Stripe (the Payment Link's
after-payment settings), so the site has no thank-you or download page.

Until stripe_link and price are filled in, a page is built with noindex,
left out of the sitemap and the build prints a warning.
"""
from lib import *
from lib import img as I
from ui26 import hero_svc, strip, intro2, features2, pricing2, steps2

# ---------------------------------------------------------------- settings (fill in before launch)
GUIDE = {
    'cs': dict(path='/pruvodce-stetci/',
               stripe_link='https://buy.stripe.com/5kQ9AVfrYaGr27uaFp2Nq03',
               price='499 Kč', price_num=499, currency='CZK'),
    'en': dict(path='/en/brush-guide/',
               stripe_link='https://buy.stripe.com/6oU4gB4Nk4i36nKaFp2Nq02',
               price='€19', price_num=19, currency='EUR'),
    'uk': dict(path='/uk/gaid-penzlyky/',
               stripe_link='https://buy.stripe.com/bJe5kF93A8yj6nK00L2Nq01',
               price='699 грн', price_num=699, currency='UAH'),
}
LANGS = ('cs', 'en', 'uk')
OTHER = {'cs': 'en', 'en': 'cs', 'uk': 'cs'}   # target of the header language switch


def ready(lang):
    g = GUIDE[lang]
    return bool(g['stripe_link'] and g['price'])


def all_ready():
    return all(ready(l) for l in LANGS)


# ---------------------------------------------------------------- copy (taken from the guide itself)
T = {
    'cs': dict(
        title='Průvodce štětci na líčení (PDF) | Nikol Pavlova',
        desc='Průvodce štětci od vizážistky Nikol Pavlové: jaký štětec na co, jakým pohybem s ním pracovat a jak o něj pečovat. 23 stran PDF, 10 kapitol, 2 neveřejná videa a odkazy na všechny štětce.',
        crumbs=[('Domů', '/'), ('Blog', '/blog/'), ('Průvodce štětci', None)],
        big='Průvodce štětci', sub='na líčení – co vybrat, jak s nimi pracovat a jak o ně pečovat',
        lead='Průvodce štětci, se kterými sama pracuji: k čemu který slouží, jakým pohybem ho používat, moje tipy ke každému a jak štětce mýt, aby vydržely. PDF ke stažení hned po zaplacení.',
        buy='Koupit průvodce', buy_soon='Prodej brzy spustíme',
        hero_alt=('Průvodce štětci na líčení – obálka PDF', 'Nikol Pavlova při lekci líčení'),
        marquee=['23 stran PDF', '10 kapitol', 'Karty štětců', 'Slovníček pohybů', 'Mytí štětců', '2 neveřejná videa', 'Odkazy na štětce'],
        intro_label='O průvodci', intro_title='Jaký štětec na co a jak s ním pracovat',
        intro_tag='seznam štětců není povinný – hlavní je pochopit, jaký tvar potřebujete',
        intro_body='Jsem Ukrajinka a žiju v Praze, krása byla vždycky mým koníčkem a dnes je mojí prací. Do průvodce jsem dala štětce, které opravdu používám: na make-up a korektor, pudr a tvářenku, oči, obočí i rty. U každého najdete, <b>k čemu slouží</b>, <b>jakým pohybem s ním pracovat</b> a <b>můj tip</b>. Nemusíte kupovat stejné značky – průvodce vás naučí poznat, jaký tvar a vlas štětce potřebujete.',
        chips=['Přírodní vlas, nebo syntetika', 'Karty štětců s technikou a tipem', 'Moje základní sada 7 štětců', 'Alternativy k zakoupení v Česku'],
        feat_title='Co v průvodci |najdete', feat_sub='10 kapitol, 23 stran',
        feats=[('Vlas a pohyby', 'Přírodní vlas, nebo syntetika, druhy vlasu a slovníček pohybů: vtlačovat, roztírat, rozmazávat, táhnout.'),
               ('Karty štětců', 'Make-up a korektor, pudr a tvářenka, oči, obočí a rty: k čemu, technika a můj tip ke každému štětci.'),
               ('Péče a základní sada', 'Jak štětce mýt šetrně, čemu se vyhnout a sedm štětců, kterými je dobré začít.'),
               ('Videa a odkazy', 'Dvě neveřejná videa – jak myju štětce a jak pracuji s každým z nich – a odkazy, kde štětce koupit.')],
        feat_alts=['Obsah průvodce štětci', 'Karty štětců na make-up a korektor', 'Mytí štětců na líčení', 'Videa k průvodci štětci'],
        toc_label='Obsah', toc_title='Kapitoly průvodce',
        toc=[('Vlas: přírodní, nebo syntetika', '03'), ('Slovníček pohybů', '04'), ('Make-up a korektor', '05'),
             ('Pudr, tvářenka, bronzer, rozjasňovač', '08'), ('Oči: stíny, rozmazání, linky', '12'), ('Obočí a rty', '17'),
             ('Péče a mytí štětců', '19'), ('Moje základní sada', '20'), ('Videa k průvodci', '21'), ('Odkazy na štětce', '22')],
        price_label='Cena', price_title='Průvodce |štětci', price_note='Platba kartou přes Stripe. Odkaz ke stažení dostanete hned po zaplacení.',
        price_col='Průvodce štětci (PDF)', price_items=['23 stran, 10 kapitol', 'Karty štětců s technikou a tipy', 'Moje základní sada 7 štětců', '2 neveřejná videa', 'Odkazy na všechny štětce', 'Česky'],
        price_tbd='Cena brzy',
        steps_title='Jak to |funguje', steps_sub='nákup a stažení', steps=[
            ('Zaplaťte přes Stripe', 'Tlačítko vás přenese na zabezpečenou platební stránku Stripe.'),
            ('Dostanete odkaz ke stažení', 'Hned po zaplacení vám Stripe ukáže odkaz ke stažení PDF.'),
            ('Uložte si PDF', 'Průvodce si uložte do telefonu nebo počítače – otevřete ho kdykoli i bez internetu.'),
            ('Pusťte si videa', 'Videa otevřete přes tlačítka přímo v PDF. Jsou neveřejná, prosím, nepřeposílejte je.')],
        faq_title='Dotazy k průvodci', faq=[
            ('V jakém formátu průvodce je?', 'Je to PDF o 23 stranách. Otevřete ho v telefonu, tabletu i počítači.'),
            ('Jak průvodce dostanu?', 'Hned po zaplacení vám Stripe ukáže odkaz ke stažení PDF.'),
            ('Musím si koupit stejné štětce?', 'Ne. Seznam štětců není povinný – průvodce vás naučí, jaký tvar a vlas štětce potřebujete. Na konci jsou i alternativy k zakoupení v Česku (Notino, Douglas).'),
            ('Je průvodce i v jiných jazycích?', 'Ano: anglicky – <a href="/en/brush-guide/">Makeup brush guide</a>, ukrajinsky – <a href="/uk/gaid-penzlyky/">Гайд по пензликах</a>.'),
            ('Stažení nefunguje, co teď?', f'Napište mi na <a href="mailto:{MAIL}">{MAIL}</a> e-mail, který jste zadali při platbě, a průvodce vám pošlu.')],
        foot=('Máte dotaz k průvodci?', 'Kontaktujte mě', 'Napište mi, ráda poradím, jestli je průvodce pro vás.'),
    ),
    'en': dict(
        title='Makeup Brush Guide (PDF) | Nikol Pavlova, Prague MUA',
        desc='A makeup brush guide by Prague makeup artist Nikol Pavlova: which brush for what, which movement to use and how to care for it. 23-page PDF, 10 chapters, 2 private videos and links to every brush.',
        crumbs=[('Home', '/en/'), ('Blog', '/en/blog/'), ('Brush guide', None)],
        big='Brush guide', sub='for makeup – what to choose, how to use them and how to care for them',
        lead='A guide to the brushes I actually work with: what each one is for, which movement to use, my tip for every brush and how to wash them so they last. Download the PDF right after payment.',
        buy='Buy the guide', buy_soon='Coming soon',
        hero_alt=('Makeup brush guide – PDF cover', 'Nikol Pavlova during a makeup lesson'),
        marquee=['23-page PDF', '10 chapters', 'Brush cards', 'Movement glossary', 'Brush care', '2 private videos', 'Brush links'],
        intro_label='About the guide', intro_title='Which brush for what, and how to use it',
        intro_tag='the brush list isn’t mandatory – what matters is knowing which shape you need',
        intro_body='I’m Ukrainian and I live in Prague; beauty was always my hobby and today it’s my work. In this guide I put the brushes I really use: for foundation and concealer, powder and blush, eyes, brows and lips. For each one you’ll find <b>what it’s for</b>, <b>which movement to use</b> and <b>my tip</b>. You don’t need the same brands – the guide teaches you to recognise the brush shape and bristle you need.',
        chips=['Natural or synthetic bristles', 'Brush cards with technique and a tip', 'My basic kit of 7 brushes', 'Alternatives available in Czechia'],
        feat_title='What’s |inside', feat_sub='10 chapters, 23 pages',
        feats=[('Bristles and movements', 'Natural or synthetic, bristle types and a movement glossary: tap, spread, buff, blend, drag.'),
               ('Brush cards', 'Foundation and concealer, powder and blush, eyes, brows and lips: what for, technique and my tip for every brush.'),
               ('Care and basic kit', 'How to wash brushes gently, what to avoid, and the seven brushes to start with.'),
               ('Videos and links', 'Two private videos – how I wash my brushes and how I use each one – plus links to where to buy them.')],
        feat_alts=['Brush guide contents', 'Brush cards for foundation and concealer', 'Washing makeup brushes', 'Videos for the brush guide'],
        toc_label='Contents', toc_title='Chapters in the guide',
        toc=[('Bristles: natural or synthetic', '03'), ('Movement glossary', '04'), ('Foundation and concealer', '05'),
             ('Powder, blush, contour, highlighter', '08'), ('Eyes: shadow, blending, liner', '12'), ('Brows and lips', '17'),
             ('Caring for and washing brushes', '19'), ('My basic kit', '20'), ('Videos for the guide', '21'), ('Brush links', '22')],
        price_label='Price', price_title='Brush |guide', price_note='Card payment via Stripe. You get the download link right after payment.',
        price_col='Makeup brush guide (PDF)', price_items=['23 pages, 10 chapters', 'Brush cards with technique and tips', 'My basic kit of 7 brushes', '2 private videos', 'Links to every brush', 'In English'],
        price_tbd='Price soon',
        steps_title='How it |works', steps_sub='buying and download', steps=[
            ('Pay via Stripe', 'The button takes you to Stripe’s secure checkout.'),
            ('Get the download link', 'Right after payment Stripe shows you the link to download the PDF.'),
            ('Save the PDF', 'Save the guide to your phone or computer – open it any time, even offline.'),
            ('Watch the videos', 'Open the videos with the buttons inside the PDF. They are private, so please don’t share them.')],
        faq_title='Questions about the guide', faq=[
            ('What format is the guide?', 'It’s a 23-page PDF. It opens on a phone, tablet or computer.'),
            ('How do I get the guide?', 'Right after payment Stripe shows you the link to download the PDF.'),
            ('Do I need to buy the same brushes?', 'No. The brush list isn’t mandatory – the guide teaches you which brush shape and bristle you need. At the end there are also alternatives you can buy in Czechia (Notino, Douglas).'),
            ('Is the guide available in other languages?', 'Yes: in Czech – <a href="/pruvodce-stetci/">Průvodce štětci</a>, and in Ukrainian – <a href="/uk/gaid-penzlyky/">Гайд по пензликах</a>.'),
            ('The download doesn’t work – what now?', f'Email me at <a href="mailto:{MAIL}">{MAIL}</a> from the address you used at checkout and I’ll send you the guide.')],
        foot=('Questions about the guide?', 'Get in touch', 'Message me and I’ll help you decide whether the guide is right for you.'),
    ),
    'uk': dict(
        title='Гайд по пензликах для макіяжу (PDF) | Nikol Pavlova',
        desc='Гайд по пензликах від візажистки Ніколь Павлової: який пензлик для чого, яким рухом працювати і як доглядати. PDF на 23 сторінки, 10 розділів, 2 закриті відео і посилання на всі пензлики.',
        crumbs=[('Головна', '/'), ('Гайд по пензликах', None)],
        big='Гайд по пензликах', sub='для макіяжу – що обрати, як працювати і як доглядати',
        lead='Гайд по пензликах, з якими я сама працюю: для чого кожен, яким рухом ним працювати, мої поради до кожного і як мити пензлики, щоб вони служили довше. PDF можна завантажити одразу після оплати.',
        buy='Купити гайд', buy_soon='Скоро у продажу',
        hero_alt=('Гайд по пензликах для макіяжу – обкладинка PDF', 'Ніколь Павлова на уроці макіяжу'),
        marquee=['PDF на 23 сторінки', '10 розділів', 'Картки пензликів', 'Словничок рухів', 'Миття пензликів', '2 закриті відео', 'Посилання на пензлики'],
        intro_label='Про гайд', intro_title='Який пензлик для чого і як ним працювати',
        intro_tag='список пензликів не обов’язковий – головне розуміти, яка форма тобі потрібна',
        intro_body='Я українка, живу в Празі; краса завжди була моїм хобі, а тепер це моя робота. У гайд я зібрала пензлики, якими справді користуюся: для тону й коректора, пудри й рум’ян, очей, брів і губ. Для кожного ти знайдеш, <b>для чого він</b>, <b>яким рухом ним працювати</b> і <b>мою пораду</b>. Не обов’язково купувати ті самі бренди – гайд навчить розуміти, яка форма й ворс пензлика тобі потрібні.',
        chips=['Натуральний ворс чи синтетика', 'Картки пензликів з технікою й порадою', 'Мій базовий набір із 7 пензликів', 'Альтернативи, які можна купити в Чехії'],
        feat_title='Що в |гайді', feat_sub='10 розділів, 23 сторінки',
        feats=[('Ворс і рухи', 'Натуральний ворс чи синтетика, види ворсу і словничок рухів: набивати, розтягувати, шліфувати, відтушовувати, тягнути.'),
               ('Картки пензликів', 'Тон і коректор, пудра й рум’яна, очі, брови й губи: для чого, техніка і моя порада до кожного пензлика.'),
               ('Догляд і базовий набір', 'Як дбайливо мити пензлики, чого уникати, і сім пензликів, з яких варто почати.'),
               ('Відео й посилання', 'Два закриті відео – як я мию пензлики і як працюю кожним із них – і посилання, де їх купити.')],
        feat_alts=['Зміст гайду по пензликах', 'Картки пензликів для тону й коректора', 'Миття пензликів для макіяжу', 'Відео до гайду по пензликах'],
        toc_label='Зміст', toc_title='Розділи гайду',
        toc=[('Ворс: натуральний чи синтетика', '03'), ('Словничок рухів', '04'), ('Тон і коректор', '05'),
             ('Пудра, рум’яна, скульптор, хайлайтер', '08'), ('Очі: тіні, розтушовка, підводка', '12'), ('Брови і губи', '17'),
             ('Догляд і миття пензликів', '19'), ('Мій базовий набір', '20'), ('Відео до гайду', '21'), ('Посилання на пензлики', '22')],
        price_label='Ціна', price_title='Гайд по |пензликах', price_note='Оплата карткою через Stripe. Посилання на завантаження – одразу після оплати.',
        price_col='Гайд по пензликах (PDF)', price_items=['23 сторінки, 10 розділів', 'Картки пензликів з технікою й порадами', 'Мій базовий набір із 7 пензликів', '2 закриті відео', 'Посилання на всі пензлики', 'Українською'],
        price_tbd='Ціна скоро',
        steps_title='Як це |працює', steps_sub='покупка і завантаження', steps=[
            ('Оплати через Stripe', 'Кнопка відкриє захищену сторінку оплати Stripe.'),
            ('Отримай посилання', 'Одразу після оплати Stripe покаже посилання для завантаження PDF.'),
            ('Збережи PDF', 'Збережи гайд у телефон чи комп’ютер – відкривай будь-коли, навіть без інтернету.'),
            ('Дивись відео', 'Відео відкриваються кнопками прямо в PDF. Вони закриті, тож, будь ласка, не пересилай їх.')],
        faq_title='Запитання про гайд', faq=[
            ('У якому форматі гайд?', 'Це PDF на 23 сторінки. Він відкривається на телефоні, планшеті й комп’ютері.'),
            ('Як я отримаю гайд?', 'Одразу після оплати Stripe покаже посилання для завантаження PDF.'),
            ('Чи треба купувати ті самі пензлики?', 'Ні. Список пензликів не обов’язковий – гайд навчить розуміти, яка форма й ворс тобі потрібні. Посилання ведуть переважно в українські магазини, а в кінці є альтернативи, які можна купити в Чехії (Notino, Douglas).'),
            ('Чи є гайд іншими мовами?', 'Так: чеською – <a href="/pruvodce-stetci/">Průvodce štětci</a>, англійською – <a href="/en/brush-guide/">Makeup brush guide</a>.'),
            ('Завантаження не працює, що робити?', f'Напиши мені на <a href="mailto:{MAIL}">{MAIL}</a> з адреси, яку вказала під час оплати, і я надішлю гайд.')],
        foot=('Є запитання про гайд?', 'Напиши мені', 'Напиши – підкажу, чи підійде тобі гайд.'),
    ),
}

FEAT_IMGS = {'uk': ['guide-uk-p02', 'guide-uk-p06', 'brushes-hero', 'guide-uk-p21'],
             'cs': ['guide-cs-p02', 'guide-cs-p06', 'brushes-hero', 'guide-cs-p21'],
             'en': ['guide-en-p02', 'guide-en-p06', 'brushes-hero', 'guide-en-p21']}


def _noindex(h, path):
    h = h.replace('content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"', 'content="noindex, nofollow"')
    return h.replace(f'<link rel="canonical" href="{SITE}{path}">\n', '')


def _schema(lang, t, g):
    url = SITE + g['path']
    prod = {'@type': 'Product', '@id': url + '#product', 'name': t['price_col'], 'description': t['desc'],
            'image': SITE + f"/assets/img/guide-{lang}-p01-800.webp", 'brand': {'@type': 'Brand', 'name': 'Nikol Pavlova'},
            'inLanguage': lang}
    if g['price_num'] is not None:
        prod['offers'] = {'@type': 'Offer', 'price': str(g['price_num']), 'priceCurrency': g['currency'],
                          'availability': 'https://schema.org/InStock', 'url': url}
    import schema as S
    graph = [{'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': t['title'], 'description': t['desc'],
              'inLanguage': lang, 'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': url + '#product'}},
             prod, S.faq(g['path'], lang, t['faq'])]
    return [{'@context': 'https://schema.org', '@graph': graph}]


def sales(lang):
    t, g, other = T[lang], GUIDE[lang], GUIDE[OTHER[lang]]
    path, ok = g['path'], ready(lang)
    buy_href = g['stripe_link'] if ok else '#packages'
    buy_label = f"{t['buy']} – {g['price']} +" if ok else t['buy_soon']
    alts = [(l, GUIDE[l]['path']) for l in LANGS] + [('x-default', GUIDE['cs']['path'])] if all_ready() else []
    h = head(lang, t['title'], t['desc'], path, alts, SITE + f'/assets/img/guide-{lang}-p01-800.webp', _schema(lang, t, g),
             preload(f'guide-{lang}-p01', '(max-width: 900px) 60vw, 30vw'))
    if not ok:
        h = _noindex(h, path)
    h += header(lang, path, other['path'])
    h += hero_svc(lang, t['crumbs'], t['big'], t['sub'], t['lead'], (buy_href, buy_label),
                  [(f'guide-{lang}-p01', t['hero_alt'][0], 'u-doc'), ('course', t['hero_alt'][1], 'u-c3')])
    h += strip(t['marquee'])
    h += intro2(t['intro_label'], t['intro_title'], t['intro_tag'], [(f'guide-{lang}-p06', t['feat_alts'][1]), (f'guide-{lang}-p02', t['feat_alts'][0])],
                t['intro_body'], t['chips'])
    cells = []
    for k, ((hd, txt), im, alt) in enumerate(zip(t['feats'], FEAT_IMGS[lang], t['feat_alts'])):
        cells += [('img', im, alt), ('panel', f'{k + 1:02d}', hd, txt, k % 2 == 1)]
    h += features2(t['feat_title'], t['feat_sub'], cells)
    rows = ''.join(f'<div><dt class="k">{n}</dt><dd class="v">{p}</dd></div>' for n, p in t['toc'])
    h += f'''<section class="sec u u-guide" aria-labelledby="toc-h"><div class="wrap guide">
<aside><p class="lbl red">{t['toc_label']}</p><h2 class="big-h" id="toc-h">{t['toc_title']}</h2></aside>
<article><dl class="rows">{rows}</dl></article>
</div></section>
'''
    h += pricing2(t['price_label'], t['price_title'], t['price_note'],
                  [(t['price_col'], g['price'] if ok else t['price_tbd'], t['price_items'], buy_label)], buy_href,
                  imgs=[(f'guide-{lang}-p01', t['hero_alt'][0])])
    h += steps2(t['steps_title'], t['steps_sub'], t['steps'])
    h += faq(lang, {'cs': 'časté dotazy', 'uk': 'часті запитання'}.get(lang, 'FAQ'), t['faq'], title=t['faq_title'])
    h += footer(lang, t['foot'][0], t['foot'][1], t['foot'][2], (buy_href, buy_label) if ok else None)
    if ok:   # Stripe checkout opens in a new tab, so the guide page stays open
        h = h.replace(f'href="{buy_href}"', f'href="{buy_href}" target="_blank" rel="noopener"')
    write(path, h)


PROMO = {
    'cs': dict(lbl='Novinka', h='Holky, <em>průvodce štětci</em> je tady!', p='Který štětec na co, jakým pohybem s ním pracovat a jak ho mýt. 23 stran PDF a 2 neveřejná videa.', btn='Chci průvodce →'),
    'en': dict(lbl='New', h='Girls, the <em>brush guide</em> is here!', p='Which brush for what, which movement to use and how to wash them. A 23-page PDF and 2 private videos.', btn='Get the guide →'),
    'uk': dict(lbl='Новинка', h='Дівчата, <em>гайд по пензликах</em> уже тут!', p='Який пензлик для чого, яким рухом працювати і як мити. PDF на 23 сторінки і 2 закриті відео.', btn='Хочу гайд →'),
}


def promo(lang):
    """Sticky card for the right column of blog articles (and a full-width card on narrower screens)."""
    if not ready(lang):
        return ''
    g, t = GUIDE[lang], PROMO[lang]
    return f'''<aside class="post-promo" aria-label="{T[lang]['price_col']}"><a class="pp-card" href="{g['path']}">
<span class="pp-ph">{I(f'guide-{lang}-p01', T[lang]['hero_alt'][0], sizes='(max-width: 1200px) 40vw, 240px', cls='u-doc')}</span>
<span class="pp-txt"><span class="pp-lbl">{t['lbl']} · PDF</span>
<span class="pp-h">{t['h']}</span>
<span class="pp-p">{t['p']}</span>
<span class="pp-row"><span class="pp-price">{g['price']}</span><span class="pp-btn">{t['btn']}</span></span></span>
</a></aside>'''


FAB = {
    'cs': dict(lbl='Novinka', name='Průvodce štětci', close='Zavřít'),
    'en': dict(lbl='New', name='Brush guide', close='Close'),
    'uk': dict(lbl='Новинка', name='Гайд по пензликах', close='Закрити'),
}


def fab(lang):
    """Small floating guide button (bottom right) for the home and service pages.
    Slides in after a little scrolling; the × hides it for 7 days (localStorage, ignored if unavailable)."""
    if not ready(lang):
        return ''
    g, t = GUIDE[lang], FAB[lang]
    return f'''<div class="g-fab" data-fab hidden>
<a class="g-fab-a" href="{g['path']}"><span class="g-fab-ph">{I(f'guide-{lang}-p01', '', sizes='56px', cls='u-doc')}</span>
<span class="g-fab-t"><span class="g-fab-l">{t['lbl']} · PDF</span><span class="g-fab-n">{t['name']}</span><span class="g-fab-p">{g['price']} <span aria-hidden="true">→</span></span></span></a>
<button class="g-fab-x" type="button" aria-label="{t['close']}" data-fab-x>×</button>
</div>
<script>(function(){{var k='guideFab',f=document.querySelector('[data-fab]'),n=Date.now();
try{{if(+localStorage.getItem(k)>n)return}}catch(e){{}}
f.hidden=false;function s(){{if(scrollY>500){{f.classList.add('is-on');removeEventListener('scroll',s)}}}}addEventListener('scroll',s,{{passive:true}});s();
f.querySelector('[data-fab-x]').addEventListener('click',function(){{f.classList.remove('is-on');try{{localStorage.setItem(k,n+6048e5)}}catch(e){{}}}});}})();</script>
'''


def build():
    for lang in LANGS:
        sales(lang)
        if not ready(lang):
            print(f'  ! brush guide ({lang}): set stripe_link and price in _build/pages_guide.py – page is noindex until then')
