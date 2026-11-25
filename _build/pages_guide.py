"""Paid PDF guide: sales pages (CZ + EN) and the thank-you pages Stripe redirects to after payment.

How the sale works
  1. "Buy" buttons open a Stripe Payment Link (STRIPE_LINK below).
  2. In the Payment Link, "After payment" redirects to THANKS_PATH?session_id={CHECKOUT_SESSION_ID}.
  3. The thank-you page sends the buyer to DOWNLOAD_API/download?session_id=...&lang=..
     (the Cloudflare Worker in _worker/guide-download), which checks with Stripe that the session
     is paid and streams the PDF from a private R2 bucket. The PDFs are never in this public repo.

Until STRIPE_LINK, PRICE and DOWNLOAD_API are filled in, the pages are built with noindex,
left out of the sitemap and the build prints a warning.
"""
from lib import *
from lib import img as I
from ui26 import hero_svc, strip, intro2, features2, pricing2, steps2

# ---------------------------------------------------------------- settings (fill in before launch)
DOWNLOAD_API = ''   # e.g. 'https://guide.nikolmakeup.cz' (the Worker's URL, no trailing slash)
GUIDE = {
    'cs': dict(path='/pruvodce-stetci/', thanks='/pruvodce-stetci/dekuji/',
               stripe_link='',      # e.g. 'https://buy.stripe.com/xxxx' (Payment Link for the CZ guide)
               price='', price_num=None, currency='CZK'),   # price shown on the page, e.g. '390 Kč'; price_num=390
    'en': dict(path='/en/brush-guide/', thanks='/en/brush-guide/thank-you/',
               stripe_link='',      # Payment Link for the EN guide
               price='', price_num=None, currency='EUR'),   # e.g. '€15'; price_num=15
}


def ready(lang):
    g = GUIDE[lang]
    return bool(g['stripe_link'] and g['price'] and DOWNLOAD_API)


def pair_ready():
    return ready('cs') and ready('en')


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
            ('Zaplaťte přes Stripe', 'Tlačítko vás přenese na zabezpečenou platební stránku Stripe. Platíte kartou, Apple Pay nebo Google Pay.'),
            ('Otevře se stránka ke stažení', 'Hned po platbě se vrátíte na můj web, kde je tlačítko ke stažení PDF.'),
            ('Uložte si PDF', 'Průvodce si uložte do telefonu nebo počítače – otevřete ho kdykoli i bez internetu.'),
            ('Pusťte si videa', 'Videa otevřete přes tlačítka přímo v PDF. Jsou neveřejná, prosím, nepřeposílejte je.')],
        faq_title='Dotazy k průvodci', faq=[
            ('V jakém formátu průvodce je?', 'Je to PDF o 23 stranách. Otevřete ho v telefonu, tabletu i počítači.'),
            ('Jak průvodce dostanu?', 'Hned po zaplacení vás Stripe vrátí na můj web na stránku s tlačítkem ke stažení PDF.'),
            ('Musím si koupit stejné štětce?', 'Ne. Seznam štětců není povinný – průvodce vás naučí, jaký tvar a vlas štětce potřebujete. Na konci jsou i alternativy k zakoupení v Česku (Notino, Douglas).'),
            ('Je průvodce i v angličtině?', 'Ano, anglickou verzi najdete na stránce <a href="/en/brush-guide/">Makeup brush guide</a>.'),
            ('Stažení nefunguje, co teď?', f'Napište mi na <a href="mailto:{MAIL}">{MAIL}</a> e-mail, který jste zadali při platbě, a průvodce vám pošlu.')],
        foot=('Máte dotaz k průvodci?', 'Kontaktujte mě', 'Napište mi, ráda poradím, jestli je průvodce pro vás.'),
        # thank-you page
        ty_title='Děkuji za nákup | Průvodce štětci – Nikol Pavlova',
        ty_big='Děkuji!', ty_sub='váš průvodce štětci je připravený',
        ty_text='Platba proběhla. Stáhněte si PDF a uložte si ho do telefonu nebo počítače.',
        ty_btn='Stáhnout průvodce (PDF)', ty_note='Odkaz ke stažení platí 30 dní – uložte si PDF hned.',
        ty_missing=f'Odkaz ke stažení se nenačetl. Napište mi prosím na <a href="mailto:{MAIL}">{MAIL}</a> e-mail, který jste zadali při platbě, a průvodce vám pošlu.',
        ty_next='Mezitím se podívejte do blogu', ty_next_href='/blog/jak-myt-stetce-na-make-up/', ty_next_label='Jak mýt štětce na make-up →',
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
            ('Pay via Stripe', 'The button takes you to Stripe’s secure checkout. Pay by card, Apple Pay or Google Pay.'),
            ('The download page opens', 'Right after payment you come back to my site, to a page with the PDF download button.'),
            ('Save the PDF', 'Save the guide to your phone or computer – open it any time, even offline.'),
            ('Watch the videos', 'Open the videos with the buttons inside the PDF. They are private, so please don’t share them.')],
        faq_title='Questions about the guide', faq=[
            ('What format is the guide?', 'It’s a 23-page PDF. It opens on a phone, tablet or computer.'),
            ('How do I get the guide?', 'Right after payment Stripe sends you back to my site, to a page with the PDF download button.'),
            ('Do I need to buy the same brushes?', 'No. The brush list isn’t mandatory – the guide teaches you which brush shape and bristle you need. At the end there are also alternatives you can buy in Czechia (Notino, Douglas).'),
            ('Is the guide available in Czech?', 'Yes, the Czech version is on the <a href="/pruvodce-stetci/">Průvodce štětci</a> page.'),
            ('The download doesn’t work – what now?', f'Email me at <a href="mailto:{MAIL}">{MAIL}</a> from the address you used at checkout and I’ll send you the guide.')],
        foot=('Questions about the guide?', 'Get in touch', 'Message me and I’ll help you decide whether the guide is right for you.'),
        ty_title='Thank you | Makeup Brush Guide – Nikol Pavlova',
        ty_big='Thank you!', ty_sub='your brush guide is ready',
        ty_text='Your payment went through. Download the PDF and save it to your phone or computer.',
        ty_btn='Download the guide (PDF)', ty_note='The download link works for 30 days – save the PDF now.',
        ty_missing=f'The download link didn’t load. Please email me at <a href="mailto:{MAIL}">{MAIL}</a> from the address you used at checkout and I’ll send you the guide.',
        ty_next='In the meantime, read on the blog', ty_next_href='/en/blog/how-to-wash-makeup-brushes/', ty_next_label='How to wash makeup brushes →',
    ),
}

