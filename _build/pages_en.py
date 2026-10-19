from lib import *
from lib import img as I
import schema as S
from reviews import pick
from pages_cs import PORTFOLIO_ITEMS, portfolio_grid, NOSCRIPT

LANG = 'en'
HOME = ('Home', '/en/')
SVC = ('Services', '/en/#services')


def alts(cs, en):
    return [('cs', cs), ('en', en), ('x-default', cs)] if cs else [('en', en)]


BOOK_FAQ = ('How can I book an appointment?', f'Book online via <a href="{CAL}">Calendly</a>, call or text <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a>, or send a message on Instagram <a href="{IG}">@nikol__mua</a>. I usually reply within a few hours.')


# ---------------------------------------------------------------- HOME
def home():
    path = '/en/'
    title = 'Nikol Pavlova - Professional Makeup Artist in Prague'
    desc = 'Professional English-speaking makeup artist in Prague. Specialized in bridal, evening styling and courses. Book your appointment.'
    faq_items = [
        ('Where are you based and do you travel for bookings?', 'I am a professional makeup artist based in Prague, Czech Republic. I work across all districts of Prague – including Praha 1 (Old Town), Praha 2 (Vinohrady), and Praha 7 – and I also travel to other cities in the Czech Republic and across Europe for destination weddings, photo shoots and events.'),
        ('What makeup services do you offer?', 'I offer wedding and bridal makeup, evening and cocktail styling, natural nude looks, prom and ball makeup, commercial and editorial makeup for photo shoots, and personalized one-on-one makeup courses for clients who want to learn professional techniques.'),
        ('Do you speak English?', 'Yes. I provide makeup services fluently in English and Czech, which makes me a comfortable choice for international clients, expats living in Prague, and couples planning a destination wedding in the Czech Republic.'),
        ('What is included in the wedding makeup package?', 'The wedding package includes a bridal trial before the wedding day, full wedding-day makeup application, false lashes, and a personal touch-up kit so your look stays fresh from the ceremony through the reception.'),
        ('How much does makeup in Prague cost?', 'Prices depend on the type of service, location, and timing – bridal packages, evening makeup and commercial shoots are all priced individually. Please contact me with your event details and I will send you a personalized quote within 24 hours.'),
        ('How far in advance should I book?', 'For weddings I recommend booking 6–12 months in advance, especially for the peak season from May to September. For evening makeup and shoots, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'),
        ('What does a makeup course look like?', 'Courses are personalized one-on-one sessions tailored to your skill level and goals – from learning everyday makeup for yourself to professional techniques for aspiring MUAs. We cover skin prep, color theory, application techniques, and product selection using your own face as the canvas.'),
        ('How can I book an appointment?', f'You can book <a href="{CAL}">online via Calendly</a>, call or text <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a>, or send a direct message on Instagram <a href="{IG}">@nikol__mua</a>. I usually reply within a few hours.'),
    ]
    h = head(LANG, title, desc, path, alts('/', '/en/'), SITE + '/img/nikol.jpg', S.load('en-home'), preload('nikol-hero', '100vw'))
    h += header(LANG, 'home', '/')
    h += f'''<section class="hero-full" aria-labelledby="page-h1">
{I('nikol-hero', 'Nikol Pavlova – professional makeup artist in Prague', sizes='100vw', priority=True, style='object-position:50% 30%')}
<div class="wrap inner"><div></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="hero-row"><p>Hi beautiful! I love designing beautiful makeup looks which enhance your natural features and distinctive style. Let's create stunning makeup transformations together!</p><a class="btn btn--light" href="#services">My services <span aria-hidden="true">↓</span></a></div>
<h1 class="h1" id="page-h1"><span class="big">Nikol Pavlova</span><span class="sub">– English-speaking makeup artist in Prague</span></h1>
</div></div>
</section>
'''
    h += marquee(['Wedding makeup', 'Nude makeup', 'Evening makeup', 'Commercial', 'Makeup courses', 'Prague 7 · available for travel'])
    h += f'''<section class="wrap intro" id="about" aria-labelledby="about-h">
<div class="head"><p class="lbl red">About me</p><h2 class="mid-h" id="about-h">Nikol Pavlova is a makeup artist in Prague</h2><p class="serif tag">creating makeup that still feels like you</p></div>
<div class="pair">{I('nikol-portrait', 'Nikol Pavlova – makeup artist portrait', sizes='260px', style='object-position:50% 25%')}{I('nikol-header', 'Nikol Pavlova – makeup artist in Prague', sizes='260px', style='object-position:50% 20%')}</div>
<div class="rule" aria-hidden="true"><span class="serif">precision</span><hr><span class="serif">natural beauty.</span></div>
<p class="body">My name is Nikol Pavlova and I work as your dedicated makeup artist based in Prague. I love designing beautiful makeup looks which enhance your natural features and distinctive style. I will transform your vision into reality whether you dream of a soft bridal glow or glamorous evening makeup or something boldly creative. My commitment lies in precision and creativity.</p>
<ul class="chips"><li>Bridal Specialist</li><li>Editorial &amp; Commercial</li><li>Personalized Courses</li><li>English · Česky · Українська</li></ul>
{I('signature', 'Nikol Pavlova signature', sizes='220px', style='width:220px')}
</section>
<section id="services" aria-labelledby="services-h">
<div class="wrap">{sec_head('What I do', 'my services', '<a class="link-arrow" href="/en/portfolio/">Full portfolio →</a>', hid='services-h')}</div>
<ul class="g4" role="list">
<li>{I('wedding-5', 'Wedding makeup Prague')}</li>
<li><a class="tile-panel center" href="/en/wedding/"><h3>Wedding makeup</h3><p class="serif">Long-lasting &amp; radiant</p><span class="lbl more">Details →</span></a></li>
<li>{I('nude-1', 'Nude makeup Prague')}</li>
<li><a class="tile-panel center alt" href="/en/nude-makeup/"><h3>Nude makeup</h3><p class="serif">Enhancing natural beauty</p><span class="lbl more">Details →</span></a></li>
<li><a class="tile-panel center alt" href="/en/evening-makeup/"><h3>Evening makeup</h3><p class="serif">Elegant &amp; glamorous</p><span class="lbl more">Details →</span></a></li>
<li>{I('evening-5', 'Evening makeup Prague')}</li>
<li><a class="tile-panel center" href="/en/commercial-makeup/"><h3>Commercial</h3><p class="serif">Photo shoots &amp; media</p><span class="lbl more">Details →</span></a></li>
<li>{I('commercial-4', 'Commercial makeup for a beauty brand shoot')}</li>
<li>{I('course', 'Makeup courses Prague', style='object-position:50% 15%')}</li>
<li><a class="tile-panel center" href="/en/courses/"><h3>Makeup courses</h3><p class="serif">Learn professional techniques</p><span class="lbl more">Details →</span></a></li>
<li class="span2"><a class="tile-panel center dark" style="height:100%" href="{CAL}"><p class="serif" style="font-size:28px">Your look, your day.</p><h3 style="font-size:30px">Book an appointment +</h3></a></li>
</ul>
</section>
<section class="mos-sec" aria-labelledby="mos-h">
<div class="wrap"><div class="mos">
<h2 class="m-t big-h" id="mos-h" style="font-size:clamp(24px,2.4vw,30px);line-height:1.15">I create looks that enhance your <span class="accent">natural beauty</span></h2>
{I('wedding-1', 'Bridal look – soft glam', cls='m1')}
{I('wedding-15', 'Bridal look – soft glam', sizes='(max-width: 900px) 50vw, 33vw', cls='m2')}
{I('evening-3', 'Evening look – bold lip and clean skin', sizes='(max-width: 900px) 50vw, 33vw', cls='m3')}
{I('nude-3', 'Nude look – fresh dewy skin', cls='m4')}
{I('commercial-6', 'Commercial look – editorial', cls='m5')}
{I('wedding-9', 'Bridal look – Prague destination wedding', cls='m6')}
{I('evening-13', 'Evening look – soft glam', cls='m7')}
<div class="m-s"><p class="lbl pink">Bridal Specialist · Editorial &amp; Commercial · Personalized Courses</p><p class="serif" style="font-size:clamp(22px,2.2vw,28px);line-height:1.2">From a soft bridal glow to a bold editorial look.</p><a class="btn btn--pink" href="/en/portfolio/">View portfolio →</a></div>
{I('wedding-14', 'Bridal look – soft glam bridal makeup', cls='m8')}
</div></div>
</section>
<section class="phrase" aria-label="My approach">
{I('contact', '', sizes='100vw', style='object-position:50% 30%')}<div class="mesh"></div>
<div class="wrap"><p><span>Precise</span><span>technique</span></p><p><span>Creativity</span><span>and feeling</span></p><p><span>For colour</span><span>&amp; texture</span></p></div>
</section>
<section class="sec" id="pricing" aria-labelledby="pricing-h">
<div class="wrap">
{sec_head('Rates', 'pricing packages', '<p class="serif muted2">*Please contact me for a personalised quote.</p>', hid='pricing-h')}
<ul class="cards3" role="list">
<li><a class="pcard" href="/en/wedding/"><div class="ph">{I('wedding-4', 'Wedding makeup package', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Wedding</span></div><div class="row"><h3>Wedding package</h3><span class="lbl red">Request</span></div><p class="body">Bridal Trial · Wedding Day Makeup · Lashes Included · Touch-up Kit</p></a></li>
<li><a class="pcard" href="/en/evening-makeup/"><div class="ph">{I('evening-7', 'Special occasion makeup', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Special occasions</span></div><div class="row"><h3>Evening &amp; events</h3><span class="lbl red">Request</span></div><p class="body">Cocktail Makeup · Evening Styling · Prom / Ball Makeup · Photo Shoots</p></a></li>
<li><a class="pcard" href="/en/courses/"><div class="ph">{I('nude-2', 'Makeup courses', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Courses</span></div><div class="row"><h3>Personal makeup lesson</h3><span class="lbl red">Request</span></div><p class="body">Skin Prep · Colour Theory · Eyes &amp; Lashes · Tools &amp; Products</p></a></li>
</ul></div>
</section>
'''
    h += reviews(LANG, 'what clients say', pick('zoe', 'nelli', 'glenn', 'polina', 'shirley', 'darya', 'beata', 'marie', 'lena'), top=False)
    h += faq(LANG, 'popular questions', faq_items)
    h += footer(LANG, 'Contact me', 'Do you need help with creative make-up?',
                "I'm committed to ensuring your satisfaction with bridal, event, or editorial makeup services. Reach out to plan your requirements.")
    write(path, h)


