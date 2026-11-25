"""Home page body (hero → pricing) in the 2026-11 style, shared by / and /en/.
Copy is the existing home-page copy; reviews, blog teaser, FAQ and footer come from lib."""
from lib import *
from lib import img as I

T = {
    'cs': dict(
        chips=['5,0 ★ Google', 'Praha 8 – Karlín', 'Česky · English · Українська'],
        hero_p='Ahoj! Jmenuji se Nikol a miluju tvořit krásné a jedinečné líčení, které zdůrazní to nejlepší v tobě. Pojďme společně vytvořit něco výjimečného!',
        h1=('Nikol Pavlova', '– profesionální vizážistka v Praze'), hero_alt='Nikol Pavlova – profesionální vizážistka v Praze',
        book='Rezervovat termín +', more='Moje služby ↓',
        strip=['Svatební líčení', 'Nude makeup', 'Večerní líčení', 'Komerční líčení', 'Kurzy líčení', 'Praha 8 – Karlín · možnost dojezdu'],
        svc_label='služby', svc_h=('Co', 'nabízím'), portfolio_link=('/portfolio/', 'Celé portfolio →'),
        svc=[('Svatební líčení', 'Dlouhotrvající &amp; zářivé', 'Nabídka do 24 h', '/svatebni-liceni/', 'wedding-5', 'Svatební líčení Praha', 1),
             ('Nude makeup', 'Přirozená krása', '', '/nude-liceni/', 'nude-1', 'Nude makeup Praha', 2),
             ('Večerní líčení', 'Plesy a večírky', 'od 2 500 Kč', '/vecerni-liceni/', 'evening-5', 'Večerní líčení Praha', 3),
             ('Komerční líčení', 'Focení a reklama', '', '/komercni-liceni/', 'commercial-4', 'Komerční líčení – focení pro beauty značku', 4),
             ('Kurzy líčení', 'Naučte se líčit jako profík', 'Na vyžádání', '/kurzy-liceni/', 'course', 'Kurzy líčení Praha', 5)],
        season=('Plesová sezóna 2027', ('Líčení i účes', 'na ples'),
                'Maturitní, reprezentační i firemní plesy. Líčení 2 500 Kč, líčení s účesem 4 500 Kč (ušetříte 500 Kč) – lednové a únorové soboty se plní nejdřív.',
                '/plesove-liceni/', 'Plesové líčení →'),
        about_label='O mně', about_h='Nikol Pavlova je vizážistka v Praze', about_tag='tvořící líčení, ve kterém se cítíš jako ty',
        about_alt='Nikol Pavlova – portrét vizážistky',
        about_p='Ahoj, jsem Nikol, profesionální vizážistka v Praze. Můj styl spojuje precizní techniku, kreativitu a cit pro barvy i textury, díky čemuž vytvářím make-up looky, které dokonale zvýrazní tvou přirozenou krásu. Ať už toužíš po jemném svatebním vzhledu, odvážném večerním make-upu nebo originálním editoriálním looku, vždycky mě baví společně s tebou proměnit tvou vizi ve skutečnost.',
        chips2=['Svatební specialistka', 'Editorial &amp; Komerce', 'Osobní kurzy líčení', 'Česky · English · Українська'],
        about_more=('/o-mne/', 'Více o mně →'),
        mos_h=('Tvořím looky, které zdůrazní tvou', 'přirozenou krásu'), mos_p='Od jemného svatebního glow po výrazný editoriální look.',
        mos_btn=('/portfolio/', 'Zobrazit portfolio →'),
        mos=[('wedding-1', 'Svatební look – jemný glam'), ('wedding-15', 'Svatební look – soft glam'), ('evening-3', 'Večerní look – výrazný ret a čistá pleť'),
             ('nude-3', 'Nude look – svěží dewy pleť'), ('commercial-6', 'Komerční look – editorial'), ('wedding-9', 'Svatební look – destination svatba v Praze'),
             ('evening-13', 'Večerní look – soft glam'), ('wedding-14', 'Svatební look – soft glam svatební líčení')],
        phrase='Precizní technika, <em>kreativita</em><br>a cit <em>pro barvy i textury</em>', phrase_label='Můj přístup',
        price_label='balíčky služeb', price_h='Ceník', price_note='*Pro konkrétní cenovou nabídku mě prosím kontaktujte.',
        price=[('Svatba', 'Svatební balíček', 'Info', '/svatebni-liceni/', 'bride-calla', 'Nevěsta s kyticí kal – svatební líčení', ['Zkouška líčení', 'Svatební make-up', 'Umělé řasy v ceně', 'Touch-up kit']),
               ('Speciální příležitosti', 'Ples, večer &amp; akce', 'od 2 500 Kč', '/plesove-liceni/', 'ev-gold', 'Speciální příležitosti – plesové a večerní líčení', ['Plesové líčení', 'Večerní make-up', 'Účes', 'Líčení na akce']),
               ('Kurzy', 'Osobní kurz líčení', 'Na vyžádání', '/kurzy-liceni/', 'nude-2', 'Kurzy líčení', ['Příprava pleti', 'Teorie barev', 'Oči &amp; řasy', 'Nástroje &amp; produkty'])]),
    'en': dict(
        chips=['5.0 ★ Google', 'Prague 8 – Karlín', 'English · Česky · Українська'],
        hero_p='Hi beautiful! I love designing beautiful makeup looks which enhance your natural features and distinctive style. Let\'s create stunning makeup transformations together!',
        h1=('Nikol Pavlova', '– English-speaking makeup artist in Prague'), hero_alt='Nikol Pavlova – professional makeup artist in Prague',
        book='Book an appointment +', more='My services ↓',
        strip=['Wedding makeup', 'Nude makeup', 'Evening makeup', 'Commercial', 'Makeup courses', 'Prague 8 – Karlín · available for travel'],
        svc_label='my services', svc_h=('What', 'I do'), portfolio_link=('/en/portfolio/', 'Full portfolio →'),
        svc=[('Wedding makeup', 'Long-lasting &amp; radiant', 'Quote within 24 h', '/en/wedding/', 'wedding-5', 'Wedding makeup Prague', 1),
             ('Nude makeup', 'Enhancing natural beauty', '', '/en/nude-makeup/', 'nude-1', 'Nude makeup Prague', 2),
             ('Evening makeup', 'Elegant &amp; glamorous', 'from CZK 2,500', '/en/evening-makeup/', 'evening-5', 'Evening makeup Prague', 3),
             ('Commercial', 'Photo shoots &amp; media', '', '/en/commercial-makeup/', 'commercial-4', 'Commercial makeup for a beauty brand shoot', 4),
             ('Makeup courses', 'Learn professional techniques', 'On request', '/en/courses/', 'course', 'Makeup courses Prague', 5)],
        season=None,
        about_label='About me', about_h='Nikol Pavlova is a makeup artist in Prague', about_tag='creating makeup that still feels like you',
        about_alt='Nikol Pavlova – makeup artist portrait',
        about_p='My name is Nikol Pavlova and I work as your dedicated makeup artist based in Prague. I love designing beautiful makeup looks which enhance your natural features and distinctive style. I will transform your vision into reality whether you dream of a soft bridal glow or glamorous evening makeup or something boldly creative. My commitment lies in precision and creativity.',
        chips2=['Bridal Specialist', 'Editorial &amp; Commercial', 'Personalized Courses', 'English · Česky · Українська'],
        about_more=('/en/about/', 'More about me →'),
        mos_h=('I create looks that enhance your', 'natural beauty'), mos_p='From a soft bridal glow to a bold editorial look.',
        mos_btn=('/en/portfolio/', 'View portfolio →'),
        mos=[('wedding-1', 'Bridal look – soft glam'), ('wedding-15', 'Bridal look – soft glam'), ('evening-3', 'Evening look – bold lip and clean skin'),
             ('nude-3', 'Nude look – fresh dewy skin'), ('commercial-6', 'Commercial look – editorial'), ('wedding-9', 'Bridal look – Prague destination wedding'),
             ('evening-13', 'Evening look – soft glam'), ('wedding-14', 'Bridal look – soft glam bridal makeup')],
        phrase='Precise technique, <em>creativity</em><br>and a feeling <em>for colour &amp; texture</em>', phrase_label='My approach',
        price_label='pricing packages', price_h='Rates', price_note='*Please contact me for a personalised quote.',
        price=[('Wedding', 'Wedding package', 'Request', '/en/wedding/', 'bride-calla', 'Bride with a calla bouquet – wedding makeup', ['Bridal Trial', 'Wedding Day Makeup', 'Lashes Included', 'Touch-up Kit']),
               ('Special occasions', 'Balls, evenings &amp; events', 'from CZK 2,500', '/en/ball-makeup/', 'ev-gold', 'Special occasion makeup – ball and evening makeup', ['Ball Makeup', 'Evening Makeup', 'Hairstyling', 'Event Makeup']),
               ('Courses', 'Personal makeup lesson', 'Request', '/en/courses/', 'nude-2', 'Makeup courses', ['Skin Prep', 'Colour Theory', 'Eyes &amp; Lashes', 'Tools &amp; Products'])]),
}