FEAT_IMGS = {'cs': ['guide-cs-p02', 'guide-cs-p06', 'brushes-hero', 'guide-cs-p21'],
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
    t, g, other = T[lang], GUIDE[lang], GUIDE['en' if lang == 'cs' else 'cs']
    path, ok = g['path'], ready(lang)
    buy_href = g['stripe_link'] if ok else '#packages'
    buy_label = f"{t['buy']} – {g['price']} +" if ok else t['buy_soon']
    alts = [('cs', GUIDE['cs']['path']), ('en', GUIDE['en']['path']), ('x-default', GUIDE['cs']['path'])] if pair_ready() else []
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
    h += faq(lang, 'FAQ' if lang == 'en' else 'časté dotazy', t['faq'], title=t['faq_title'])
    h += footer(lang, t['foot'][0], t['foot'][1], t['foot'][2], (buy_href, buy_label) if ok else None)
    write(path, h)


def thanks(lang):
    """Stripe redirects here with ?session_id=cs_...; the button goes to the Worker, which checks the payment."""
    t, g = T[lang], GUIDE[lang]
    path = g['thanks']
    h = head(lang, t['ty_title'], t['ty_text'], path, [], SITE + f'/assets/img/guide-{lang}-p01-800.webp', [])
    h = _noindex(h, path)
    h = h.replace('</head>', '<meta name="referrer" content="no-referrer">\n</head>', 1)   # keep session_id out of Referer headers
    h += header(lang, '', GUIDE['en' if lang == 'cs' else 'cs']['thanks'])
    h += f'''<div class="u"><section class="u-hero" aria-labelledby="page-h1">
<div class="u-hero-txt">
<h1 class="u-h1" id="page-h1"><span class="big">{t['ty_big']}</span> <span class="sub">{t['ty_sub']}</span></h1>
<p class="u-lead">{t['ty_text']}</p>
<p data-dl hidden><a class="u-btn u-btn--dark" data-dl-btn href="#">{t['ty_btn']}</a></p>
<p class="u-lead" data-dl hidden style="font-size:15px;line-height:1.7">{t['ty_note']}</p>
<p class="u-lead" data-dl-missing hidden style="font-size:15px;line-height:1.7">{t['ty_missing']}</p>
<p style="margin-top:16px"><a class="u-link" href="{t['ty_next_href']}">{t['ty_next_label']}</a></p>
</div>
<div class="u-hero-ph"><span class="u-ph u-ph--a">{I(f'guide-{lang}-p01', t['hero_alt'][0], sizes='(max-width: 900px) 60vw, 30vw', cls='u-doc', priority=True)}</span>
<div class="u-hero-col"><span class="u-ph u-ph--b">{I(f'guide-{lang}-p21', t['feat_alts'][3], sizes='(max-width: 900px) 40vw, 22vw', cls='u-doc')}</span></div></div>
</section></div>
<script>(function(){{var id=new URLSearchParams(location.search).get('session_id'),api={DOWNLOAD_API!r};
var ok=id&&/^cs_(test|live)_[A-Za-z0-9]+$/.test(id)&&api;
document.querySelectorAll(ok?'[data-dl]':'[data-dl-missing]').forEach(function(e){{e.hidden=false}});
if(ok)document.querySelector('[data-dl-btn]').href=api+'/download?lang={lang}&session_id='+encodeURIComponent(id);}})();</script>
'''
    h += footer(lang, t['foot'][0], t['foot'][1], t['foot'][2])
    write(path, h)


def build():
    for lang in ('cs', 'en'):
        sales(lang)
        thanks(lang)
        if not ready(lang):
            print(f'  ! brush guide ({lang}): set stripe_link, price and DOWNLOAD_API in _build/pages_guide.py – page is noindex until then')