# ---------------------------------------------------------------- WEDDING
def wedding():
    path = '/en/wedding/'
    title = 'Wedding & Bridal Makeup Artist Prague | Nikol Pavlova MUA'
    desc = 'Professional bridal makeup artist in Prague. Nikol Pavlova offers wedding makeup packages including bridal trial, lashes and touch-up kit. English-speaking. Book: +420 608 178 390.'
    faq_items = [
        ('What is included in a wedding makeup package in Prague?', 'Every bridal package includes a personalised bridal trial, full wedding-day makeup application, false lashes, and a touch-up kit with the key products used on your skin. Travel to your Prague venue is included; travel fees may apply for locations outside Prague.'),
        ('How far in advance should I book a wedding makeup artist in Prague?', 'For weddings in Prague, especially during peak season from May to September, booking 6–12 months in advance is strongly recommended. Popular summer Saturdays book out quickly. For autumn and winter weddings, 3–6 months is usually sufficient.'),
        ('Are you available for destination weddings in the Czech Republic?', 'Yes. Nikol is based in Prague but regularly travels for destination weddings across the Czech Republic – South Moravia wine country, Bohemian châteaux, spa towns like Karlovy Vary – and across Europe. Travel and accommodation fees apply outside Prague.'),
        ('Do you speak English for international brides?', 'Yes. Nikol is fully fluent in English, Czech and Ukrainian, and regularly works with international brides, expats in Prague, and couples from the UK, USA, Ireland, Australia and elsewhere planning a destination wedding in the Czech Republic.'),
        ('How much does bridal makeup cost in Prague?', 'Bridal makeup pricing depends on the service scope, wedding location, date, and whether a bridal party is included. Nikol provides personalised quotes after an initial consultation – share your wedding details and she will respond within 24 hours.'),
        ('Can you do makeup for my entire bridal party?', 'Yes. Beyond the bride, Nikol provides makeup for bridesmaids, the mother of the bride and flower girls. Group packages are available, and a timed schedule is created in advance so everyone is ready before the ceremony.'),
        ('What bridal makeup styles do you offer?', "Nikol specialises in all bridal styles – soft natural glow, glamorous evening bridal, classic nude, Old Hollywood and bohemian romantic. Each look is tailored to the bride's skin, features, dress and theme, and the trial is the perfect time to explore directions."),
        ('How can I book a bridal consultation?', f'Book instantly online via the <a href="https://calendly.com/pavlovanikol/makeup-appointment">Calendly scheduling page</a>, or call/text <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a>, or send a direct message on Instagram <a href="{IG}">@nikol__mua</a>. Nikol typically replies within a few hours. Consultations can be held in person in Prague or by video call for international clients.'),
    ]
    h = head(LANG, title, desc, path, alts('/svatebni-liceni/', path), SITE + '/img/wedding/wedding-prague-1.png', S.load('en-wedding'), preload('wedding-prague', '100vw'))
    h += header(LANG, '/en/wedding/', '/svatebni-liceni/')
    h += f'''<section class="hero-full hero-full--svc" aria-labelledby="page-h1">
{I('wedding-prague', 'Bridal makeup Prague – bride and groom', sizes='100vw', priority=True, style='object-position:60% 30%')}
<div class="wrap inner">
<div>{crumbs(LANG, [HOME, SVC, ('Wedding makeup', None)], cls='lbl glass crumbs-glass')}</div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="hero-row"><p>Your wedding day deserves a look as unique as your love story. I create long-lasting, radiant bridal makeup that enhances your natural beauty – tailored entirely to you, your dress and your vision.</p><a class="btn btn--light" href="{CAL}">Book appointment online +</a></div>
<h1 class="h1" id="page-h1"><span class="big">Bridal makeup</span><span class="sub">in Prague – makeup that lasts all day</span></h1>
</div></div>
</section>
'''
    h += marquee(['Lasts all day', 'Bridal trial included', 'English-speaking', 'Destination weddings', 'Bride, bridesmaids &amp; mother'])
    h += intro('About the service', 'Your bridal look, exactly as you imagined', 'beautiful, camera-ready and uniquely yours',
               [('wedding-2', 'Bridal makeup Prague – bride and bridesmaids'), ('wedding-4', 'Bridal makeup – bride and groom')],
               "As a professional <b>wedding makeup artist based in Prague</b>, I work with brides to create looks that are beautiful, camera-ready, and – most importantly – uniquely theirs. Whether you are getting married in Prague's Old Town, a château outside the city, or planning a destination wedding anywhere in Europe, I will travel to you. Every bridal service begins with a detailed consultation about your vision, skin type, dress and wedding aesthetic. A <b>bridal trial</b> is included in every wedding package so you arrive on your wedding day fully confident.",
               ['English-speaking – ideal for international &amp; expat brides', 'Bridal trial included in every wedding package', 'Bride, bridesmaids &amp; mother of the bride', 'Destination weddings across Czech Republic &amp; Europe'],
               (CAL, 'Book your bridal consultation +'))
    h += checker('What sets the experience apart', 'why brides choose Nikol', [
        ('img', 'wedding-15', 'Bridal look – soft glam'),
        ('panel', '01', 'English-speaking MUA', 'Fluent in English, Czech and Ukrainian – no communication barriers for international brides or destination weddings in Prague.', False),
        ('img', 'wedding-3', 'Bridal look – long-lasting makeup'),
        ('panel', '02', 'Bridal trial included', 'Every wedding package includes a dedicated trial session so you refine your look and arrive on the day with complete confidence.', True),
        ('panel', '03', 'Destination weddings', 'Available throughout the Czech Republic and across Europe – I come to your venue, hotel or location of choice.', True),
        ('img', 'wedding-6', 'Bridal look – romantic styling'),
        ('panel', '04', 'Long-lasting finish', 'Professional products and techniques keep your bridal look fresh and photo-ready from the ceremony to the last dance.', False),
        ('img', 'wedding-12', 'Bride and bridesmaids styling')])
    h += ox_pricing('Rates &amp; services', 'Wedding makeup packages', 'Pricing varies by date, location and scope. Personalised quote within 24 hours.', [
        ('Full bridal package', 'Request', ['Personalised Bridal Trial', 'Wedding-Day Application', 'False Lashes Included', 'Touch-Up Kit for the Day', 'Travel to Venue (Prague)'], 'Request a quote +'),
        ('Bridal party &amp; travel', 'Request', ['Bridesmaids Makeup', 'Mother of the Bride', 'Coordinated Party Look', 'Travel Across Czech Republic', 'European Destinations'], 'Request a quote +')])
    h += steps('The bridal process', 'how it works', [
        ('Initial consultation', 'We discuss your vision, dress and venue – in person, by phone or video call, convenient for international brides planning a destination wedding in Prague.'),
        ('Bridal trial session', 'Typically 4–8 weeks before the wedding. We test the full look, adjust colours and techniques, and finalise every detail with trial photos.'),
        ('Wedding morning makeup', "Nikol arrives at your hotel, venue or home. Bridal party makeup is scheduled first; the bride's look is applied last so it is freshest for the ceremony and photos."),
        ('Touch-up kit &amp; final check', 'You receive a personalised touch-up kit with the key products used on your skin, so your look stays perfect through to the last dance.')],
        'From your first consultation to the final touch-up on your wedding day – here is exactly what to expect when you book Nikol Pavlova as your wedding makeup artist in Prague.')
    h += gallery('Recent bridal looks', 'selected work', 'View full portfolio', '/en/portfolio/', [
        ('wedding-5', 'Bridal makeup look – soft bridal glow, Prague wedding'), ('wedding-7', 'Bridal makeup look – classic bridal beauty'),
        ('wedding-9', 'Bridal makeup look – Prague destination wedding'), ('wedding-11', 'Bridal makeup look – luminous wedding skin'),
        ('wedding-12', 'Bridal party makeup – bride and bridesmaids, Prague'), ('wedding-13', 'Bridal makeup look – natural bridal beauty'),
        ('wedding-14', 'Bridal makeup look – soft glam bridal, Prague'), ('wedding-15', 'Bridal makeup look by Nikol Pavlova, Prague')])
    h += reviews(LANG, 'brides &amp; wedding shoots', pick('shirley', 'polinashu', 'erika_w'), top=False)
    h += f'''<section class="sec" aria-labelledby="guide-h"><div class="wrap guide">
<aside><p class="lbl red">Bridal makeup guide</p><h2 class="big-h" id="guide-h">Wedding makeup in Prague</h2>
<nav class="toc" aria-label="Guide contents"><a href="#g1">What a bridal MUA offers</a><a href="#g2">How far in advance to book</a><a href="#g3">The bridal trial</a><a href="#g4">English-speaking MUA</a><a href="#g5">Bridal makeup styles</a></nav></aside>
<article>
<p class="opener">Choosing the right wedding makeup artist in Prague is one of the most important decisions a bride makes. Your makeup needs to photograph beautifully, last from morning through the reception, and most importantly – make you feel like yourself on your most significant day.</p>
<section id="g1"><h3>What does a bridal makeup artist in Prague offer?</h3><p class="body">A professional <b>bridal makeup artist in Prague</b> like Nikol Pavlova provides a full end-to-end service: an initial consultation to understand your vision and skin type, a <b>bridal trial</b> to perfect the look beforehand, and on-location application at your venue or accommodation on the wedding morning.</p></section>
<section id="g2"><h3>How far in advance should you book?</h3><p class="body">For <b>wedding makeup in Prague</b>, most artists book 6–12 months ahead, particularly for the peak season from May to September. Prague is one of Europe's most popular destination-wedding cities, so demand for English-speaking makeup artists is high in summer. Booking early secures your date and leaves time for the bridal trial.</p></section>
<section id="g3"><h3>What is a bridal trial and why does it matter?</h3><p class="body">A <b>bridal trial</b> is a full makeup rehearsal, usually 4–8 weeks before the wedding. You test foundation shade, eye look, lip colour and lashes, producing reference photos that guide the wedding-day application. Every wedding package with Nikol Pavlova includes a bridal trial as standard.</p></section>
<section id="g4"><h3>English-speaking wedding makeup artist in Prague</h3><p class="body">For international brides, expats and couples planning a <b>destination wedding in the Czech Republic</b>, working with an <b>English-speaking wedding makeup artist in Prague</b> removes a major source of stress. Nikol is fluent in English, Czech and Ukrainian – a natural choice for multicultural weddings and clients travelling from the UK, USA, Ireland, Australia and across Europe.</p></section>
<section id="g5"><h3>Bridal makeup styles available in Prague</h3>
<dl class="rows"><div><dt class="k">Soft bridal glow</dt><dd class="v">dewy, luminous skin with subtle eye definition</dd></div><div><dt class="k">Glamorous evening bridal</dt><dd class="v">full coverage, bold lashes, defined eyes</dd></div><div><dt class="k">Natural nude bridal</dt><dd class="v">skin-like coverage that enhances rather than transforms</dd></div><div><dt class="k">Old Hollywood bridal</dt><dd class="v">dramatic liner, red lip, flawless base</dd></div><div><dt class="k">Bohemian bridal</dt><dd class="v">warm tones, earthy palette, relaxed and romantic</dd></div></dl>
<p class="body" style="margin-top:16px">During your consultation, Nikol helps you choose the style that best suits your skin, dress, venue and wedding theme.</p></section>
</article></div></section>
'''
    h += faq(LANG, 'wedding makeup questions', faq_items)
    h += tiles(LANG, [('Evening makeup', '/en/evening-makeup/', 'evening-5'), ('Makeup courses', '/en/courses/', 'course')])
    h += footer(LANG, 'Book your bridal consultation', 'Get in touch', 'Based in Prague, Czech Republic · Available for travel across Europe. Personalised quote within 24 hours.', (CAL, 'Book your appointment online +'))
    write(path, h)


