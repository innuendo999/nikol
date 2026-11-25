from lib import *
from lib import img as I
import schema as S
from pages_home import home_body
from ui26 import hero_svc, strip, intro2, features2, pricing2, steps2, gallery2, related2, svc_photos, review_quote, banner2, hero_from_split
from reviews import pick
from pages_guide import fab as guide_fab
from posts import teaser
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
        ('Where are you based and do you travel for bookings?', 'I am a professional makeup artist based in Prague 8 – Karlín (Prvního pluku 8a), Czech Republic. I work across all districts of Prague – including Praha 1 (Old Town), Praha 2 (Vinohrady), and Praha 8 (Karlín) – and I also travel to other cities in the Czech Republic and across Europe for destination weddings, photo shoots and events.'),
        ('What makeup services do you offer?', 'I offer wedding and bridal makeup, evening and cocktail styling, natural nude looks, <a href="/en/ball-makeup/">ball and prom makeup with hair</a>, <a href="/en/event-makeup/">makeup for corporate and social events</a>, commercial and editorial makeup for photo shoots, and personalized one-on-one makeup courses for clients who want to learn professional techniques.'),
        ('Do you speak English?', 'Yes. I provide makeup services fluently in English and Czech, which makes me a comfortable choice for international clients, expats living in Prague, and couples planning a destination wedding in the Czech Republic.'),
        ('What is included in the wedding makeup package?', 'The wedding package includes a bridal trial before the wedding day, full wedding-day makeup application, false lashes, and a personal touch-up kit so your look stays fresh from the ceremony through the reception.'),
        ('How much does makeup in Prague cost?', 'Prices depend on the type of service, location, and timing – bridal packages, evening makeup and commercial shoots are all priced individually. Please contact me with your event details and I will send you a personalized quote within 24 hours.'),
        ('How far in advance should I book?', 'For weddings I recommend booking 6–12 months in advance, especially for the peak season from May to September. For evening makeup and shoots, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'),
        ('What does a makeup course look like?', 'Courses are personalized one-on-one sessions tailored to your skill level and goals – from learning everyday makeup for yourself to professional techniques for aspiring MUAs. We cover skin prep, color theory, application techniques, and product selection using your own face as the canvas.'),
        ('How can I book an appointment?', f'You can book <a href="{CAL}">online via Calendly</a>, call or text <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a>, or send a direct message on Instagram <a href="{IG}">@nikol__mua</a>. I usually reply within a few hours.'),
    ]
    h = head(LANG, title, desc, path, alts('/', '/en/'), SITE + '/img/nikol.jpg', S.load('en-home'), preload('nikol-hero', '100vw'))
    h += header(LANG, 'home', '/')
    h += home_body(LANG)
    h += reviews(LANG, 'what clients say', pick('zoe', 'nelli', 'glenn', 'polina', 'shirley', 'darya', 'beata', 'marie', 'lena'), top=False)
    h += teaser(LANG, ['blush', 'travel', 'brushes'], 'From the blog', 'tutorials &amp; honest reviews')
    h += faq(LANG, 'popular questions', faq_items)
    h += guide_fab(LANG)
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
    h = head(LANG, title, desc, path, alts('/svatebni-liceni/', path), SITE + '/img/wedding/wedding-prague-1.png', S.load('en-wedding'), preload('bride-window', '(max-width: 900px) 60vw, 30vw'))
    h += header(LANG, '/en/wedding/', '/svatebni-liceni/')
    h += hero_svc(LANG, [HOME, SVC, ('Wedding makeup', None)], 'Bridal makeup', 'in Prague – makeup that lasts all day',
                  'Your wedding day deserves a look as unique as your love story. I create long-lasting, radiant bridal makeup that enhances your natural beauty – tailored entirely to you, your dress and your vision.',
                  (CAL, 'Book appointment online +'),
                  [('bride-window', 'Bridal makeup Prague – bride by the window', 'u-c2'), ('bride-calla', 'Bridal makeup – bride with calla lilies', 'u-c2')],
                  ('“…a flawless look that held up perfectly for over 15 hours.”', '5.0 on Google'))
    h += strip(['Lasts all day', 'Bridal trial included', 'English-speaking', 'Destination weddings', 'Bride, bridesmaids &amp; mother'])
    h += intro2('About the service', 'Your bridal look, exactly as you imagined', 'beautiful, camera-ready and uniquely yours',
               [('stairs-couple', 'Bridal makeup – newlyweds on the stairs'), ('window-ready-2', 'Bride getting ready')],
               "As a professional <b>wedding makeup artist based in Prague</b>, I work with brides to create looks that are beautiful, camera-ready, and – most importantly – uniquely theirs. Whether you are getting married in Prague's Old Town, a château outside the city, or planning a destination wedding anywhere in Europe, I will travel to you. Every bridal service begins with a detailed consultation about your vision, skin type, dress and wedding aesthetic. A <b>bridal trial</b> is included in every wedding package so you arrive on your wedding day fully confident.",
               ['English-speaking – ideal for international &amp; expat brides', 'Bridal trial included in every wedding package', 'Bride, bridesmaids &amp; mother of the bride', 'Destination weddings across Czech Republic &amp; Europe'],
               (CAL, 'Book your bridal consultation +'))
    h += features2('What sets the bridal experience |apart', 'why brides choose Nikol', [
        ('img', 'mother-makeup', 'Makeup for the mother of the bride'),
        ('panel', '01', 'English-speaking MUA', 'Fluent in English, Czech and Ukrainian – no communication barriers for international brides or destination weddings in Prague.', False),
        ('img', 'bride-mirror', 'Bride checking her look in the mirror'),
        ('panel', '02', 'Bridal trial included', 'Every wedding package includes a dedicated trial session so you refine your look and arrive on the day with complete confidence.', True),
        ('panel', '03', 'Destination weddings', 'Available throughout the Czech Republic and across Europe – I come to your venue, hotel or location of choice.', True),
        ('img', 'castle-couple', 'Château wedding'),
        ('panel', '04', 'Long-lasting finish', 'Professional products and techniques keep your bridal look fresh and photo-ready from the ceremony to the last dance.', False),
        ('img', 'couple-field', 'Bridal look at sunset')])
    h += pricing2('Rates &amp; services', 'Wedding makeup |packages', 'Pricing varies by date, location and scope. Personalised quote within 24 hours.', [
        ('Full bridal package', 'Request', ['Personalised Bridal Trial', 'Wedding-Day Application', 'False Lashes Included', 'Touch-Up Kit for the Day', 'Travel to Venue (Prague)'], 'Request a quote +'),
        ('Bridal party &amp; travel', 'Request', ['Bridesmaids Makeup', 'Mother of the Bride', 'Coordinated Party Look', 'Travel Across Czech Republic', 'European Destinations'], 'Request a quote +')], imgs=[('couple-bouquet', 'Wedding makeup package'), ('bridesmaids', 'Bridal party – bride and bridesmaids')])
    h += steps2('The bridal |process', 'how it works', [
        ('Initial consultation', 'We discuss your vision, dress and venue – in person, by phone or video call, convenient for international brides planning a destination wedding in Prague.'),
        ('Bridal trial session', 'Typically 4–8 weeks before the wedding. We test the full look, adjust colours and techniques, and finalise every detail with trial photos.'),
        ('Wedding morning makeup', "Nikol arrives at your hotel, venue or home. Bridal party makeup is scheduled first; the bride's look is applied last so it is freshest for the ceremony and photos."),
        ('Touch-up kit &amp; final check', 'You receive a personalised touch-up kit with the key products used on your skin, so your look stays perfect through to the last dance.')],
        'From your first consultation to the final touch-up on your wedding day – here is exactly what to expect when you book Nikol Pavlova as your wedding makeup artist in Prague.')
    h += gallery2('Recent |bridal looks', 'selected work', 'View full portfolio', '/en/portfolio/', [('veil-kiss', 'Bridal makeup – kiss under the veil'), ('bride-dress', 'Bridal makeup – bride before putting on the dress'), ('stairs-bride', 'Bridal makeup – bride on the staircase'), ('wedding-walk', 'Bridal makeup – leaving the ceremony'), ('couple-garden', 'Bridal makeup – garden portrait'), ('terrace-toast', 'Bridal makeup – toast on the terrace'), ('church-bw', 'Bridal makeup – leaving the church'), ('bride-back', 'Bridal makeup – dress and hair detail')])
    h += reviews(LANG, 'brides &amp; wedding shoots', pick('shirley', 'polinashu', 'erika_w'), top=False, title='Google reviews from brides')
    h += f'''<section class="sec u u-guide" aria-labelledby="guide-h"><div class="wrap guide">
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
    h += faq(LANG, 'FAQ', faq_items, title='Questions about wedding makeup')
    h += teaser(LANG, ['blush', 'travel'])
    h += related2(LANG, [('Evening makeup', '/en/evening-makeup/', 'evening-5'), ('Makeup courses', '/en/courses/', 'course')])
    h += guide_fab(LANG)
    h += footer(LANG, 'Book your bridal consultation', 'Get in touch', 'Based in Prague, Czech Republic · Available for travel across Europe. Personalised quote within 24 hours.', (CAL, 'Book your appointment online +'))
    write(path, h)


# ---------------------------------------------------------------- GENERIC SERVICE (EN)
def service(cfg):
    path = cfg['path']
    hero_ph, price_ph, gal = svc_photos(cfg, LANG)
    parent = [cfg['parent']] if cfg.get('parent') else []
    sch = S.service_page(LANG, path, cfg['title'], cfg['desc'], cfg['service_name'], cfg['service_type'],
                         f"/assets/img/{hero_ph[0][0]}-800.webp", [('Home', '/en/'), ('Services', '/en/#services')] + parent + [(cfg['crumb'], path)], cfg['faq'], cfg['offers'])
    h = head(LANG, cfg['title'], cfg['desc'], path, alts(cfg['cs'], path), SITE + f"/assets/img/{hero_ph[0][0]}-800.webp", sch,
             preload(hero_ph[0][0], '(max-width: 900px) 60vw, 30vw'))
    h += header(LANG, path, cfg['cs'])
    h += hero_svc(LANG, [HOME, SVC] + parent + [(cfg['crumb'], None)], cfg['big'].replace('<br>', ' '), cfg['sub'], cfg['lead'], (cfg['buttons'][0][1], cfg['buttons'][0][0]),
                  hero_ph, review_quote(cfg['reviews'], LANG))
    h += strip(cfg['marquee'])
    h += intro2('About the service', cfg['intro_title'], cfg['intro_tag'], cfg['intro_imgs'], cfg['intro_body'], cfg['chips'])
    h += features2(cfg['grid_title'], cfg['grid_sub'], cfg['grid'])
    h += pricing2('Rates', cfg['price_title'], cfg['price_note'], cfg.get('price_cols') or [cfg['price_col']], cfg.get('price_href', '#contact'), imgs=price_ph)
    h += steps2(cfg['steps_title'], 'how it works', cfg['steps'])
    h += gallery2(cfg['gal_title'], 'selected work', 'View full portfolio', '/en/portfolio/', gal)
    h += banner2(cfg.get('banner', ''))
    h += reviews(LANG, cfg['rv_sub'], cfg['reviews'], top=False, title=cfg.get('rv_h2'))
    h += faq(LANG, cfg['faq_sub'], cfg['faq'], title=cfg.get('faq_h2'))
    h += teaser(LANG, cfg.get('posts', []))
    h += related2(LANG, cfg['related'])
    h += guide_fab(LANG)
    h += footer(LANG, cfg['f_label'], 'Get in touch', cfg['f_text'], cfg.get('f_primary'))
    write(path, h)

EVENING = dict(
    posts=['blush', 'catrice'],
    path='/en/evening-makeup/', cs='/vecerni-liceni/', crumb='Evening makeup', tone='tone-ox',
    title='Evening Makeup Prague | Glam & Smoky Eyes – Nikol Pavlova',
    desc='Evening makeup in Prague: soft glam, smoky eyes, statement lips and Hollywood glam for cocktail parties, dinners and celebrations. Makeup that lasts all night.',
    service_name='Evening makeup Prague', service_type='Evening makeup',
    offers=['Cocktail Makeup', 'Evening Styling', 'Prom / Ball Makeup', 'Photo Shoots'],
    big='Evening<br>makeup', sub='in Prague – glam, smoky eyes &amp; statement lips',
    lead='Glamorous looks built for galas, cocktail parties, proms, balls and special events in Prague. Smoky eyes, sculpted cheekbones, statement lips and luminous skin – finished with techniques that hold up under both flash photography and ambient evening light.',
    buttons=[('Book appointment +', CAL), ('Makeup styles', '#grid-h')], hero_img='evening-5', hero_alt='Evening makeup Prague – elegant glamour look',
    marquee=['Balls', 'Galas', 'Cocktail parties', 'Proms', 'Smoky eyes', 'Statement lips'],
    intro_title='A bold look you feel confident in', intro_tag='from soft glam to dramatic smoky eyes',
    intro_imgs=[('evening-1', 'Evening look – glamour smoky eye'), ('evening-3', 'Evening look – bold lip and clean skin')],
    intro_body='Every evening look is tailored to your dress, hair, lighting and the character of the event. We start with a quick chat about how bold you want to go. I come to your home, hotel or venue anywhere in Prague; travel outside Prague is available on request. Going to a ball? See <a href="/en/ball-makeup/">ball makeup and hair</a>. For a corporate event, gala or a group, there is <a href="/en/event-makeup/">event makeup</a>.',
    chips=['Balls, proms &amp; galas', 'Cocktail parties &amp; celebrations', 'Photo shoots', 'English &amp; Czech'],
    grid_title='Evening makeup styles', grid_sub='from soft glam to smoky eyes', grid=[
        ('img', 'evening-13', 'Soft glam evening look'), ('panel', '01', 'Soft glam', 'Luminous skin, softly defined eyes and an elegant, timeless finish.', False),
        ('img', 'evening-12', 'Dramatic eye styling'), ('panel', '02', 'Smoky eyes', 'Smoky eyes and dramatic eye styling for the big nights.', True),
        ('panel', '03', 'Statement lips', 'Clean skin with a bold lip as the focus of the whole look.', True), ('img', 'evening-16', 'Sculpted contour and lips'),
        ('panel', '04', 'Hollywood glam', 'Flawless skin, liner and a classic red lip – a timeless look for a big night.', False), ('img', 'evening-4', 'Evening glamour styling')],
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
    faq_sub='FAQ', faq_h2='Questions about evening makeup', faq=[
        ('How far in advance should I book?', 'For evening makeup and shoots, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'),
        ('How much does evening makeup cost in Prague?', 'Prices depend on the type of service, location and timing. Send me your event details and I will reply with a personalised quote within 24 hours.'),
        ('Do you come to me?', 'Yes. I work across all districts of Prague – including Praha 1 (Old Town), Praha 2 (Vinohrady) and Praha 8 (Karlín) – and travel to other cities in the Czech Republic and across Europe.'),
        ('Do you speak English?', 'Yes, I speak fluent English and Czech, so international clients and expats in Prague are very welcome.'), BOOK_FAQ],
    related=[('Ball makeup', '/en/ball-makeup/', 'evening-14'), ('Event makeup', '/en/event-makeup/', 'evening-1')],
    f_label='Book your evening makeup', f_text='Based in Prague, Czech Republic · Available for travel. Personalised quote within 24 hours.')

PRICE_NOTE = 'Travel is charged separately depending on the location.'

BALL = dict(
    posts=['blush', 'catrice'],
    path='/en/ball-makeup/', cs='/plesove-liceni/', crumb='Ball makeup',
    parent=('Evening makeup', '/en/evening-makeup/'), tone='tone-ox',
    title='Ball & Prom Makeup and Hair Prague | Nikol Pavlova',
    desc='Ball and prom makeup and hair in Prague, at your home or hotel. Makeup that lasts until morning and looks great in photos. Dates open for the 2027 ball season.',
    service_name='Ball makeup and hair Prague', service_type='Ball makeup and hairstyling',
    offers=[('Ball makeup', 2500), ('Ball hairstyle', 2500), ('Ball makeup and hair', 4500)],
    big='Ball<br>makeup', sub='and hair in Prague – makeup that lasts until morning',
    lead='Makeup and hair for school-leaving balls (maturitní ples), formal balls and corporate balls. I come to your home or hotel anywhere in Prague and create a look that lasts the whole night, the dancing and every flash photo.',
    buttons=[('Check available dates +', CAL), ('Prices', '#packages')], hero_img='evening-14',
    hero_alt='Ball makeup Prague – glamour makeup and Hollywood waves',
    marquee=['School-leaving balls', 'Formal balls', 'Corporate balls', 'Makeup &amp; hair', 'Lasts until morning', 'Prague &amp; surroundings'],
    intro_title='Ball makeup without the stress – makeup and hair in one appointment', intro_tag='2027 ball season: January and February Saturdays fill up first',
    intro_imgs=[('evening-17', 'Ball hairstyle – updo with loose strands and soft glam'), ('evening-12', 'Ball look – Hollywood waves and bold lashes')],
    intro_body='I tailor <b>ball makeup</b> to your dress, hair and the character of the ball – from a soft look for a graduate to bold glam for a formal ball. I prep the skin so the makeup survives dancing, a warm ballroom and flash photos, and I do your <b>ball hairstyle</b> in the same appointment, so you don’t have to go anywhere else. I work at your home, your hotel or my studio in Prague 8 – Karlín. In ball season I recommend booking 4–6 weeks ahead.',
    chips=['School-leaving, formal &amp; corporate balls', 'Makeup and hair in one appointment', 'Graduate and mum', 'English · Česky · Українська'],
    grid_title='Ball looks and hairstyles', grid_sub='what suits your dress', grid=[
        ('img', 'evening-13', 'Soft glam ball look'), ('panel', '01', 'Soft glam', 'Luminous skin and softly defined eyes. Works with light and pastel dresses and for graduates.', False),
        ('img', 'evening-12', 'Hollywood waves and glamour makeup'), ('panel', '02', 'Hollywood waves', 'Glossy waves and bold lashes – a classic with long satin gowns.', True),
        ('panel', '03', 'Elegant updo', 'A hairstyle that lasts a night of dancing and shows off your neckline and earrings.', True), ('img', 'wedding-12', 'Elegant updo and glamour makeup'),
        ('panel', '04', 'Smoky eyes &amp; bold lips', 'A dramatic evening look for black, red and velvet gowns.', False), ('img', 'evening-6', 'Bold evening look for a ball')],
    price_title='Ball makeup and hair', price_note=PRICE_NOTE + ' False lashes, a price for a group of friends and travel are agreed when you book.',
    price_cols=[('Ball makeup', 'CZK 2,500', ['Skin prep', 'Makeup that lasts until morning', 'Matched to your dress and hair', 'Tips for touch-ups during the night'], 'Book +'),
                ('Ball hairstyle', 'CZK 2,500', ['Updo, waves or half-up', 'Set to last all night', 'Matched to your dress and accessories'], 'Book +'),
                ('Makeup + hair', 'CZK 4,500', ['Ball makeup', 'Ball hairstyle', 'One appointment, about 2 hours', 'You save CZK 500', 'Graduate and mum'], 'Book +')],
    price_href=CAL,
    steps_title='How ball makeup works', steps=[
        ('Booking', 'Send me the date of the ball, when you need to leave and the location. In ball season, book 4–6 weeks ahead – Saturdays go fastest.'),
        ('Dress and inspiration', 'Send me a photo of your dress and looks you like. We agree on how bold the makeup should be and the type of hairstyle.'),
        ('Makeup and hair', 'Makeup alone takes 60–75 minutes, makeup with hair 2 hours. We start 2–3 hours before you leave for the ball.'),
        ('Final check', 'Last touches, setting and tips on refreshing your look during the night.')],
    gal_title='Ball looks', gallery=[],
    banner=f'''<section class="sec--tight" aria-label="Makeup courses"><div class="wrap"><a class="banner" href="/en/courses/"><span class="txt"><span class="lbl pink">Makeup courses</span><span class="mid-h">Want to do your own ball makeup?</span><span class="serif" style="font-size:20px;color:#E9DCD8">In a one-on-one lesson for CZK 3,500 you learn an evening look on your own face.</span><span class="btn btn--pink">Makeup courses →</span></span><span class="img">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}</span></a></div></section>