def home_body(lang):
    t = T[lang]
    chips = ''.join(f'<li class="hm-chip">{c}</li>' for c in t['chips'])
    strip = ''.join(f'<span>{x}</span><span class="hm-dot" aria-hidden="true">✦</span>' for x in t['strip'])
    svc = ''.join(f'<li><a class="hm-svc" href="{u}"><span class="hm-svc-ph">{I(im, alt, sizes="(max-width: 700px) 100vw, (max-width: 1200px) 33vw, 20vw", cls="hm-c" + str(k))}'
                  f'<span class="hm-gel hm-gel--{k}" aria-hidden="true"></span></span>'
                  f'<span class="hm-svc-row"><h3>{n}</h3>{f"<small>{p}</small>" if p else ""}</span><span class="hm-svc-sub">{d}</span></a></li>'
                  for n, d, p, u, im, alt, k in t['svc'])
    season = ''
    if t['season']:
        lab, (h1_, h2_), txt, u, btn = t['season']
        season = (f'<section class="wrap hm-season-w" aria-labelledby="season-h"><a class="hm-season" href="{u}"><span class="hm-season-txt">'
                  f'<span class="hm-label">({lab})</span><span class="hm-h3" id="season-h">{h1_} <em>{h2_}</em></span><span class="hm-p">{txt}</span>'
                  f'<span class="hm-btn">{btn}</span></span><span class="hm-season-img">{I("evening-14", "", sizes="(max-width: 900px) 100vw, 45vw", cls="hm-c2")}</span></a></section>\n')
    chips2 = ''.join(f'<li>{c}</li>' for c in t['chips2'])
    mos = ''.join(f'<span class="hm-mo hm-mo--{i + 1}">{I(im, alt, sizes="260px")}</span>' for i, (im, alt) in enumerate(t['mos']))
    mos_dup = ''.join(f'<span class="hm-mo hm-mo--{i + 1}">{I(im, "", sizes="260px")}</span>' for i, (im, alt) in enumerate(t['mos']))
    PC_POS = {'bride-calla': 'hm-pc1', 'ev-gold': 'hm-pc2', 'nude-2': 'hm-pc3'}
    price = ''.join(f'<li><a class="hm-pc" href="{u}"><span class="hm-pc-ph">{I(im, alt, sizes="(max-width: 900px) 100vw, 33vw", cls=PC_POS.get(im, ""))}<span class="hm-tag">{tag}</span></span>'
                    f'<span class="hm-pc-b"><h3>{n}</h3><span class="hm-price">{p}</span><span class="hm-list">{"".join(f"<span>— {x}</span>" for x in li)}</span></span></a></li>'
                    for tag, n, p, u, im, alt, li in t['price'])
    return f'''<div class="hm">
<section class="hm-hero" aria-labelledby="page-h1">
{I('nikol-hero', t['hero_alt'], sizes='100vw', priority=True, cls='hm-hero-img')}
<span class="hm-hero-gel" aria-hidden="true"></span><span class="hm-rays" aria-hidden="true"></span><span class="hm-hero-shade" aria-hidden="true"></span>
<div class="wrap hm-hero-in">
<ul class="hm-chips" role="list">{chips}</ul>
<div class="hm-hero-row">
<h1 class="hm-h1" id="page-h1"><span class="big">{t['h1'][0]}</span> <span class="sub">{t['h1'][1]}</span></h1>
<div class="hm-hero-side"><p>{t['hero_p']}</p><p class="hm-btns"><a class="hm-btn hm-btn--light" href="{CAL}">{t['book']}</a><a class="hm-btn hm-btn--line" href="#services">{t['more']}</a></p></div>
</div></div>
</section>
<div class="hm-strip" aria-hidden="true"><div class="hm-mq">{strip}{strip}</div></div>
<section class="wrap hm-sec" id="services" aria-labelledby="services-h">
<div class="hm-head"><div><p class="hm-label">({t['svc_label']})</p><h2 class="hm-h2" id="services-h">{t['svc_h'][0]} <em>{t['svc_h'][1]}</em></h2></div>
<a class="hm-link" href="{t['portfolio_link'][0]}">{t['portfolio_link'][1]}</a></div>
<ul class="hm-svcs" role="list">{svc}</ul>
</section>
{season}<section class="wrap hm-about" id="about" aria-labelledby="about-h">
<span class="hm-about-ph">{I('nikol-about', t['about_alt'], sizes='(max-width: 900px) 100vw, 460px', cls='hm-c3')}<span class="hm-about-gel" aria-hidden="true"></span></span>
<div class="hm-about-txt"><p class="hm-label">({t['about_label']})</p>
<h2 class="hm-h2 hm-h2--m" id="about-h">{t['about_h']}</h2><p class="hm-tagline"><em>{t['about_tag']}</em></p>
<p class="hm-p">{t['about_p']}</p>
<ul class="hm-chips2" role="list">{chips2}</ul>
<a class="hm-link" href="{t['about_more'][0]}">{t['about_more'][1]}</a></div>
</section>
<section class="hm-mos-sec" aria-labelledby="mos-h">
<div class="wrap hm-head"><div><h2 class="hm-h2 hm-h2--m" id="mos-h">{t['mos_h'][0]} <em>{t['mos_h'][1]}</em></h2><p class="hm-p hm-mos-p">{t['mos_p']}</p></div>
<a class="hm-btn hm-btn--dark" href="{t['mos_btn'][0]}">{t['mos_btn'][1]}</a></div>
<div class="hm-mos"><div class="hm-mq hm-mq--slow">{mos}<span class="hm-dup" aria-hidden="true">{mos_dup}</span></div></div>
</section>
<section class="wrap hm-phrase-w" aria-label="{t['phrase_label']}"><p class="hm-phrase">{t['phrase']}</p></section>
<section class="hm-price-sec" id="pricing" aria-labelledby="pricing-h"><div class="wrap">
<div class="hm-head"><div><p class="hm-label">({t['price_label']})</p><h2 class="hm-h2" id="pricing-h">{t['price_h']}</h2></div><p class="hm-note">{t['price_note']}</p></div>
<ul class="hm-pcs" role="list">{price}</ul>
</div></section>
</div>
'''