# ---------------------------------------------------------------- GENERIC SERVICE (EN)
def service(cfg):
    path = cfg['path']
    sch = S.service_page(LANG, path, cfg['title'], cfg['desc'], cfg['service_name'], cfg['service_type'],
                         f"/assets/img/{cfg['hero_img']}-800.webp", [('Home', '/en/'), ('Services', '/en/#services'), (cfg['crumb'], path)], cfg['faq'], cfg['offers'])
    h = head(LANG, cfg['title'], cfg['desc'], path, alts(cfg['cs'], path), SITE + f"/assets/img/{cfg['hero_img']}-800.webp", sch,
             preload(cfg['hero_img'], '(max-width: 900px) 100vw, 50vw'))
    h += header(LANG, path, cfg['cs'])
    h += hero_split(LANG, cfg['tone'], [HOME, SVC, (cfg['crumb'], None)], cfg['big'], cfg['sub'], cfg['lead'], cfg['buttons'], cfg['hero_img'], cfg['hero_alt'])
    h += marquee(cfg['marquee'])
    h += intro('About the service', cfg['intro_title'], cfg['intro_tag'], cfg['intro_imgs'], cfg['intro_body'], cfg['chips'])
    h += checker(cfg['grid_title'], cfg['grid_sub'], cfg['grid'])
    h += ox_pricing('Rates', cfg['price_title'], cfg['price_note'], [cfg['price_col']])
    h += steps(cfg['steps_title'], 'how it works', cfg['steps'])
    h += gallery(cfg['gal_title'], 'selected work', 'View full portfolio', '/en/portfolio/', cfg['gallery'], c3=len(cfg['gallery']) < 8)
    h += cfg.get('banner', '')
    h += reviews(LANG, cfg['rv_sub'], cfg['reviews'], top=False)
    h += faq(LANG, cfg['faq_sub'], cfg['faq'])
    h += tiles(LANG, cfg['related'])
    h += footer(LANG, cfg['f_label'], 'Get in touch', cfg['f_text'], cfg.get('f_primary'))
    write(path, h)


EVENING = dict(
    path='/en/evening-makeup/', cs='/vecerni-liceni/', crumb='Evening makeup', tone='tone-ox',
    title='Evening & Ball Makeup Prague | Cocktail Makeup – Nikol Pavlova',
    desc='Evening, cocktail and ball makeup in Prague. Glamorous looks for galas, proms and parties – smoky eyes, statement lips and makeup that lasts all night.',
    service_name='Evening makeup Prague', service_type='Evening and ball makeup',
    offers=['Cocktail Makeup', 'Evening Styling', 'Prom / Ball Makeup', 'Photo Shoots'],
    big='Evening<br>makeup', sub='in Prague – galas, balls &amp; parties',
    lead='Glamorous looks built for galas, cocktail parties, proms, balls and special events in Prague. Smoky eyes, sculpted cheekbones, statement lips and luminous skin – finished with techniques that hold up under both flash photography and ambient evening light.',
    buttons=[('Book appointment +', CAL), ('Makeup styles', '#grid-h')], hero_img='evening-5', hero_alt='Evening makeup Prague – elegant glamour look',
    marquee=['Balls', 'Galas', 'Cocktail parties', 'Proms', 'Smoky eyes', 'Statement lips'],
    intro_title='A bold look you feel confident in', intro_tag='from soft glam to dramatic smoky eyes',
    intro_imgs=[('evening-1', 'Evening look – glamour smoky eye'), ('evening-3', 'Evening look – bold lip and clean skin')],
    intro_body='Every evening look is tailored to your dress, hair, lighting and the character of the event. We start with a quick chat about how bold you want to go. I come to your home, hotel or venue anywhere in Prague; travel outside Prague is available on request.',
    chips=['Balls, proms &amp; galas', 'Cocktail parties &amp; celebrations', 'Photo shoots', 'English &amp; Czech'],
    grid_title='Makeup styles', grid_sub='from soft glam to smoky eyes', grid=[
        ('img', 'evening-13', 'Soft glam evening look'), ('panel', '01', 'Soft glam', 'Luminous skin, softly defined eyes and an elegant, timeless finish.', False),
        ('img', 'evening-12', 'Dramatic eye styling'), ('panel', '02', 'Smoky eyes', 'Smoky eyes and dramatic eye styling for the big nights.', True),
        ('panel', '03', 'Statement lips', 'Clean skin with a bold lip as the focus of the whole look.', True), ('img', 'evening-16', 'Sculpted contour and lips'),
        ('panel', '04', 'Prom &amp; ball', 'Prom and ball styling that lasts all night and in every photo.', False), ('img', 'evening-4', 'Prom and ball styling')],
    price_title='Special occasions', price_note='Prices depend on the type of service, location and timing. Send me your event details and I will reply with a personalised quote within 24 hours.',
    price_col=('Evening &amp; events', 'Request', ['Cocktail Makeup', 'Evening Styling', 'Prom / Ball Makeup', 'Photo Shoots'], 'Request a quote +'),
    steps_title='How evening makeup works', steps=[
        ('Enquiry', 'Send me the date, location and type of event – by phone, text, email or Instagram. I usually reply within a few hours.'),
        ('Quote &amp; look', 'You receive a personal quote within 24 hours. We talk about your dress, hair and how bold you want to go.'),
        ('Application', 'At your home, hotel or venue – with long-wear products that last all evening.'),
        ('Final check', 'Last touches before you leave, plus tips on refreshing your look during the night.')],
    gal_title='Evening looks', gallery=[('evening-6', 'Evening look – seductive eye makeup'), ('evening-7', 'Evening look – radiant evening glam'),
        ('evening-10', 'Evening look – classic evening glam'), ('evening-8', 'Evening look – bold colourful eye'),
        ('evening-11', 'Evening look – gala makeup'), ('evening-15', 'Evening look – radiant evening face'),
        ('evening-14', 'Evening look – modern evening styling'), ('evening-17', 'Evening look – finishing touch')],
    rv_sub='makeup that lasts into the night', reviews=pick('nelli', 'stepanka', 'glenn'),
    faq_sub='evening makeup questions', faq=[
        ('How far in advance should I book?', 'For evening makeup and shoots, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'),
        ('How much does evening makeup cost in Prague?', 'Prices depend on the type of service, location and timing. Send me your event details and I will reply with a personalised quote within 24 hours.'),
        ('Do you come to me?', 'Yes. I work across all districts of Prague – including Praha 1 (Old Town), Praha 2 (Vinohrady) and Praha 7 – and travel to other cities in the Czech Republic and across Europe.'),
        ('Do you speak English?', 'Yes, I speak fluent English and Czech, so international clients and expats in Prague are very welcome.'), BOOK_FAQ],
    related=[('Wedding makeup', '/en/wedding/', 'wedding-5'), ('Commercial makeup', '/en/commercial-makeup/', 'commercial-4')],
    f_label='Book your evening makeup', f_text='Based in Prague, Czech Republic · Available for travel. Personalised quote within 24 hours.')