''',
    rv_sub='makeup and hair that last', reviews=pick('zoe_c', 'shirley', 'nelli'),
    faq_sub='FAQ', faq_h2='Questions about ball makeup', faq=[
        ('How much does ball makeup cost in Prague?', 'Ball makeup costs CZK 2,500, a ball hairstyle CZK 2,500, and makeup and hair together only CZK 4,500 – you save CZK 500. Travel is charged separately depending on the location.'),
        ('Do you also do ball hairstyles?', 'Yes. I do makeup and hair in one appointment – from an elegant updo to Hollywood waves. Send me a photo of your dress and some inspiration.'),
        ('How far ahead should I book?', 'In ball season (January–February) I recommend 4–6 weeks ahead; Saturdays disappear fastest. Outside the season, 2–3 weeks is usually enough.'),
        ('Will the makeup last all night?', 'Yes. I prep the skin, set the makeup in layers and use waterproof products. I leave you the lipstick for small touch-ups.'),
        ('How long does it take?', 'Makeup alone about 60–75 minutes, makeup and hair 2 hours.'),
        ('Will you come to my home or hotel?', 'Yes, I travel all over Prague, and outside Prague by arrangement. Travel is charged separately depending on the location.'),
        ('Can you also do my mum or friends?', 'Yes, I’m happy to get several people ready at once – just give the number when booking and I’ll plan the timing so you are all ready on time.'),
        ('Can I send inspiration and a photo of my dress?', 'Definitely – it helps fine-tune the colours and intensity of the look.'),
        ('I have sensitive skin – is that a problem?', 'Not at all. Let me know in advance and I’ll adapt the products.'), BOOK_FAQ],
    related=[('Evening makeup', '/en/evening-makeup/', 'evening-5'), ('Event makeup', '/en/event-makeup/', 'evening-1')],
    f_label='Book your ball makeup', f_text='2027 ball season · Prague and surroundings · Travel charged separately.')

EVENTS = dict(
    posts=['catrice', 'empties'],
    path='/en/event-makeup/', cs='/liceni-na-akce/', crumb='Event makeup',
    parent=('Evening makeup', '/en/evening-makeup/'), tone='tone-sand',
    title='Event Makeup Artist Prague | Corporate Events & Galas',
    desc='Makeup and hair for social events, galas and corporate events in Prague. For individuals and groups, in English and Czech. Book online or by phone.',
    service_name='Event makeup Prague', service_type='Makeup and hair for social and corporate events',
    offers=[('Event makeup', 2500), ('Event hairstyle', 2500), ('Event makeup and hair', 4500)],
    big='Event<br>makeup', sub='in Prague – corporate events, galas &amp; parties',
    lead='A gala, a company party, a conference, a birthday or a hen party. I do makeup and hair for you or your whole group – at your place, your hotel or right at the venue.',
    buttons=[('Book online +', CAL), (f'Call {TEL_H}', f'tel:{TEL}'), ('Send an email', f'mailto:{MAIL}')], hero_img='evening-1',
    hero_alt='Event makeup Prague – glamour look for a social event',
    marquee=['Galas', 'Company parties', 'Conferences', 'Birthdays &amp; celebrations', 'Groups', 'English · Česky'],
    intro_title='Event makeup for you and your company', intro_tag='from a gala to a conference',
    intro_imgs=[('wedding-2', 'Group makeup and hair for a whole group'), ('evening-11', 'Gala makeup')],
    intro_body='At an event you want to look great without the worry. <b>For you</b> I do makeup and hair for a gala, a party, a birthday, an anniversary, a premiere or a hen party. <b>For companies and organisers</b> I provide makeup for speakers and hosts before a conference or filming, group makeup for your team and touch-ups during the event. We can work in English, Czech or Ukrainian.',
    chips=['For individuals and groups', 'Makeup and hair in one appointment', 'At the venue in Prague', 'English · Česky · Українська'],
    grid_title='Event makeup formats', grid_sub='what I can do for you', grid=[
        ('panel', '01', 'Individual makeup and hair', 'A look tailored to your outfit and the event – at your place, your hotel or my studio in Karlín.', False), ('img', 'evening-7', 'Makeup for a social event'),
        ('panel', '02', 'Group makeup', 'Friends, bridesmaids or a whole team – I prepare a schedule so everyone is ready on time.', True), ('img', 'wedding-3', 'Makeup and hair for an event guest'),
        ('img', 'evening-15', 'Makeup for a company party'), ('panel', '03', 'At the venue', 'I come to the venue and, if agreed, stay on for touch-ups during the evening.', True),
        ('img', 'evening-2', 'Natural makeup on camera'), ('panel', '04', 'On camera and on stage', 'Makeup for speakers, hosts and filming that works under stage lights.', False)],
    price_title='Prices per person', price_note=PRICE_NOTE + ' Touch-ups during the event, group prices and travel are agreed when you book.',
    price_cols=[('Event makeup', 'CZK 2,500', ['Skin prep', 'Makeup that lasts all evening', 'Matched to your outfit and the event'], 'Book +'),
                ('Event hairstyle', 'CZK 2,500', ['Updo, waves or a sleek style', 'Set to last all evening'], 'Book +'),
                ('Makeup + hair', 'CZK 4,500', ['Event makeup', 'Hairstyle', 'One appointment, about 2 hours', 'You save CZK 500'], 'Book +')],
    price_href=CAL,
    steps_title='How event makeup works', steps=[
        ('Enquiry', f'Call <a href="tel:{TEL}">{TEL_H}</a>, email <a href="mailto:{MAIL}">{MAIL}</a> or pick a time in <a href="{CAL}">Calendly</a>. Tell me the date, time, place and number of people.'),
        ('Schedule', 'For groups I prepare a timetable – makeup alone takes 60–75 minutes per person, makeup with hair 2 hours.'),
        ('Makeup and hair', 'At your place, your hotel or right at the venue, with products that last all evening.'),
        ('Final check', 'Last touches before the event starts and, if agreed, touch-ups during the evening.')],
    gal_title='Event looks', gallery=[
        ('evening-1', 'Event makeup – glamour look'), ('evening-5', 'Evening look for a social event'),
        ('evening-11', 'Gala makeup'), ('evening-3', 'Party look – bold lip and clean skin'),
        ('evening-4', 'Elegant makeup for a corporate event'), ('wedding-2', 'Group makeup – getting several people ready')],
    rv_sub='looks that last all evening', reviews=pick('zoe', 'glenn', 'erika'),
    faq_sub='FAQ', faq_h2='Questions about event makeup', faq=[
        ('How much does event makeup cost?', 'Per person: makeup CZK 2,500, hair CZK 2,500, makeup and hair together only CZK 4,500 – you save CZK 500. Travel is charged separately depending on the location.'),
        ('How many people can you do?', 'It depends on the time we have. Allow roughly 60–75 minutes for makeup alone and 2 hours for makeup with hair per person – I plan the schedule around that.'),
        ('Can you stay at the event for touch-ups?', 'Yes, by arrangement. Scope and price are agreed when you book.'),
        ('Will you come to the venue?', 'Yes – to hotels, offices and venues anywhere in Prague, and outside Prague by arrangement. Travel is charged separately depending on the location.'),
        ('Do you speak English?', 'Yes – English, Czech and Ukrainian, so international teams and foreign guests are very welcome.'), BOOK_FAQ],
    related=[('Ball makeup', '/en/ball-makeup/', 'evening-14'), ('Commercial makeup', '/en/commercial-makeup/', 'commercial-4')],
    f_label='Planning an event?', f_text='Send me the date, place and number of people – or pick a time online.')

NUDE = dict(
    posts=['blush', 'summer'],
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
    grid_title='Who nude makeup is for', grid_sub='when a nude look works best', grid=[
        ('panel', '01', 'Engagement shoots', 'A natural look that feels fresh and timeless in photos.', False), ('img', 'wedding-13', 'Natural bridal beauty'),
        ('panel', '02', 'Daytime portraits', 'Business, profile and personal portraits in daylight.', True), ('img', 'nude-3', 'Fresh dewy skin'),
        ('img', 'wedding-1', 'Soft bridal makeup'), ('panel', '03', 'Civil ceremonies', 'A soft bridal look for smaller and civil ceremonies.', True),
        ('img', 'nude-2', 'Soft natural glow'), ('panel', '04', 'Barely-there', 'Healthy glowing skin with a minimum of product.', False)],
    price_title='Natural makeup', price_note='Prices depend on the type of service, location and timing. Send me the details and I will reply with a personalised quote within 24 hours.',
    price_col=('Nude makeup', 'Request', ['Skin preparation', 'Light base &amp; concealer', 'Soft eye &amp; brow definition', 'Natural cheeks &amp; lips'], 'Request a quote +'),
    steps_title='How nude makeup works', steps=[
        ('Enquiry', 'Send me the date, location and occasion. I usually reply within a few hours.'),
        ('Skin prep', 'Every look starts with skincare tailored to your skin type.'),
        ('Light layers', 'Coverage only where needed and soft definition of your features.'),
        ('Final check', 'A daylight check so the look reads natural in person and on camera.')],
    gal_title='Natural looks', gallery=[('nude-1', 'Nude look – natural no-makeup look, Prague'), ('nude-2', 'Nude look – soft natural glow'), ('nude-3', 'Nude look – fresh dewy skin')],
    banner=f'''<section class="sec--tight" aria-label="Makeup courses"><div class="wrap"><a class="banner" href="/en/courses/"><span class="txt"><span class="lbl pink">Makeup courses</span><span class="mid-h">Want to learn the natural look yourself?</span><span class="serif" style="font-size:20px;color:#E9DCD8">In a one-on-one lesson we cover skin prep, colour theory and technique on your own face.</span><span class="btn btn--pink">Makeup courses →</span></span><span class="img">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}</span></a></div></section>