NUDE = dict(
    path='/en/nude-makeup/', cs='/nude-liceni/', crumb='Nude makeup', tone='tone-blush',
    title='Natural Nude Makeup Prague | Makeup Artist Nikol Pavlova',
    desc='Natural nude makeup in Prague. Soft, skin-first looks for engagement shoots, portraits and civil ceremonies – healthy glowing skin without a heavy finish.',
    service_name='Nude makeup Prague', service_type='Natural makeup',
    offers=['Skin preparation', 'Light base &amp; concealer', 'Soft eye &amp; brow definition', 'Natural cheeks &amp; lips'],
    big='Nude<br>makeup', sub='in Prague – enhance, never transform',
    lead='Soft, skin-first looks that enhance natural features without looking heavy. Ideal for engagement shoots, daytime portraits, civil ceremonies and clients who prefer a barely-there finish with healthy glowing skin.',
    buttons=[('Book appointment +', CAL), ('Who it is for', '#grid-h')], hero_img='nude-1', hero_alt='Nude makeup Prague – natural no-makeup look',
    marquee=['No-makeup look', 'Healthy glow', 'Dewy skin', 'Engagement shoots', 'Civil ceremonies'],
    intro_title='Healthy, glowing skin and your own features', intro_tag='you, at your very best',
    intro_imgs=[('nude-2', 'Nude look – soft natural glow'), ('nude-3', 'Nude look – fresh dewy skin')],
    intro_body='A nude look starts with careful skin preparation and light layers of product that melt into the skin. I tailor the makeup to your skin type, tone and occasion, so the result looks fresh in photos and in person – from morning to evening.',
    chips=['Skin prep first', 'Light coverage, no mask effect', 'Softly defined eyes, brows &amp; lips', 'English &amp; Czech'],
    grid_title='Who it is for', grid_sub='when a nude look works best', grid=[
        ('panel', '01', 'Engagement shoots', 'A natural look that feels fresh and timeless in photos.', False), ('img', 'wedding-13', 'Natural bridal beauty'),
        ('panel', '02', 'Daytime portraits', 'Business, profile and personal portraits in daylight.', True), ('img', 'nude-3', 'Fresh dewy skin'),
        ('img', 'wedding-1', 'Soft bridal makeup'), ('panel', '03', 'Civil ceremonies', 'A soft bridal look for smaller and civil ceremonies.', True),
        ('img', 'nude-2', 'Soft natural glow'), ('panel', '04', 'Barely-there', 'Healthy glowing skin with a minimum of product.', False)],
    price_title='Natural look', price_note='Prices depend on the type of service, location and timing. Send me the details and I will reply with a personalised quote within 24 hours.',
    price_col=('Nude makeup', 'Request', ['Skin preparation', 'Light base &amp; concealer', 'Soft eye &amp; brow definition', 'Natural cheeks &amp; lips'], 'Request a quote +'),
    steps_title='How it works', steps=[
        ('Enquiry', 'Send me the date, location and occasion. I usually reply within a few hours.'),
        ('Skin prep', 'Every look starts with skincare tailored to your skin type.'),
        ('Light layers', 'Coverage only where needed and soft definition of your features.'),
        ('Final check', 'A daylight check so the look reads natural in person and on camera.')],
    gal_title='Natural looks', gallery=[('nude-1', 'Nude look – natural no-makeup look, Prague'), ('nude-2', 'Nude look – soft natural glow'), ('nude-3', 'Nude look – fresh dewy skin')],
    banner=f'''<section class="sec--tight" aria-label="Makeup courses"><div class="wrap"><a class="banner" href="/en/courses/"><span class="txt"><span class="lbl pink">Makeup courses</span><span class="mid-h">Want to learn the natural look yourself?</span><span class="serif" style="font-size:20px;color:#E9DCD8">In a one-on-one lesson we cover skin prep, colour theory and technique on your own face.</span><span class="btn btn--pink">Makeup courses →</span></span><span class="img">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}</span></a></div></section>
''',
    rv_sub='natural, fresh skin', reviews=pick('karin', 'marie', 'beata'),
    faq_sub='nude makeup questions', faq=[
        ('Does a nude look work for a wedding?', 'Yes. Natural nude is one of the bridal styles I offer – ideal for civil ceremonies and brides who want to look like themselves. See <a href="/en/wedding/">Wedding makeup</a>.'),
        ('How much does nude makeup cost?', 'Prices depend on the type of service, location and timing. Send me the details and I will reply with a personalised quote within 24 hours.'),
        ('How far in advance should I book?', 'For shoots and everyday events, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'), BOOK_FAQ],
    related=[('Wedding makeup', '/en/wedding/', 'wedding-5'), ('Evening makeup', '/en/evening-makeup/', 'evening-5')],
    f_label='Book your nude makeup', f_text='Based in Prague, Czech Republic · Available for travel. Personalised quote within 24 hours.')

COMMERCIAL = dict(
    path='/en/commercial-makeup/', cs='/komercni-liceni/', crumb='Commercial makeup', tone='tone-ink',
    title='Commercial & Editorial Makeup Artist Prague | Nikol Pavlova',
    desc='Commercial and editorial makeup in Prague for photo shoots, campaigns, lookbooks and video. Makeup adapted to light and concept, with on-set touch-ups all day.',
    service_name='Commercial and editorial makeup Prague', service_type='Makeup for photo shoots and advertising',
    offers=['Concept &amp; look consultation', 'Makeup for light &amp; brief', 'On-set touch-ups', 'Travel across Czechia &amp; Europe'],
    big='Commercial<br>makeup', sub='in Prague – shoots, campaigns &amp; editorial',
    lead='Makeup for photo shoots, brand campaigns, lookbooks, magazine editorials and video content. Adapted to the lighting and concept of each shoot – from clean beauty work to bold editorial styling – with on-set touch-ups across the production day.',
    buttons=[('Send a brief +', f'mailto:{MAIL}'), ('Project types', '#grid-h')], hero_img='commercial-4', hero_alt='Commercial makeup – beauty brand shoot',
    marquee=['Beauty', 'Campaigns', 'Lookbooks', 'Editorial', 'Video content', 'On-set touch-ups'],
    intro_title='Makeup that works on camera', intro_tag='from clean beauty to bold editorial',
    intro_imgs=[('commercial-2', 'Commercial look – campaign shoot'), ('commercial-3', 'Commercial look – magazine editorial styling')],
    intro_body='I work on shoots in Prague and beyond. Before the shoot we go through the concept, lighting and number of looks, so the makeup matches the brief and lasts the whole production day. I stay on set for touch-ups, so every frame looks as clean as the first.',
    chips=['Adapted to light &amp; concept', 'On-set touch-ups all day', 'Travel across Czechia &amp; Europe', 'English &amp; Czech'],
    grid_title='Project types', grid_sub='what I work on', grid=[
        ('img', 'commercial-1', 'Editorial shoot'), ('panel', '01', 'Beauty &amp; campaigns', 'Clean beauty work and brand campaigns for cosmetics and fashion labels.', False),
        ('img', 'commercial-3', 'Magazine editorial'), ('panel', '02', 'Editorial', 'Magazine editorials and bold, concept-led styling.', True),
        ('panel', '03', 'Lookbooks', 'Consistent looks for lookbooks and fashion collections.', True), ('img', 'commercial-5', 'Fashion editorial makeup'),
        ('panel', '04', 'Video content', 'Makeup for video and high-resolution content.', False), ('img', 'commercial-6', 'Media shoot')],
    price_title='Commercial projects', price_note='Commercial projects are priced individually by scope, location and date. Send me the shoot details and I will reply with a quote within 24 hours.',
    price_col=('Shoots &amp; production', 'Request', ['Concept &amp; look consultation', 'Makeup for light &amp; brief', 'On-set touch-ups', 'Travel across Czechia &amp; Europe'], 'Request a quote +'),
    steps_title='How we work together', steps=[
        ('Brief', 'Send me the date, location, concept and number of looks. I usually reply within a few hours.'),
        ('Quote &amp; prep', 'You receive a quote within 24 hours and I prepare looks for the concept and light.'),
        ('Shoot day', 'Makeup on set and look changes following the production schedule.'),
        ('On-set touch-ups', 'Ongoing checks and touch-ups so the makeup looks perfect in every frame.')],
    gal_title='Commercial looks', gallery=[('commercial-1', 'Commercial look – editorial shoot, Prague'), ('commercial-2', 'Commercial look – campaign shoot'),
        ('commercial-3', 'Commercial look – magazine editorial styling'), ('commercial-4', 'Commercial look – beauty brand shoot'),
        ('commercial-5', 'Commercial look – fashion editorial'), ('commercial-6', 'Commercial look – media shoot')],
    rv_sub='shoots &amp; modelling', reviews=pick('polina', 'zoe_c', 'glenn'),
    faq_sub='commercial makeup questions', faq=[
        ('How much does commercial makeup cost?', 'Commercial projects are priced individually by type of service, location and date. Send me the details and I will reply with a personalised quote within 24 hours.'),
        ('How far in advance should I book a shoot?', 'For shoots, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'),
        ('Do you travel for shoots outside Prague?', 'Yes. I am based in Prague and travel for shoots to other cities in the Czech Republic and across Europe.'),
        ('Do you work in English?', 'Yes, I speak fluent English and Czech, so international teams are very welcome.'), BOOK_FAQ],
    related=[('Evening makeup', '/en/evening-makeup/', 'evening-5'), ('Nude makeup', '/en/nude-makeup/', 'nude-1')],
    f_label='Planning a shoot?', f_text='Send me the date, location and concept – personalised quote within 24 hours.', f_primary=(f'mailto:{MAIL}', 'Send a brief by email +'))


# ---------------------------------------------------------------- COURSES
def courses():
    path = '/en/courses/'
    title = 'Makeup Course Prague | 1-on-1 Makeup Classes – Nikol Pavlova'
    desc = 'Personalised makeup courses in Prague with professional MUA Nikol Pavlova. One-on-one makeup lessons for beginners and aspiring makeup artists – skin prep, colour theory, techniques. Book online.'
    faq_items = [
        ('Who are the makeup courses suitable for?', 'The courses suit everyone – complete beginners learning everyday makeup for themselves, people preparing for a special occasion, and aspiring makeup artists building professional skills. Each course is personalised to your level and goals.'),
        ('What does a makeup course cover?', 'One-on-one sessions cover skin preparation, colour theory, foundation and base, eye makeup and lashes, contour and highlight, plus tool and product selection. We work on your own face so you can repeat the looks at home.'),
        ('Are lessons one-on-one or in a group?', 'Lessons are personalised one-on-one sessions, so the full session focuses entirely on you. Small private group sessions can be arranged on request.'),
        ('Do I need to bring my own products?', 'You can bring your existing products so we work with what you own and recommend improvements, or use professional products during the lesson. Afterwards you receive a personalised product and tool list.'),
        ('How long is a makeup course and what does it cost?', "Length and price depend on your level and goals – from a single focused lesson to a fuller programme. Tell Nikol what you'd like to learn and she'll send a personalised quote within 24 hours."),
        ('Are the courses available in English?', 'Yes. Nikol teaches in fluent English and Czech, making the courses comfortable for international clients and expats living in Prague.'),
        ('How do I book a makeup course in Prague?', f'Book online via <a href="{CAL}">Calendly</a>, or contact Nikol by phone/text <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a>, or Instagram <a href="{IG}">@nikol__mua</a>.'),
    ]
    h = head(LANG, title, desc, path, alts('/kurzy-liceni/', path), SITE + '/img/courses/IMG_7417.jpg', S.load('en-courses'), preload('course', '(max-width: 900px) 100vw, 50vw'))
    h += header(LANG, path, '/kurzy-liceni/')
    h += hero_split(LANG, 'tone-sand', [HOME, SVC, ('Makeup courses', None)], 'Makeup<br>courses', 'in Prague – learn to create your own looks',
                    'Personalised one-on-one makeup lessons in Prague – whether you want to master everyday makeup for yourself or build professional skills as an aspiring makeup artist. We work on your own face, at your own pace.',
                    [('Book a course online +', CAL), ('Course options', '#packages')], 'course', 'One-on-one makeup course in Prague with Nikol Pavlova', '50% 15%')
    h += marquee(['One-on-one', 'On your own face', 'English &amp; Czech', 'Beginners &amp; aspiring MUAs', 'Product list to take home'])
    h += intro('About the course', 'Makeup lessons tailored entirely to you', 'no fixed script, just what you want to learn', [],
               'As a professional <b>makeup artist and instructor in Prague</b>, I teach personalised one-on-one <b>makeup courses</b> built around your level and goals. There is no fixed script – we focus on exactly what you want to learn, using your own face as the canvas so you can recreate every look at home. Whether you have never held a brush or you are an aspiring MUA refining professional technique, every lesson is hands-on, relaxed and practical – and you leave with a personalised product and tool list.',
               ['One-on-one – the whole session is about you', 'Beginners and aspiring professionals welcome', 'Taught in English &amp; Czech', 'Personalised product &amp; tool list to take home'],
               (CAL, 'Book your lesson +'))
    h += checker("What you'll learn", 'the curriculum', [
        ('img', 'nude-1', 'Natural everyday makeup'), ('panel', '01', 'Skin prep &amp; base', 'Skincare prep, priming and flawless foundation, concealer and base techniques for your skin type.', False),
        ('img', 'nude-2', 'Soft natural glow'), ('panel', '02', 'Colour theory', 'Face mapping and colour theory so you choose shades that flatter your features and tone.', True),
        ('panel', '03', 'Eyes &amp; lashes', 'Eyeshadow blending, liner, and false-lash application – from soft daytime to defined evening looks.', True), ('img', 'evening-7', 'Defined eye makeup'),
        ('panel', '04', 'Tools &amp; products', 'Contour, blush and highlight, plus how to choose the right brushes and build your own makeup kit.', False), ('img', 'evening-5', 'Evening glam look')])
    h += ox_pricing('Course options', 'Choose your course', "Course length and price are tailored to your level and goals. Personalised quote within 24 hours.", [
        ('Personal makeup lesson', 'Request', ['Learn Everyday Self-Makeup', 'Skin Prep &amp; Base', 'Eyes, Lashes &amp; Finish', 'Personalised Product List', 'One-on-One in Prague'], 'Request a course +'),
        ('Pro / aspiring MUA course', 'Request', ['Professional Techniques', 'Colour Theory &amp; Face Mapping', 'Hygiene &amp; Kit Building', 'Working on Clients', 'Tailored to Your Goals'], 'Request a course +')])
    h += steps('How the course runs', 'how it works', [
        ('Goal-setting chat', 'We discuss your level, what you want to learn and the looks you love – in person, by phone or video call for international students.'),
        ('Personalised plan', 'I prepare a lesson plan around your goals, skin type and the products you already own, so every minute is relevant to you.'),
        ('Hands-on session', 'We work step by step on your own face. You do the application with guidance, so the techniques truly stick.'),
        ('Product list &amp; follow-up', 'You leave with a personalised product and tool list and notes, so you can confidently recreate everything at home.')],
        'Each makeup course in Prague is built around you. Here is what to expect from first message to follow-up.')
    h += f'''<section class="sec--tight" aria-labelledby="insp-h"><div class="wrap">
{sec_head('Looks you can learn to create', 'inspiration', '<a class="link-arrow" href="/en/portfolio/">View full portfolio →</a>', hid='insp-h')}
<ul class="cards3" role="list" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))">
<li><figure class="pcard"><div class="ph">{I('nude-1', 'Natural everyday makeup look taught in Prague makeup course')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Natural daytime look</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('nude-2', 'Soft natural glow makeup technique, Prague lesson')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Soft glow</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-5', 'Evening glam makeup look taught in Prague course')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Evening glam</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-7', 'Defined eye makeup technique, Prague makeup lesson')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Defined eyes</figcaption></figure></li>
</ul></div></section>
<section class="sec sec--blush" aria-labelledby="students-h"><div class="wrap">
{sec_head('Happy students', 'what they say about the lessons', f'<a class="btn" href="{CAL}">Book your lesson +</a>', hid='students-h')}
<div class="quotes3">
<figure><blockquote><p>“I finally understand how to do my own makeup. Nikol explained everything so clearly and let me do it myself – now I actually use these techniques every day.”</p></blockquote><figcaption class="lbl"><cite>Tereza H.</cite> <span class="muted2">· Personal lesson</span></figcaption></figure>
<figure><blockquote><p>“As someone starting out as an MUA, the pro session was exactly what I needed – real technique, hygiene and product advice you can't get from videos.”</p></blockquote><figcaption class="lbl"><cite>Marta S.</cite> <span class="muted2">· Pro course</span></figcaption></figure>
<figure><blockquote><p>“Booked a lesson in English as an expat in Prague. Relaxed, personal and so practical – I left with a product list I actually use.”</p></blockquote><figcaption class="lbl"><cite>Olivia R.</cite> <span class="muted2">· Personal lesson</span></figcaption></figure>
</div></div></section>
<section class="sec" aria-labelledby="guide-h"><div class="wrap guide">
<aside><p class="lbl red">Makeup course guide</p><h2 class="big-h" id="guide-h">Makeup courses in Prague</h2></aside>
<article>
<p class="opener">Looking for a makeup course in Prague? Whether you want to finally master your own everyday look or take your first steps as a professional, a personalised one-on-one lesson is the fastest way to learn techniques that actually work for your face.</p>
<section><h3>Who are makeup classes in Prague for?</h3><p class="body">Makeup classes suit complete beginners, anyone preparing for a special occasion, and aspiring makeup artists. Because lessons are one-on-one, the content is adapted to your level – nobody is left behind and nobody is bored.</p></section>
<section><h3>What does a makeup lesson cover?</h3><p class="body">A typical <b>makeup lesson</b> covers skin preparation, colour theory and face mapping, foundation and base, eye makeup and lashes, contour and highlight, and how to choose the right tools and products. You apply the makeup yourself, with guidance, so the skills stay with you.</p></section>
<section><h3>One-on-one vs group makeup classes</h3><p class="body">Group classes can be fun, but a <b>one-on-one makeup lesson</b> means the entire session is built around your features, skin type and goals. For most people learning faster and remembering more, private lessons are the better value.</p></section>
<section><h3>English-speaking makeup courses in Prague</h3><p class="body">For expats and international clients, learning in your own language matters. Nikol teaches in fluent <b>English and Czech</b>, so every step is clear and you can ask anything along the way.</p></section>
<section><h3>What you'll be able to do afterwards</h3><dl class="rows"><div><dt class="k">Everyday makeup</dt><dd class="v">a quick, flattering look you can do confidently</dd></div><div><dt class="k">Occasion makeup</dt><dd class="v">a polished look for events, dates and photos</dd></div><div><dt class="k">Professional technique</dt><dd class="v">foundations for working as an MUA</dd></div><div><dt class="k">Smart shopping</dt><dd class="v">a product and tool list tailored to you</dd></div></dl>
<p class="body" style="margin-top:16px">Tell Nikol what you want to achieve and she'll shape the course around it – from a single focused session to a fuller programme.</p></section>
</article></div></section>
'''
    h += faq(LANG, 'makeup course questions', faq_items)
    h += tiles(LANG, [('Wedding makeup', '/en/wedding/', 'wedding-5'), ('Nude makeup', '/en/nude-makeup/', 'nude-1')])
    h += footer(LANG, 'Book your makeup course', 'Get in touch', 'Lessons held in Prague, Czech Republic · In English or Czech. Personalised quote within 24 hours.', (CAL, 'Book your course online +'))
    write(path, h)