''',
    rv_sub='natural, fresh skin', reviews=pick('karin', 'marie', 'beata'),
    faq_sub='FAQ', faq_h2='Questions about nude makeup', faq=[
        ('Does a nude look work for a wedding?', 'Yes. Natural nude is one of the bridal styles I offer – ideal for civil ceremonies and brides who want to look like themselves. See <a href="/en/wedding/">Wedding makeup</a>.'),
        ('How much does nude makeup cost?', 'Prices depend on the type of service, location and timing. Send me the details and I will reply with a personalised quote within 24 hours.'),
        ('How far in advance should I book?', 'For shoots and everyday events, 2–3 weeks is usually enough, though last-minute slots can sometimes be arranged – just get in touch.'), BOOK_FAQ],
    related=[('Wedding makeup', '/en/wedding/', 'wedding-5'), ('Evening makeup', '/en/evening-makeup/', 'evening-5')],
    f_label='Book your nude makeup', f_text='Based in Prague, Czech Republic · Available for travel. Personalised quote within 24 hours.')

COMMERCIAL = dict(
    posts=['blush', 'nyx'],
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
    grid_title='Commercial project types', grid_sub='what I work on', grid=[
        ('img', 'commercial-1', 'Editorial shoot'), ('panel', '01', 'Beauty &amp; campaigns', 'Clean beauty work and brand campaigns for cosmetics and fashion labels.', False),
        ('img', 'commercial-3', 'Magazine editorial'), ('panel', '02', 'Editorial', 'Magazine editorials and bold, concept-led styling.', True),
        ('panel', '03', 'Lookbooks', 'Consistent looks for lookbooks and fashion collections.', True), ('img', 'commercial-5', 'Fashion editorial makeup'),
        ('panel', '04', 'Video content', 'Makeup for video and high-resolution content.', False), ('img', 'commercial-6', 'Media shoot')],
    price_title='Commercial projects', price_note='Commercial projects are priced individually by scope, location and date. Send me the shoot details and I will reply with a quote within 24 hours.',
    price_col=('Shoots &amp; production', 'Request', ['Concept &amp; look consultation', 'Makeup for light &amp; brief', 'On-set touch-ups', 'Travel across Czechia &amp; Europe'], 'Request a quote +'),
    steps_title='How a commercial shoot works', steps=[
        ('Brief', 'Send me the date, location, concept and number of looks. I usually reply within a few hours.'),
        ('Quote &amp; prep', 'You receive a quote within 24 hours and I prepare looks for the concept and light.'),
        ('Shoot day', 'Makeup on set and look changes following the production schedule.'),
        ('On-set touch-ups', 'Ongoing checks and touch-ups so the makeup looks perfect in every frame.')],
    gal_title='Commercial looks', gallery=[('commercial-1', 'Commercial look – editorial shoot, Prague'), ('commercial-2', 'Commercial look – campaign shoot'),
        ('commercial-3', 'Commercial look – magazine editorial styling'), ('commercial-4', 'Commercial look – beauty brand shoot'),
        ('commercial-5', 'Commercial look – fashion editorial'), ('commercial-6', 'Commercial look – media shoot')],
    rv_sub='shoots &amp; modelling', reviews=pick('polina', 'zoe_c', 'glenn'),
    faq_sub='FAQ', faq_h2='Questions about commercial makeup', faq=[
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
    h += hero_from_split(LANG, 'tone-sand', [HOME, SVC, ('Makeup courses', None)], 'Makeup<br>courses', 'in Prague – learn to create your own looks',
                    'Personalised one-on-one makeup lessons in Prague – whether you want to master everyday makeup for yourself or build professional skills as an aspiring makeup artist. We work on your own face, at your own pace.',
                    [('Book a course online +', CAL), ('Course options', '#packages')], 'course', 'One-on-one makeup course in Prague with Nikol Pavlova', '50% 15%')
    h += strip(['One-on-one', 'On your own face', 'English &amp; Czech', 'Beginners &amp; aspiring MUAs', 'Product list to take home'])
    h += intro2('About the course', 'Makeup lessons tailored entirely to you', 'no fixed script, just what you want to learn', [],
               'As a professional <b>makeup artist and instructor in Prague</b>, I teach personalised one-on-one <b>makeup courses</b> built around your level and goals. There is no fixed script – we focus on exactly what you want to learn, using your own face as the canvas so you can recreate every look at home. Whether you have never held a brush or you are an aspiring MUA refining professional technique, every lesson is hands-on, relaxed and practical – and you leave with a personalised product and tool list.',
               ['One-on-one – the whole session is about you', 'Beginners and aspiring professionals welcome', 'Taught in English &amp; Czech', 'Personalised product &amp; tool list to take home'],
               (CAL, 'Book your lesson +'))
    h += features2("What you'll learn", 'the curriculum', [
        ('img', 'nude-1', 'Natural everyday makeup'), ('panel', '01', 'Skin prep &amp; base', 'Skincare prep, priming and flawless foundation, concealer and base techniques for your skin type.', False),
        ('img', 'nude-2', 'Soft natural glow'), ('panel', '02', 'Colour theory', 'Face mapping and colour theory so you choose shades that flatter your features and tone.', True),
        ('panel', '03', 'Eyes &amp; lashes', 'Eyeshadow blending, liner, and false-lash application – from soft daytime to defined evening looks.', True), ('img', 'evening-7', 'Defined eye makeup'),
        ('panel', '04', 'Tools &amp; products', 'Contour, blush and highlight, plus how to choose the right brushes and build your own makeup kit.', False), ('img', 'evening-5', 'Evening glam look')])
    h += pricing2('Course options', 'Choose your course', "Course length and price are tailored to your level and goals. Personalised quote within 24 hours.", [
        ('Personal makeup lesson', 'Request', ['Learn Everyday Self-Makeup', 'Skin Prep &amp; Base', 'Eyes, Lashes &amp; Finish', 'Personalised Product List', 'One-on-One in Prague'], 'Request a course +'),
        ('Pro / aspiring MUA course', 'Request', ['Professional Techniques', 'Colour Theory &amp; Face Mapping', 'Hygiene &amp; Kit Building', 'Working on Clients', 'Tailored to Your Goals'], 'Request a course +')])
    h += steps2('How the course runs', 'how it works', [
        ('Goal-setting chat', 'We discuss your level, what you want to learn and the looks you love – in person, by phone or video call for international students.'),
        ('Personalised plan', 'I prepare a lesson plan around your goals, skin type and the products you already own, so every minute is relevant to you.'),
        ('Hands-on session', 'We work step by step on your own face. You do the application with guidance, so the techniques truly stick.'),
        ('Product list &amp; follow-up', 'You leave with a personalised product and tool list and notes, so you can confidently recreate everything at home.')],
        'Each makeup course in Prague is built around you. Here is what to expect from first message to follow-up.')
    h += f'''<section class="sec--tight u u-insp" aria-labelledby="insp-h"><div class="wrap">
{sec_head('Looks you can learn to create', 'inspiration', '<a class="link-arrow" href="/en/portfolio/">View full portfolio →</a>', hid='insp-h')}
<ul class="cards3" role="list" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))">
<li><figure class="pcard"><div class="ph">{I('nude-1', 'Natural everyday makeup look taught in Prague makeup course')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Natural daytime look</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('nude-2', 'Soft natural glow makeup technique, Prague lesson')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Soft glow</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-5', 'Evening glam makeup look taught in Prague course')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Evening glam</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-7', 'Defined eye makeup technique, Prague makeup lesson')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Defined eyes</figcaption></figure></li>
</ul></div></section>
<section class="sec u u-students" aria-labelledby="students-h"><div class="wrap">
{sec_head('Happy students', 'what they say about the lessons', f'<a class="btn" href="{CAL}">Book your lesson +</a>', hid='students-h')}
<div class="quotes3">
<figure><blockquote><p>“I finally understand how to do my own makeup. Nikol explained everything so clearly and let me do it myself – now I actually use these techniques every day.”</p></blockquote><figcaption class="lbl"><cite>Tereza H.</cite> <span class="muted2">· Personal lesson</span></figcaption></figure>
<figure><blockquote><p>“As someone starting out as an MUA, the pro session was exactly what I needed – real technique, hygiene and product advice you can't get from videos.”</p></blockquote><figcaption class="lbl"><cite>Marta S.</cite> <span class="muted2">· Pro course</span></figcaption></figure>
<figure><blockquote><p>“Booked a lesson in English as an expat in Prague. Relaxed, personal and so practical – I left with a product list I actually use.”</p></blockquote><figcaption class="lbl"><cite>Olivia R.</cite> <span class="muted2">· Personal lesson</span></figcaption></figure>
</div></div></section>
<section class="sec u u-guide" aria-labelledby="guide-h"><div class="wrap guide">
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
    h += faq(LANG, 'FAQ', faq_items, title='Questions about makeup courses')
    h += teaser(LANG, ['blush', 'travel', 'brushes'], 'Practise at home', 'tutorials from the blog')
    h += related2(LANG, [('Wedding makeup', '/en/wedding/', 'wedding-5'), ('Nude makeup', '/en/nude-makeup/', 'nude-1')])
    h += guide_fab(LANG)
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
    pills, figs, total = portfolio_grid(LANG, EN_ITEMS, 'All', '', '')
    h = head(LANG, title, desc, path, alts('/portfolio/', path), SITE + '/img/wedding/wedding-1.png', S.load('en-portfolio'), extra=NOSCRIPT)
    h += header(LANG, 'portfolio', '/portfolio/')
    h += f'''<section class="page-head u u-pf-head" aria-labelledby="page-h1"><div class="wrap">
{crumbs(LANG, [HOME, ('Portfolio', None)])}
<div class="top"><h1 class="h1" id="page-h1"><span class="big wide">Portfolio</span> <span class="sub serif">makeup – Nikol Pavlova, makeup artist Prague</span></h1>
<p class="body">This is a curated selection of makeup work created by <b>Nikol Pavlova</b>, a professional makeup artist based in <b>Prague, Czech Republic</b>. The portfolio covers bridal looks for weddings across Prague and Europe, glamorous evening and cocktail makeup, soft natural nude styling, commercial and editorial work for photo shoots, and behind-the-scenes images from one-on-one makeup courses. Each look is designed to enhance the client's natural features while reflecting their personal style and the occasion.</p></div>
</div></section>
<section class="sec--tight u u-pf" aria-labelledby="looks-h">
<div class="wrap">{sec_head('Choose a look', 'browse by category', f'<div class="filters" role="group" aria-label="Category">{pills}</div>', hid='looks-h')}</div>
<div class="pgrid" data-portfolio data-label-shown="Showing {{n}} of {{t}}" data-label-more="Show more ({{n}}) ↓" aria-live="polite">{figs}</div>
<div class="more-wrap"><p class="serif muted2" data-status>Showing {min(16, total)} of {total}</p><button class="pill btn--lg" type="button" data-more>Show more ({max(0, total - 16)}) ↓</button></div>
</section>
<section class="sec u u-cats" aria-labelledby="cats-h"><div class="wrap">
{sec_head('About each category', 'inside the portfolio', hid='cats-h')}
<div class="cat-rows">
<a href="/en/wedding/"><h3>Wedding makeup →</h3><p>Bridal looks designed to last from the first kiss to the final dance. Each wedding service includes a pre-wedding trial in Prague, day-of application with long-wear products suited to Czech summer and winter conditions, individual lashes, and a personal touch-up kit. Available for ceremonies in Prague Old Town, Vinohrady, château weddings outside the city, and destination weddings across Europe.</p></a>
<a href="/en/evening-makeup/"><h3>Evening &amp; cocktail makeup →</h3><p>Glamorous looks built for galas, cocktail parties, proms, balls and special events in Prague. Smoky eyes, sculpted cheekbones, statement lips and luminous skin – finished with techniques that hold up under both flash photography and ambient evening light.</p></a>
<a href="/en/nude-makeup/"><h3>Nude &amp; natural makeup →</h3><p>Soft, skin-first looks that enhance natural features without looking heavy. Ideal for engagement shoots, daytime portraits, civil ceremonies and clients who prefer a barely-there finish with healthy glowing skin.</p></a>
<a href="/en/commercial-makeup/"><h3>Commercial &amp; editorial →</h3><p>Makeup for photo shoots, brand campaigns, lookbooks, magazine editorials and video content. Adapted to the lighting and concept of each shoot – from clean beauty work to bold editorial styling – with on-set touch-ups across the production day.</p></a>
<a href="/en/courses/"><h3>Personalized makeup courses →</h3><p>One-on-one makeup courses tailored to your level – from clients who want to master everyday looks to aspiring makeup artists building professional skills. Held in Prague, covering skin prep, color theory, application techniques, tool selection and product recommendations using your own face as the canvas.</p></a>
</div></div></section>
<section class="sec u u-like" aria-labelledby="like-h"><div class="wrap ox-split" style="align-items:end">
<div style="display:flex;flex-direction:column;gap:22px"><p class="lbl pink">Like what you see?</p><h2 class="big-h" id="like-h">Let's create your own makeup look</h2><p class="serif ox-note">Get in touch to discuss your wedding, event or shoot. I'll send a personalized quote and availability within 24 hours.</p>
<p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn--pink" href="{CAL}">Book online +</a><a class="btn btn--ghost" href="mailto:{MAIL}">{MAIL}</a></p></div>
<dl class="kv"><div><dt class="lbl">Location</dt><dd>Prague, Czech Republic</dd></div><div><dt class="lbl">Phone</dt><dd><a href="tel:{TEL}">{TEL_H}</a></dd></div><div><dt class="lbl">Instagram</dt><dd><a href="{IG}">@nikol__mua</a></dd></div><div><dt class="lbl">Travel</dt><dd>Czechia &amp; Europe</dd></div></dl>
</div></section>
'''
    h += footer(LANG, 'Contact me', 'Do you need help with creative make-up?', "Get in touch to plan your look – I'll reply within 24 hours.")
    write(path, h)


def build():
    home(); wedding(); service(EVENING); service(BALL); service(EVENTS); service(NUDE); service(COMMERCIAL); courses(); portfolio()