# ---------------------------------------------------------------- PORTFOLIO
EN_ITEMS = {
    'wedding': ('Wedding', 'Bridal look', ['soft glam bridal makeup, Prague', 'natural radiant bridal makeup, Prague', 'long-lasting bridal makeup', 'elegant wedding-day makeup', 'soft bridal glow, Prague wedding', 'romantic bridal styling', 'classic bridal beauty', 'modern bridal makeup', 'destination wedding in Prague', 'bridal trial result', 'luminous wedding skin', 'bride and bridesmaids styling', 'natural bridal beauty', 'soft glam bridal makeup', 'bridal makeup by Nikol Pavlova']),
    'evening': ('Evening', 'Evening look', ['glamour smoky eye, Prague', 'cocktail styling', 'bold lip and clean skin', 'prom and ball styling', 'elegant evening glam', 'seductive eye makeup', 'radiant evening glam', 'bold colourful eye', 'special occasion makeup', 'classic evening glam', 'gala makeup', 'dramatic eye styling', 'soft glam evening look', 'modern evening styling', 'radiant evening face', 'sculpted contour and lips', 'evening glam finishing touch']),
    'nude': ('Nude', 'Nude look', ['natural no-makeup look, Prague', 'soft natural glow', 'fresh dewy skin']),
    'commercial': ('Commercial', 'Commercial look', ['editorial shoot, Prague', 'campaign shoot', 'magazine editorial styling', 'beauty brand shoot', 'fashion editorial makeup', 'high-resolution media shoot']),
    'courses': ('Courses', 'Makeup course', ['one-on-one lesson in Prague']),
}


def portfolio():
    path = '/en/portfolio/'
    title = 'Makeup Portfolio Prague – Bridal, Evening & Commercial Looks | Nikol Pavlova'
    desc = 'Portfolio of Nikol Pavlova, professional makeup artist in Prague. Browse bridal, evening, nude, commercial and editorial makeup looks for clients in the Czech Republic and Europe.'
    total = sum(len(v[2]) for v in (PORTFOLIO_ITEMS if LANG == 'cs' else EN_ITEMS).values())
    pills, figs = portfolio_grid(LANG, EN_ITEMS, 'All', '', '')
    h = head(LANG, title, desc, path, alts('/portfolio/', path), SITE + '/img/wedding/wedding-1.png', S.load('en-portfolio'), extra=NOSCRIPT)
    h += header(LANG, 'portfolio', '/portfolio/')
    h += f'''<section class="page-head" aria-labelledby="page-h1"><div class="wrap">
{crumbs(LANG, [HOME, ('Portfolio', None)])}
<div class="top"><h1 class="h1" id="page-h1"><span class="big wide">Portfolio</span><span class="sub serif">makeup – Nikol Pavlova, makeup artist Prague</span></h1>
<p class="body">This is a curated selection of makeup work created by <b>Nikol Pavlova</b>, a professional makeup artist based in <b>Prague, Czech Republic</b>. The portfolio covers bridal looks for weddings across Prague and Europe, glamorous evening and cocktail makeup, soft natural nude styling, commercial and editorial work for photo shoots, and behind-the-scenes images from one-on-one makeup courses. Each look is designed to enhance the client's natural features while reflecting their personal style and the occasion.</p></div>
</div></section>
<section class="sec--tight" aria-labelledby="looks-h">
<div class="wrap">{sec_head('Choose a look', 'browse by category', f'<div class="filters" role="group" aria-label="Category">{pills}</div>', hid='looks-h')}</div>
<div class="pgrid" data-portfolio data-label-shown="Showing {{n}} of {{t}}" data-label-more="Show more ({{n}}) ↓" aria-live="polite">{figs}</div>
<div class="more-wrap"><p class="serif muted2" data-status>Showing {min(16, total)} of {total}</p><button class="pill btn--lg" type="button" data-more>Show more ({max(0, total - 16)}) ↓</button></div>
</section>
<section class="sec sec--blush" aria-labelledby="cats-h"><div class="wrap">
{sec_head('About each category', 'inside the portfolio', hid='cats-h')}
<div class="cat-rows">
<a href="/en/wedding/"><h3>Wedding makeup →</h3><p>Bridal looks designed to last from the first kiss to the final dance. Each wedding service includes a pre-wedding trial in Prague, day-of application with long-wear products suited to Czech summer and winter conditions, individual lashes, and a personal touch-up kit. Available for ceremonies in Prague Old Town, Vinohrady, château weddings outside the city, and destination weddings across Europe.</p></a>
<a href="/en/evening-makeup/"><h3>Evening &amp; cocktail makeup →</h3><p>Glamorous looks built for galas, cocktail parties, proms, balls and special events in Prague. Smoky eyes, sculpted cheekbones, statement lips and luminous skin – finished with techniques that hold up under both flash photography and ambient evening light.</p></a>
<a href="/en/nude-makeup/"><h3>Nude &amp; natural makeup →</h3><p>Soft, skin-first looks that enhance natural features without looking heavy. Ideal for engagement shoots, daytime portraits, civil ceremonies and clients who prefer a barely-there finish with healthy glowing skin.</p></a>
<a href="/en/commercial-makeup/"><h3>Commercial &amp; editorial →</h3><p>Makeup for photo shoots, brand campaigns, lookbooks, magazine editorials and video content. Adapted to the lighting and concept of each shoot – from clean beauty work to bold editorial styling – with on-set touch-ups across the production day.</p></a>
<a href="/en/courses/"><h3>Personalized makeup courses →</h3><p>One-on-one makeup courses tailored to your level – from clients who want to master everyday looks to aspiring makeup artists building professional skills. Held in Prague, covering skin prep, color theory, application techniques, tool selection and product recommendations using your own face as the canvas.</p></a>
</div></div></section>
<section class="sec sec--ox" aria-labelledby="like-h"><div class="wrap ox-split" style="align-items:end">
<div style="display:flex;flex-direction:column;gap:22px"><p class="lbl pink">Like what you see?</p><h2 class="big-h" id="like-h">Let's create your own makeup look</h2><p class="serif ox-note">Get in touch to discuss your wedding, event or shoot. I'll send a personalized quote and availability within 24 hours.</p>
<p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn--pink" href="{CAL}">Book online +</a><a class="btn btn--ghost" href="mailto:{MAIL}">{MAIL}</a></p></div>
<dl class="kv"><div><dt class="lbl">Location</dt><dd>Prague, Czech Republic</dd></div><div><dt class="lbl">Phone</dt><dd><a href="tel:{TEL}">{TEL_H}</a></dd></div><div><dt class="lbl">Instagram</dt><dd><a href="{IG}">@nikol__mua</a></dd></div><div><dt class="lbl">Travel</dt><dd>Czechia &amp; Europe</dd></div></dl>
</div></section>
'''
    h += footer(LANG, 'Contact me', 'Do you need help with creative make-up?', "Get in touch to plan your look – I'll reply within 24 hours.")
    write(path, h)


# ---------------------------------------------------------------- BLOG
def blog():
    path = '/en/blog/'
    title = 'Blog – Makeup Reviews, Tips & Tutorials | Nikol Pavlova, Prague'
    desc = 'Honest makeup reviews, professional tips and tutorials from Nikol Pavlova, an English-speaking makeup artist based in Prague.'
    h = head(LANG, title, desc, path, [('en', path)], SITE + '/img/nikol.jpg', S.load('en-blog'))
    h += header(LANG, 'blog', '/')
    h += f'''<section class="page-head" aria-labelledby="page-h1"><div class="wrap">
{crumbs(LANG, [HOME, ('Blog', None)])}
<div class="top"><h1 class="h1" id="page-h1"><span class="big wide">The Blog</span><span class="sub serif">– makeup reviews, tips &amp; tutorials from Prague</span></h1>
<p class="body">Honest product reviews, professional tips and behind-the-scenes notes from my work as a makeup artist in Prague – written to help you choose better products and create looks that suit you.</p></div>
</div></section>
<section class="sec--tight" aria-labelledby="latest-h"><div class="wrap">
<h2 class="visually-hidden" id="latest-h">Latest review</h2>
<article><a class="feat" href="/en/blog/full-face-of-nyx-review/">{I('nikol-hero', 'Nikol Pavlova testing a full face of NYX makeup', sizes='(max-width: 900px) 100vw, 1280px')}<span class="badge lbl glass">Latest review</span>
<div class="card glass"><p class="lbl muted" style="display:flex;gap:14px;flex-wrap:wrap"><span class="red">Reviews</span><time datetime="2026-03-20">20 March 2026</time><span>9 min read</span></p>
<h3 class="wide" style="font-size:30px;font-weight:500;line-height:1.1">Full Face of NYX: A Makeup Artist's Honest Review</h3>
<p style="color:var(--text)">I tested a full face of NYX – bestsellers and a few brand-new launches – then wore it through a real working day. Here is what earned a place in my kit, what depends on your skin type, and what I would happily skip, plus an honest all-day wear test.</p>
<span class="btn" style="align-self:flex-start">Read the review →</span></div></a></article>
</div></section>
<section class="sec sec--blush" aria-labelledby="topics-h"><div class="wrap">
{sec_head('Topics', 'what I write about', hid='topics-h')}
<ul class="topic-rows">
<li><h3>Product reviews</h3><p>Honest, hands-on takes on the products I test – what is worth it and what is not.</p><span class="lbl red">1 article</span></li>
<li><h3>Pro tips &amp; tutorials</h3><p>Techniques from my kit – skin prep, longevity, colour and application made simple.</p><span class="lbl muted2">Coming soon</span></li>
<li><h3>Bridal &amp; events</h3><p>How to plan and prepare for long-lasting makeup on the days that matter most.</p><span class="lbl muted2">Coming soon</span></li>
</ul></div></section>
<section class="duo" aria-label="Book or learn">
<div class="ox-box"><p class="lbl pink">Need help?</p><h2 class="big-h">Do you need help with creative make-up?</h2><a class="btn btn--pink" href="{CAL}">Book online +</a></div>
<div class="tiles" style="display:block"><a href="/en/courses/" style="height:100%;min-height:420px">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}<span class="cap"><span class="lbl pink">Learn with me</span><span class="wide" style="font-size:clamp(24px,2.6vw,34px)">Personalised one-on-one makeup courses in Prague →</span></span></a></div>
</section>
'''
    h += footer(LANG, 'Contact me', 'Do you need help with creative make-up?', 'Professional makeup artist based in Prague. Designing bespoke beauty looks that reflect your distinct personality.')
    write(path, h)


def post():
    path = '/en/blog/full-face-of-nyx-review/'
    title = "Full Face of NYX: A Makeup Artist's Honest Review | Nikol Pavlova"
    desc = 'Prague makeup artist Nikol Pavlova tests a full face of NYX – primer, concealer, brows, bronzer, eyeshadow, liner, mascara and setting spray – with an honest all-day wear test.'
    faqs = [
        ('Do professional makeup artists really use drugstore brands like NYX?', 'Absolutely. A working kit is a mix of price points – what matters is how a product performs, not its label. Several NYX products, including the bronzer, powder, mascara and long-wear liner, hold their own next to far pricier options.'),
        ('What were the best NYX products in this test?', 'The cult bronzer, the pressed powder, the brow glue, the mascara, the long-wear eyeliner, and the concealer for targeted spot coverage.'),
        ('Is NYX makeup good enough for a wedding or a long event?', 'The long-wear pieces – powder, setting spray, locking liner and brow glue – can last impressively well. For your wedding day I would still recommend a professional application and a trial first. You can see what that involves on my <a href="/en/wedding/">wedding makeup</a> page.'),
        ('Which NYX products should I be careful with?', 'The plumping primer can feel tight on dry or flaky skin, and the matte eyeshadows are lovely but lower in pigment – swatch them in store first.'),
        ('Can I learn to create a full-face look like this myself?', 'Yes – that is exactly what my <a href="/en/courses/">one-on-one makeup courses</a> are for, tailored to your skin type and goals, from everyday looks to professional techniques.'),
        ('Where are you based?', 'I am an English-speaking makeup artist based in Prague, and I travel across the Czech Republic and Europe for weddings, shoots and events. <a href="#contact">Get in touch here.</a>'),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary><h3>{q}</h3><span class="pm" aria-hidden="true">+</span></summary><div><p>{a_}</p></div></details>' for i, (q, a_) in enumerate(faqs))
    h = head(LANG, title, desc, path, [('en', path)], 'https://i.ytimg.com/vi/U89IYdxyJy4/maxresdefault.jpg', S.load('en-post'), preload('nikol-hero', '100vw'), og_type='article')
    h += header(LANG, 'blog', '/')
    h += f'''<article aria-labelledby="page-h1">
<header class="page-head post-head" style="padding-bottom:48px"><div class="wrap" style="display:flex;flex-direction:column;gap:28px">
{crumbs(LANG, [HOME, ('Blog', '/en/blog/'), ('Full Face of NYX', None)])}
<p class="lbl muted" style="display:flex;gap:18px;flex-wrap:wrap"><span class="red">Reviews</span><time datetime="2026-03-20">20 March 2026</time><span>9 min read</span></p>
<h1 class="wide big" id="page-h1" style="max-width:1180px">Full Face of NYX: A Makeup Artist's Honest Review</h1>
<div style="display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;border-top:1px solid var(--ink);padding-top:20px">
<p style="display:flex;align-items:center;gap:14px">{I('nikol-portrait', '', sizes='52px', style='width:52px;height:52px;border-radius:50%;object-fit:cover;object-position:50% 20%')}<span class="body">By <a rel="author" href="/en/#about"><b>Nikol Pavlova</b></a> <span class="serif" style="font-size:18px">– Professional Makeup Artist, Prague</span></span></p>
<a class="link-arrow" href="#verdict">Jump to the verdict ↓</a></div>
</div></header>
<a class="video" href="https://www.youtube.com/watch?v=U89IYdxyJy4">{I('nikol-hero', 'Video: Nikol Pavlova testing a full face of NYX makeup', sizes='100vw', priority=True)}<span class="play glass" aria-hidden="true"><svg width="34" height="34" viewBox="0 0 24 24" fill="#A8232F"><path d="M8 5l12 7-12 7z"/></svg></span><span class="lbl glass">Watch the full test on YouTube · spoken in Ukrainian</span></a>
<div class="sec"><div class="wrap post-layout">
<aside class="post-toc"><p class="lbl red">In this review</p><nav class="toc" aria-label="Contents" style="border-top:1px solid var(--ink)"><a href="#verdict">The verdict at a glance</a><a href="#primer">Skin prep</a><a href="#concealer">Complexion</a><a href="#brows">Brows</a><a href="#bronzer">Warmth</a><a href="#powder">Setting the base</a><a href="#eyes">Eyes</a><a href="#lips">Lips</a><a href="#spray">The finish</a><a href="#wear">A full day of wear</a><a href="#worth">Is it worth it?</a><a href="#lessons">Three lessons</a><a href="#faq">FAQ</a></nav></aside>
<div class="art">
<p class="opener">NYX has always sat in an interesting spot for me. It is no longer truly cheap, yet it never pretends to be luxury either – and that quiet confidence is exactly why it holds one of the most stable reputations in the drugstore world. So I put it to the test the only way that really counts: a full face, start to finish, using nothing but NYX.</p>
<p>Bestsellers, a few brand-new launches I had been dying to try, and – most importantly – an honest wear test at the end of the day. Below is everything that earned its place in my kit, and everything I would happily leave on the shelf.</p>
<p style="font-size:15px;color:var(--muted2)">Watch the full test on my channel (spoken in Ukrainian). The written breakdown, verdicts and all-day wear test are below – no sound required.</p>
<aside class="note"><p class="lbl red">How I tested it</p><p>I applied a complete look on camera – from skin prep through to setting spray – then wore it through a full working day and checked it again that night, and once more the next day. For reference, my skin is normal-to-combination.</p></aside>
<h2 id="verdict">The verdict at a glance</h2>
<div class="verdict">
<div><p class="v v-yes">Worth buying</p><ul><li>The cult bronzer</li><li>Pressed powder</li><li>Brow glue</li><li>Mascara</li><li>Concealer (spot coverage)</li><li>Long-wear eyeliner*</li></ul></div>
<div><p class="v v-dep">Depends on your skin</p><ul><li>Plumping primer</li><li>Setting spray</li></ul></div>
<div><p class="v v-sw">Swatch first</p><ul><li>Matte eyeshadow palette</li><li>Warm lip liner</li></ul></div>
</div>
<p style="font-size:15px;color:var(--muted2)">*Brilliant longevity, but unforgiving – best for confident hands.</p>
<h2 id="primer">Skin prep: the plumping primer</h2><p class="v v-dep">Depends on skin type</p>
<p>This is the brand's hero of the moment – a light, gel-emulsion that promises to be serum and primer in one, with a pleasant, neutral scent. On me it turned tacky very quickly and the tight feeling only built through the day. That stickiness can actually help foundation grip, so I would happily recommend it for combination or oily skin – but on dry or flaky skin it will not smooth those dry patches, and the pulled feeling is not for everyone. Not quite the universal hero the label suggests.</p>
<h2 id="concealer">Complexion: the serum concealer</h2><p class="v v-yes">Worth it – for targeted coverage</p>
<p>Surprisingly dense and full-coverage for something sold as a "serum" concealer. It stays put, does not slide, and the slim tube means you will actually use every last drop. It leans slightly drying, and my shade ran a touch warmer than a true cool vanilla, so check your undertone. For targeted coverage it is excellent; over the whole face the usage adds up fast.</p>
<aside class="note"><p class="lbl red">Pro move</p><p class="serif" style="font-size:20px">Mix a little into your serum or moisturiser to turn it into a sheer tint.</p></aside>
<h2 id="brows">Brows: pencils, micro-liners &amp; the brow glue</h2><p class="v v-yes">Worth it – find your shade</p>
<p>The pencils are genuinely good: consistent, easy to work with and very wearable. One thing to watch – a couple of the taupe-leaning shades can oxidise slightly green on me over time, so I have switched to the cooler blond shade, which also draws beautifully even over the brow glue. The glue itself gives serious, laminated hold, perfect if you love that brushed-up, locked-in look. I personally prefer a softer, more natural shape these days, so I used it with a lighter hand. Tip: set your brows <strong>before</strong> foundation for the cleanest finish.</p>
<h2 id="bronzer">Warmth: the cult bronzer (and a word on blush)</h2><p class="v v-yes">Worth it</p>
<p>A deserved classic. Only the warm shade was in stock, so my face ran a little golden – but the formula is the real story. It smells like a chocolate-vanilla dessert, it is not baked, and yet it still does not go patchy, which is rare at this price (un-baked budget bronzers usually streak no matter your technique). Around 10–15 €, easy top marks. I pressed it into place rather than buffing, because the skin underneath was a touch tacky.</p>
<aside class="note"><p class="lbl red">A pro note on hygiene</p><p>For blush I reached for a powder I have owned since long before I became a makeup artist – and that is something to flag, not to copy. Powders carry a period-after-opening for a reason. My honest advice as a professional is to respect those dates and replace anything well past them. Your skin will thank you.</p></aside>
<h2 id="powder">Setting the base: the pressed powder</h2><p class="v v-yes">Worth it</p>
<p>It lives up to the hype. It sets the base and controls shine without clinging to dry patches or exaggerating texture – the exact failure point of so many heavier budget powders. One of my favourite finds of the whole haul.</p>
<h2 id="eyes">Eyes: palette, liner &amp; mascara</h2>
<h3>The matte eyeshadow palette</h3><p class="v v-sw">Swatch first</p>
<p>A very on-trend warm-neutral palette with a few cooler, pinky tones. The shades are pretty, but pigmentation sits on the softer side – especially layered over powder, which sheered them further. The look still came together nicely; next time I would skip powdering the lid first.</p>
<h3>The eyeliner</h3><p class="v v-yes">Worth it – for steady hands</p>
<p>Honestly, a wow. It is intensely long-wearing and does not budge or transfer once it sets – which is also the catch: there is almost no room for error, so it is not the most forgiving choice for beginners. I built a soft winged shape and loved how crisp it stayed all day.</p>
<h3>The mascara</h3><p class="v v-yes">Worth it</p>
<p>Fresh from the tube it applied cleanly with a classic brush, adding volume rather than just length – my preference. Pending a proper flake test over a few wears, this is one I would repurchase.</p>
<h2 id="lips">Lips: liner &amp; matte balm</h2><p class="v v-mix">Mixed</p>
<p>The lip liner is a long-standing favourite, though a reformulation made it noticeably warmer – it reads quite orange-warm on me now, so it suited today's warm look but will not be everyone's everyday. The matte "whip" balm gives a soft tint with a comfortable, slightly slippery feel and a lovely sweet scent; I also dabbed it on the cheeks as a quick cream blush to tie the whole look together.</p>
<h2 id="spray">The finish: setting spray</h2><p class="v v-dep">Depends on skin type</p>
<p>Last year's much-hyped spray (mine had settled, so it is clearly powder-infused – shake well). The applicator is punchy and it genuinely locks everything down. For a true matte finish it is great; on drier skin, combined with the primer, it was simply too much fixation for me.</p>
<h2 id="wear">The part that actually matters: a full day of wear</h2>
<p>Swatches and first impressions are easy. What separates a good product from a great one is how it looks after hours of real life, so here is the honest timeline.</p>
<dl class="timeline">
<div><dt>After 3–4 hours</dt><dd>The skin had picked up a natural sheen but still looked alive, nothing had creased under the eyes, and the brows held their shape.</dd></div>
<div><dt>End of the day</dt><dd>The complexion was shiny (which I do not mind), under-eyes stayed clean, the lip tint held on beautifully and the brows had softened only minimally. The honest downside: my skin felt tight all day – which I put down to the primer-plus-setting-spray combination being too much fixation for my normal-combination skin.</dd></div>
<div><dt>Day two</dt><dd>I re-tested just the concealer and powder over my own usual skin prep and foundation. The verdict: barely moved after five hours. That told me the concealer and powder are genuinely excellent – the tight, dry feeling was the primer, not the base.</dd></div>
</dl>
<h2 id="worth">So, is a full face of NYX worth it?</h2>
<p>NYX is exactly what its reputation suggests – a confident, dependable brand that has quietly graduated from pure drugstore into the lower mid-range. The pieces I would happily keep in a working kit: the bronzer, the pressed powder, the brow glue, the mascara, the long-wear liner (for confident hands) and the concealer for targeted coverage. The plumping primer and setting spray are skin-type dependent – wonderful for combination and oily skin, a lot for dry skin. The matte palette is pretty but worth swatching for pigment first. Match the right pieces to your skin, and NYX absolutely earns its place.</p>
<h2 id="lessons">Three things this look can teach you about your own makeup</h2>
<ol class="lessons">
<li><span class="n" aria-hidden="true">1</span><div><p><strong>A product is only as good as its fit for your skin.</strong></p><p style="font-size:16px">My primer struggle was not a "bad product" – it was the wrong product for my skin that day. Learning to read your own skin is half of great makeup.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><p><strong>Placement beats pigment.</strong></p><p style="font-size:16px">Whether you powder before shadow, press versus buff your bronzer, or sheer out a dense concealer – technique decides the result far more than price does.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><p><strong>Build for the day you will actually have.</strong></p><p style="font-size:16px">For events and weddings I lean on the long-wear pieces – powder, a locking liner, brow gel – and adjust fixation to the skin in front of me.</p></div></li>
</ol>
<aside class="note" style="flex-direction:row;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:20px"><div style="max-width:480px"><p class="wide" style="font-size:18px;font-weight:600">Want to learn this properly?</p><p>These are exactly the skills we work through, one-on-one, in my <a href="/en/courses/">personalised makeup courses</a> – using your own face, your own skin type, and products that genuinely suit you.</p></div><a class="btn" href="/en/courses/">View courses →</a></aside>
<section style="background:var(--ox);color:var(--paper);padding:44px;display:flex;flex-direction:column;gap:18px;margin-top:24px" aria-labelledby="cta-h">
<h2 id="cta-h" style="margin:0;padding:0;border:0;color:var(--paper)">Let's create your look</h2>
<p class="serif" style="font-size:20px;color:#F4D6CF">Whether you want flawless, long-lasting makeup for your wedding or a special event, or you would like to learn these techniques yourself, I would love to help.</p>
<p style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn--pink" style="color:var(--ox)" href="{CAL}">Book online +</a><a class="btn btn--ghost" style="color:#fff" href="/en/wedding/">Wedding makeup</a><a class="btn btn--ghost" style="color:#fff" href="/en/courses/">Makeup courses</a></p>
</section>
<h2 id="faq">Frequently asked questions</h2>
<div class="faq" style="border-top:0">{faq_html}</div>
<div class="author">{I('nikol-portrait', 'Nikol Pavlova, makeup artist in Prague', sizes='112px')}<div style="flex:1 1 300px;display:flex;flex-direction:column;gap:6px"><p class="wide" style="font-size:20px;font-weight:600">Nikol Pavlova</p><p class="serif muted2" style="font-size:18px">Makeup Artist · Prague</p><p style="font-size:15px;line-height:1.7">Bridal, evening and editorial makeup artist based in Prague, offering personalised services and one-on-one courses. Designing looks that enhance your natural features and your own distinctive style.</p><a class="lbl" href="{IG}">@nikol__mua</a></div></div>
</div></div></div>
</article>
<section class="duo" aria-label="Book or learn">
<div class="ox-box"><p class="lbl pink">Need help?</p><h2 class="big-h">Do you need help with creative make-up?</h2><a class="btn btn--pink" href="{CAL}">Book online +</a></div>
<div class="tiles" style="display:block"><a href="/en/courses/" style="height:100%;min-height:420px">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}<span class="cap"><span class="lbl pink">Learn with me</span><span class="wide" style="font-size:clamp(24px,2.6vw,34px)">Personalised one-on-one makeup courses in Prague →</span></span></a></div>
</section>
'''
    h += footer(LANG, 'Contact me', 'Do you need help with creative make-up?', 'Professional makeup artist based in Prague. Designing bespoke beauty looks that reflect your distinct personality.')
    write(path, h)


def build():
    home(); wedding(); service(EVENING); service(NUDE); service(COMMERCIAL); courses(); portfolio(); blog(); post()
