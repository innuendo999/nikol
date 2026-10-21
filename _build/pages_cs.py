from lib import *
from lib import img as I
import schema as S
from posts import teaser
from reviews import pick

LANG = 'cs'
HOME = ('Domů', '/')
SVC = ('Služby', '/#services')


def alts(cs, en):
    return [('cs', cs), ('en', en), ('x-default', cs)] if en else [('cs', cs), ('x-default', cs)]


# ---------------------------------------------------------------- HOME
def home():
    path = '/'
    title = 'Profesionální vizážistka Praha - Líčení & Kurzy | Nikol Pavlova'
    desc = 'Hledáte zkušenou vizážistku v Praze? Nabízím profesionální svatební líčení, večerní make-up a kurzy líčení. Rezervujte si termín online.'
    faq_items = [
        ('Kde působíte a jezdíte za klienty?', 'Jsem profesionální vizážistka se sídlem v Praze. Pracuji ve všech pražských čtvrtích – včetně Prahy 1 (Staré Město), Prahy 2 (Vinohrady) a Prahy 7 – a zároveň cestuji do dalších měst v České republice i po Evropě za svatbami, focením a akcemi.'),
        ('Jaké služby líčení nabízíte?', 'Nabízím svatební líčení, večerní a koktejlový make-up, přirozené nude looky, plesový make-up, komerční a editorial líčení pro focení i osobní kurzy líčení pro klienty, kteří se chtějí naučit profesionální techniky.'),
        ('V jakých jazycích mluvíte?', 'Mluvím plynně česky a anglicky, takže nabízím pohodlný servis jak českým, tak mezinárodním klientům, expatům žijícím v Praze i párům plánujícím destination svatbu v České republice.'),
        ('Co obsahuje balíček svatebního líčení?', 'Svatební balíček zahrnuje předsvatební zkoušku líčení, kompletní líčení v den svatby, umělé řasy a osobní touch-up kit, aby váš look vypadal skvěle od obřadu až po hostinu.'),
        ('Kolik stojí líčení v Praze?', 'Ceny závisí na typu služby, lokaci a termínu – svatební balíčky, večerní líčení i komerční zakázky cením individuálně. Napište mi prosím detaily vaší akce a do 24 hodin vám pošlu osobní cenovou nabídku.'),
        ('Jak dlouho dopředu si rezervovat termín?', 'Pro svatby doporučuji rezervaci 6–12 měsíců dopředu, zejména v hlavní sezóně od května do září. Pro večerní líčení a focení obvykle stačí 2–3 týdny, někdy lze zařídit i last-minute termín – stačí mě kontaktovat.'),
        ('Jak probíhá kurz líčení?', 'Kurzy jsou osobní (one-on-one) lekce přizpůsobené vaší úrovni a cílům – od běžného líčení pro sebe až po profesionální techniky pro začínající vizážistky. Probereme přípravu pleti, teorii barev, aplikační techniky a výběr produktů přímo na vaší tváři.'),
        ('Jak si mohu rezervovat termín?', f'Rezervovat můžete <a href="{CAL}">online přes Calendly</a>, telefonicky nebo SMS na <a href="tel:{TEL}">{TEL_H}</a>, e-mailem na <a href="mailto:{MAIL}">{MAIL}</a> nebo přes Instagram <a href="{IG}">@nikol__mua</a>. Obvykle odpovídám do několika hodin.'),
    ]
    h = head(LANG, title, desc, path, alts('/', '/en/'), SITE + '/img/nikol.jpg', S.load('cs-home'),
             preload('nikol-hero', '100vw'))
    h += header(LANG, 'home', '/en/')
    h += f'''<section class="hero-full" aria-labelledby="page-h1">
{I('nikol-hero', 'Nikol Pavlova – profesionální vizážistka v Praze', sizes='100vw', priority=True, style='object-position:50% 30%')}
<div class="wrap inner">
<div></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="hero-row"><p>Ahoj! Jmenuji se Nikol a miluju tvořit krásné a jedinečné líčení, které zdůrazní to nejlepší v tobě. Pojďme společně vytvořit něco výjimečného!</p><a class="btn btn--light" href="#services">Moje služby <span aria-hidden="true">↓</span></a></div>
<h1 class="h1" id="page-h1"><span class="big">Nikol Pavlova</span><span class="sub">– profesionální vizážistka v Praze</span></h1>
</div>
</div>
</section>
'''
    h += marquee(['Svatební líčení', 'Nude makeup', 'Večerní líčení', 'Komerční líčení', 'Kurzy líčení', 'Praha 7 · možnost dojezdu'])
    h += f'''<section class="wrap intro" id="about" aria-labelledby="about-h">
<div class="head"><p class="lbl red">O mně</p><h2 class="mid-h" id="about-h">Nikol Pavlova je vizážistka v Praze</h2><p class="serif tag">tvořící líčení, ve kterém se cítíš jako ty</p></div>
<div class="pair">{I('nikol-portrait', 'Nikol Pavlova – portrét vizážistky', sizes='260px', style='object-position:50% 25%')}{I('nikol-header', 'Nikol Pavlova – profesionální vizážistka v Praze', sizes='260px', style='object-position:50% 20%')}</div>
<div class="rule" aria-hidden="true"><span class="serif">precizní technika</span><hr><span class="serif">přirozená krása.</span></div>
<p class="body">Ahoj, jsem Nikol, profesionální vizážistka v Praze. Můj styl spojuje precizní techniku, kreativitu a cit pro barvy i textury, díky čemuž vytvářím make-up looky, které dokonale zvýrazní tvou přirozenou krásu. Ať už toužíš po jemném svatebním vzhledu, odvážném večerním make-upu nebo originálním editoriálním looku, vždycky mě baví společně s tebou proměnit tvou vizi ve skutečnost.</p>
<ul class="chips"><li>Svatební specialistka</li><li>Editorial &amp; Komerce</li><li>Osobní kurzy líčení</li><li>Česky · English · Українська</li></ul>
{I('signature', 'Podpis Nikol Pavlova', sizes='220px', style='width:220px')}
</section>
<section id="services" aria-labelledby="services-h">
<div class="wrap">{sec_head('Co nabízím', 'služby', '<a class="link-arrow" href="/portfolio/">Celé portfolio →</a>', hid='services-h')}</div>
<ul class="g4" role="list">
<li>{I('wedding-5', 'Svatební líčení Praha')}</li>
<li><a class="tile-panel center" href="/svatebni-liceni/"><h3>Svatební líčení</h3><p class="serif">Dlouhotrvající &amp; zářivé</p><span class="lbl more">Detail →</span></a></li>
<li>{I('nude-1', 'Nude makeup Praha')}</li>
<li><a class="tile-panel center alt" href="/nude-liceni/"><h3>Nude makeup</h3><p class="serif">Přirozená krása</p><span class="lbl more">Detail →</span></a></li>
<li><a class="tile-panel center alt" href="/vecerni-liceni/"><h3>Večerní líčení</h3><p class="serif">Plesy a večírky</p><span class="lbl more">Detail →</span></a></li>
<li>{I('evening-5', 'Večerní líčení Praha')}</li>
<li><a class="tile-panel center" href="/komercni-liceni/"><h3>Komerční líčení</h3><p class="serif">Focení a reklama</p><span class="lbl more">Detail →</span></a></li>
<li>{I('commercial-4', 'Komerční líčení – focení pro beauty značku')}</li>
<li>{I('course', 'Kurzy líčení Praha', style='object-position:50% 15%')}</li>
<li><a class="tile-panel center" href="/kurzy-liceni/"><h3>Kurzy líčení</h3><p class="serif">Naučte se líčit jako profík</p><span class="lbl more">Detail →</span></a></li>
<li class="span2"><a class="tile-panel center dark" style="height:100%" href="{CAL}"><p class="serif" style="font-size:28px">Váš look, váš den.</p><h3 style="font-size:30px">Rezervovat termín +</h3></a></li>
</ul>
</section>
<section class="mos-sec" aria-labelledby="mos-h">
<div class="wrap"><div class="mos">
<h2 class="m-t big-h" id="mos-h" style="font-size:clamp(24px,2.4vw,30px);line-height:1.15">Tvořím looky, které zdůrazní tvou <span class="accent">přirozenou krásu</span></h2>
{I('wedding-1', 'Svatební look – jemný glam', cls='m1')}
{I('wedding-15', 'Svatební look – soft glam', sizes='(max-width: 900px) 50vw, 33vw', cls='m2')}
{I('evening-3', 'Večerní look – výrazný ret a čistá pleť', sizes='(max-width: 900px) 50vw, 33vw', cls='m3')}
{I('nude-3', 'Nude look – svěží dewy pleť', cls='m4')}
{I('commercial-6', 'Komerční look – editorial', cls='m5')}
{I('wedding-9', 'Svatební look – destination svatba v Praze', cls='m6')}
{I('evening-13', 'Večerní look – soft glam', cls='m7')}
<div class="m-s"><p class="lbl pink">Svatební specialistka · Editorial &amp; Komerce · Osobní kurzy líčení</p><p class="serif" style="font-size:clamp(22px,2.2vw,28px);line-height:1.2">Od jemného svatebního glow po výrazný editoriální look.</p><a class="btn btn--pink" href="/portfolio/">Zobrazit portfolio →</a></div>
{I('wedding-14', 'Svatební look – soft glam svatební líčení', cls='m8')}
</div></div>
</section>
<section class="phrase" aria-label="Můj přístup">
{I('contact', '', sizes='100vw', style='object-position:50% 30%')}<div class="mesh"></div>
<div class="wrap"><p><span>Precizní</span><span>technika</span></p><p><span>Kreativita</span><span>a cit</span></p><p><span>Pro barvy</span><span>i textury</span></p></div>
</section>
<section class="sec" id="pricing" aria-labelledby="pricing-h">
<div class="wrap">
{sec_head('Ceník', 'balíčky služeb', '<p class="serif muted2">*Pro konkrétní cenovou nabídku mě prosím kontaktujte.</p>', hid='pricing-h')}
<ul class="cards3" role="list">
<li><a class="pcard" href="/svatebni-liceni/"><div class="ph">{I('wedding-4', 'Svatební balíček', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Svatba</span></div><div class="row"><h3>Svatební balíček</h3><span class="lbl red">Info</span></div><p class="body">Zkouška líčení · Svatební make-up · Umělé řasy v ceně · Touch-up kit</p></a></li>
<li><a class="pcard" href="/vecerni-liceni/"><div class="ph">{I('evening-7', 'Speciální příležitosti – večerní líčení', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Speciální příležitosti</span></div><div class="row"><h3>Večer &amp; akce</h3><span class="lbl red">Info</span></div><p class="body">Večerní líčení · Plesový make-up · Make-up na focení · Líčení na akce</p></a></li>
<li><a class="pcard" href="/kurzy-liceni/"><div class="ph">{I('nude-2', 'Kurzy líčení', sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">Kurzy</span></div><div class="row"><h3>Osobní kurz líčení</h3><span class="lbl red">Na vyžádání</span></div><p class="body">Příprava pleti · Teorie barev · Oči &amp; řasy · Nástroje &amp; produkty</p></a></li>
</ul>
</div>
</section>
'''
    h += reviews(LANG, 'co říkají klientky', pick('nelli', 'zoe', 'polinashu', 'erika', 'darya', 'marie', 'stepanka', 'beata', 'lena'), top=False)
    h += teaser(LANG, ['summer', 'nyx'], 'Z blogu', 'tutoriály a poctivé recenze')
    h += faq(LANG, 'nejčastější otázky', faq_items)
    h += footer(LANG, 'Kontaktujte mě', 'Máte dotaz nebo si přejete rezervovat termín?',
                'Ráda vám pomohu vytvořit dokonalý look na váš speciální den. Neváhejte mě kontaktovat a společně naplánujeme vše potřebné.')
    write(path, h)


# ---------------------------------------------------------------- WEDDING
def wedding():
    path = '/svatebni-liceni/'
    title = 'Svatební líčení Praha | Svatební vizážistka Nikol Pavlova'
    desc = 'Profesionální svatební vizážistka v Praze. Nikol Pavlova nabízí balíčky svatebního líčení – zkušební líčení, řasy a sadu na dotyky. Anglicky mluvící. Rezervace: +420 608 178 390.'
    faq_items = [
        ('Co je zahrnuto v balíčku svatebního líčení v Praze?', 'Každý svatební balíček zahrnuje osobní zkušební líčení, kompletní líčení v den svatby, umělé řasy a sadu na dotyky s klíčovými produkty použitými na vaši pleť. Doprava na místo v Praze je v ceně; mimo Prahu může být účtováno cestovné.'),
        ('Jak dlouho dopředu si rezervovat svatební vizážistku v Praze?', 'Pro svatby v Praze, zejména v hlavní sezóně od května do září, důrazně doporučujeme rezervaci 6–12 měsíců předem. Oblíbené letní soboty se plní rychle. Na podzim a v zimě obvykle stačí 3–6 měsíců.'),
        ('Jezdíte na destinační svatby po České republice?', 'Ano. Působím v Praze, ale pravidelně cestuji na svatby po celé ČR – jižní Morava, zámky i lázeňská města jako Karlovy Vary – a po celé Evropě. Mimo Prahu se účtuje cestovné a případné ubytování.'),
        ('Mluvíte anglicky pro zahraniční nevěsty?', 'Ano. Mluvím plynně anglicky, česky a ukrajinsky a pravidelně pracuji se zahraničními nevěstami, expaty v Praze a páry z Velké Británie, USA, Irska či Austrálie, kteří plánují destinační svatbu v České republice.'),
        ('Kolik stojí svatební líčení v Praze?', 'Cena závisí na rozsahu služby, místě, datu a tom, zda je zahrnut svatební doprovod. Po úvodní konzultaci připravím osobní cenovou nabídku – napište mi detaily a ozvu se do 24 hodin.'),
        ('Můžete nalíčit celý svatební doprovod?', 'Ano. Kromě nevěsty líčím i družičky, maminku nevěsty a květinové družičky. K dispozici jsou skupinové balíčky a předem připravím časový harmonogram, aby byli všichni hotovi před obřadem.'),
        ('Jaké styly svatebního líčení nabízíte?', 'Specializuji se na všechny styly – jemný přirozený glow, glamour večerní líčení, klasický nude, Old Hollywood i bohémský romantický styl. Každý look je přizpůsoben pleti, rysům, šatům a tématu svatby a zkušební líčení je ideální čas vyzkoušet různé směry.'),
        ('Jak si rezervovat svatební konzultaci?', f'Rezervujte si termín online přes <a href="{CAL}">Calendly</a>, nebo zavolejte/napište na <a href="tel:{TEL}">{TEL_H}</a>, e-mail <a href="mailto:{MAIL}">{MAIL}</a>, případně napište na Instagram <a href="{IG}">@nikol__mua</a>. Obvykle odpovídám během několika hodin. Konzultace mohou probíhat osobně v Praze nebo přes videohovor pro zahraniční klienty.'),
    ]
    h = head(LANG, title, desc, path, alts(path, '/en/wedding/'), SITE + '/img/wedding/wedding-prague-1.png', S.load('cs-wedding'),
             preload('wedding-prague', '100vw'))
    h += header(LANG, path, '/en/wedding/')
    h += f'''<section class="hero-full hero-full--svc" aria-labelledby="page-h1">
{I('wedding-prague', 'Svatební líčení Praha – nevěsta a ženich', sizes='100vw', priority=True, style='object-position:60% 30%')}
<div class="wrap inner">
<div>{crumbs(LANG, [HOME, SVC, ('Svatební líčení', None)], cls='lbl glass crumbs-glass')}</div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="hero-row"><p>Váš svatební den si zaslouží vzhled stejně jedinečný jako váš příběh. Vytvářím dlouhotrvající a zářivé svatební líčení, které zvýrazní vaši přirozenou krásu – vždy na míru vám, vašim šatům a vaší představě.</p><a class="btn btn--light" href="{CAL}">Rezervovat termín online +</a></div>
<h1 class="h1" id="page-h1"><span class="big">Svatební líčení</span><span class="sub">v Praze – líčení, které vydrží celý den</span></h1>
</div>
</div>
</section>
'''
    h += marquee(['Vydrží celý den', 'Zkušební líčení v ceně', 'Anglicky mluvící', 'Destinační svatby', 'Nevěsta, družičky i maminka'])
    h += intro('O službě', 'Svatební líčení přesně podle vašich představ', 'krásné, připravené pro fotografie a jedinečně vaše',
               [('wedding-2', 'Svatební líčení Praha – nevěsta a družičky'), ('wedding-4', 'Svatební líčení – nevěsta a ženich')],
               'Jako profesionální <b>svatební vizážistka v Praze</b> pracuji s nevěstami na looku, který je krásný, připravený pro fotografie a – co je nejdůležitější – jedinečně jejich. Ať už se vdáváte na Staroměstském náměstí, na zámku za Prahou, nebo plánujete destinační svatbu kdekoli v Evropě, přijedu za vámi. Každá služba začíná podrobnou konzultací o vaší představě, typu pleti, šatech a stylu svatby. <b>Zkušební líčení</b> je součástí každého svatebního balíčku, abyste do svatebního dne šli zcela sebejistě.',
               ['Anglicky mluvící – ideální pro zahraniční nevěsty a expaty', 'Zkušební líčení v ceně každého svatebního balíčku', 'Nevěsta, družičky i maminka nevěsty', 'Destinační svatby po České republice i Evropě'],
               (CAL, 'Rezervovat svatební konzultaci +'))
    h += checker('Čím se služba odlišuje', 'proč si nevěsty vybírají Nikol', [
        ('img', 'wedding-15', 'Svatební look – soft glam'),
        ('panel', '01', 'Anglicky mluvící vizážistka', 'Plynně anglicky, česky a ukrajinsky – žádná jazyková bariéra pro zahraniční nevěsty ani destinační svatby v Praze.', False),
        ('img', 'wedding-3', 'Svatební look – dlouhotrvající líčení'),
        ('panel', '02', 'Zkušební líčení v ceně', 'Každý svatební balíček obsahuje zkušební líčení, abyste si vzhled doladili a do svatebního dne šli zcela sebejistě.', True),
        ('panel', '03', 'Destinační svatby', 'K dispozici po celé České republice i Evropě – přijedu na vaše místo konání, do hotelu či kamkoli si přejete.', True),
        ('img', 'wedding-6', 'Svatební look – romantický styling'),
        ('panel', '04', 'Dlouhotrvající výsledek', 'Profesionální produkty a techniky udrží váš svatební look svěží a připravený na fotografie od obřadu až po poslední tanec.', False),
        ('img', 'wedding-12', 'Styling nevěsty a družiček'),
    ])
    h += ox_pricing('Ceník a služby', 'Balíčky svatebního líčení', 'Cena se odvíjí od data, místa a rozsahu. Osobní nabídku pošlu do 24 hodin.', [
        ('Kompletní svatební balíček', 'Na vyžádání', ['Osobní zkušební líčení', 'Líčení v den svatby', 'Umělé řasy v ceně', 'Sada na dotyky', 'Doprava po Praze'], 'Poptat balíček +'),
        ('Svatební doprovod &amp; cestování', 'Na vyžádání', ['Líčení družiček', 'Maminka nevěsty', 'Sladěný look doprovodu', 'Cestování po ČR', 'Evropské destinace'], 'Poptat doprovod +'),
    ])
    h += steps('Průběh svatebního líčení', 'jak to probíhá', [
        ('Úvodní konzultace', 'Probereme vaši představu, šaty a místo konání – osobně, telefonicky nebo přes videohovor, což je ideální pro zahraniční nevěsty plánující destinační svatbu v Praze.'),
        ('Zkušební líčení', 'Obvykle 4–8 týdnů před svatbou. Vyzkoušíme kompletní look, doladíme odstíny a techniky a vše zdokumentujeme zkušebními fotografiemi.'),
        ('Líčení v den svatby', 'Přijedu do hotelu, na místo konání či domů. Doprovod líčím jako první, nevěstu jako poslední, aby byl její look co nejsvěžejší pro obřad i fotografie.'),
        ('Sada na dotyky a finální kontrola', 'Dostanete osobní sadu na dotyky s klíčovými produkty použitými na vaši pleť, takže váš look zůstane perfektní až do posledního tance.'),
    ], 'Od první konzultace až po finální dotyky ve svatební den – přesně takto vypadá spolupráce, když si jako svou svatební vizážistku v Praze zarezervujete Nikol Pavlovou.')
    h += gallery('Nedávné svatební looky', 'vybrané práce', 'Zobrazit celé portfolio', '/portfolio/', [
        ('wedding-5', 'Svatební líčení – jemný svatební glow, Praha'), ('wedding-7', 'Svatební líčení – klasická svatební krása'),
        ('wedding-9', 'Svatební líčení – destinační svatba Praha'), ('wedding-11', 'Svatební líčení – zářivá svatební pleť'),
        ('wedding-12', 'Líčení svatebního doprovodu – nevěsta a družičky'), ('wedding-13', 'Svatební líčení – přirozená svatební krása'),
        ('wedding-14', 'Svatební líčení – jemný glamour, Praha'), ('wedding-15', 'Svatební líčení od Nikol Pavlové')])
    h += reviews(LANG, 'nevěsty a svatební focení', pick('shirley', 'polinashu', 'erika_w'), top=False)
    h += f'''<section class="sec" aria-labelledby="guide-h">
<div class="wrap guide">
<aside><p class="lbl red">Průvodce svatebním líčením</p><h2 class="big-h" id="guide-h">Svatební líčení v Praze</h2>
<nav class="toc" aria-label="Obsah průvodce"><a href="#g1">Co nabízí svatební vizážistka</a><a href="#g2">Jak dlouho dopředu rezervovat</a><a href="#g3">Zkušební líčení</a><a href="#g4">Anglicky mluvící vizážistka</a><a href="#g5">Styly svatebního líčení</a></nav></aside>
<article>
<p class="opener">Výběr té správné svatební vizážistky v Praze patří k nejdůležitějším rozhodnutím každé nevěsty. Líčení musí krásně vypadat na fotografiích, vydržet od rána až po hostinu a hlavně – musíte se v něm cítit jako vy sama ve svůj nejvýznamnější den.</p>
<section id="g1"><h3>Co nabízí svatební vizážistka v Praze?</h3><p class="body">Profesionální <b>svatební vizážistka v Praze</b> jako Nikol Pavlova poskytuje kompletní službu: úvodní konzultaci k pochopení vaší představy a typu pleti, <b>zkušební líčení</b> pro doladění looku předem a líčení na místě ve vašem ubytování či na místě konání ráno v den svatby.</p></section>
<section id="g2"><h3>Jak dlouho dopředu rezervovat?</h3><p class="body">Pro <b>svatební líčení v Praze</b> se vizážistky obvykle rezervují 6–12 měsíců předem, zvláště v hlavní sezóně od května do září. Praha je jedním z nejoblíbenějších měst pro destinační svatby v Evropě, takže poptávka po anglicky mluvících vizážistkách je v létě vysoká. Včasná rezervace zajistí váš termín a ponechá čas na zkušební líčení.</p></section>
<section id="g3"><h3>Co je zkušební líčení a proč je důležité?</h3><p class="body"><b>Zkušební líčení</b> je generální zkouška líčení, obvykle 4–8 týdnů před svatbou. Vyzkoušíte odstín make-upu, líčení očí, barvu rtů i řasy a vzniknou referenční fotografie, podle kterých se řídí líčení ve svatební den. Zkušební líčení je součástí každého svatebního balíčku Nikol Pavlové.</p></section>
<section id="g4"><h3>Anglicky mluvící svatební vizážistka v Praze</h3><p class="body">Pro zahraniční nevěsty, expaty a páry plánující <b>destinační svatbu v České republice</b> odstraní spolupráce s <b>anglicky mluvící svatební vizážistkou v Praze</b> velkou část stresu. Nikol mluví plynně anglicky, česky a ukrajinsky – přirozená volba pro mezinárodní svatby a klienty z Velké Británie, USA, Irska, Austrálie i z celé Evropy.</p></section>
<section id="g5"><h3>Styly svatebního líčení v Praze</h3>
<dl class="rows"><div><dt class="k">Jemný svatební glow</dt><dd class="v">rosná, zářivá pleť s decentně zvýrazněnýma očima</dd></div><div><dt class="k">Glamour večerní</dt><dd class="v">plné krytí, výrazné řasy, zvýrazněné oči</dd></div><div><dt class="k">Přirozený nude</dt><dd class="v">líčení, které zvýrazní, ne změní</dd></div><div><dt class="k">Old Hollywood</dt><dd class="v">výrazná linka, červené rty, dokonalá pleť</dd></div><div><dt class="k">Bohémský styl</dt><dd class="v">teplé tóny, přírodní paleta, romantika</dd></div></dl>
<p class="body" style="margin-top:16px">Během konzultace vám Nikol pomůže vybrat styl, který nejlépe sedne k vaší pleti, šatům, místu konání i tématu svatby.</p></section>
</article>
</div>
</section>
'''
    h += faq(LANG, 'otázky o svatebním líčení', faq_items)
    h += teaser(LANG, ['nyx', 'summer'])
    h += tiles(LANG, [('Večerní líčení', '/vecerni-liceni/', 'evening-5'), ('Kurzy líčení', '/kurzy-liceni/', 'course')])
    h += footer(LANG, 'Rezervujte si svatební konzultaci', 'Kontaktujte mě', 'Působím v Praze, ČR · K dispozici pro cestování po Evropě. Osobní nabídka do 24 hodin.',
                (CAL, 'Rezervovat termín online +'))
    write(path, h)


# ---------------------------------------------------------------- GENERIC SERVICE (Večerní / Nude / Komerční)
def service(cfg):
    path = cfg['path']
    faq_items = cfg['faq']
    crumb_items = [HOME, SVC, (cfg['crumb'], None)]
    sch = S.service_page(LANG, path, cfg['title'], cfg['desc'], cfg['service_name'], cfg['service_type'],
                         f"/assets/img/{cfg['hero_img']}-800.webp", [('Domů', '/'), ('Služby', '/#services'), (cfg['crumb'], path)], faq_items, cfg['offers'])
    h = head(LANG, cfg['title'], cfg['desc'], path, alts(path, cfg['en']), SITE + f"/assets/img/{cfg['hero_img']}-800.webp", sch,
             preload(cfg['hero_img'], '(max-width: 900px) 100vw, 50vw'))
    h += header(LANG, path, cfg['en'])
    h += hero_split(LANG, cfg['tone'], crumb_items, cfg['big'], cfg['sub'], cfg['lead'], cfg['buttons'], cfg['hero_img'], cfg['hero_alt'])
    h += marquee(cfg['marquee'])
    h += intro('O službě', cfg['intro_title'], cfg['intro_tag'], cfg['intro_imgs'], cfg['intro_body'], cfg['chips'])
    h += checker(cfg['grid_title'], cfg['grid_sub'], cfg['grid'])
    h += ox_pricing('Ceník', cfg['price_title'], cfg['price_note'], [cfg['price_col']])
    h += steps(cfg['steps_title'], 'jak to probíhá', cfg['steps'])
    h += gallery(cfg['gal_title'], 'vybrané práce', 'Zobrazit celé portfolio', '/portfolio/', cfg['gallery'], c3=len(cfg['gallery']) < 8)
    if cfg.get('banner'):
        h += cfg['banner']
    h += reviews(LANG, cfg['rv_sub'], cfg['reviews'], top=False)
    h += faq(LANG, cfg['faq_sub'], faq_items)
    h += teaser(LANG, cfg.get('posts', []))
    h += tiles(LANG, cfg['related'])
    h += footer(LANG, cfg['f_label'], 'Kontaktujte mě', cfg['f_text'], cfg.get('f_primary'))
    write(path, h)


BOOK_FAQ = ('Jak si mohu rezervovat termín?', f'Rezervovat můžete <a href="{CAL}">online přes Calendly</a>, telefonicky nebo SMS na <a href="tel:{TEL}">{TEL_H}</a>, e-mailem na <a href="mailto:{MAIL}">{MAIL}</a> nebo přes Instagram <a href="{IG}">@nikol__mua</a>. Obvykle odpovídám do několika hodin.')

EVENING = dict(
    posts=['nyx', 'summer'],
    path='/vecerni-liceni/', en='/en/evening-makeup/', crumb='Večerní líčení', tone='tone-ox',
    title='Večerní líčení Praha | Plesový a koktejlový make-up – Nikol Pavlova',
    desc='Večerní a plesové líčení v Praze. Glamour looky na plesy, galavečery, maturitní bály a večírky – smoky eyes, výrazné rty a make-up, který vydrží celý večer.',
    service_name='Večerní líčení Praha', service_type='Večerní a plesový make-up',
    offers=['Večerní líčení', 'Plesový make-up', 'Make-up na focení', 'Líčení na akce'],
    big='Večerní<br>líčení', sub='v Praze – plesy, galavečery a večírky',
    lead='Glamour looky na galavečery, koktejlové akce, plesy, maturitní bály a speciální události v Praze. Smoky eyes, vymodelované lícní kosti, výrazné rty a zářivá pleť – dokončené technikami, které vydrží pod fotografickým bleskem i v ambientním večerním světle.',
    buttons=[('Rezervovat termín +', CAL), ('Styly líčení', '#grid-h')], hero_img='evening-5', hero_alt='Večerní líčení Praha – elegantní glamour look',
    marquee=['Plesy', 'Galavečery', 'Koktejlové akce', 'Maturitní bály', 'Smoky eyes', 'Výrazné rty'],
    intro_title='Výrazný look, ve kterém se budete cítit sebejistě', intro_tag='od jemného soft glamu po dramatické smoky eyes',
    intro_imgs=[('evening-1', 'Večerní look – glamour smoky eye'), ('evening-3', 'Večerní look – výrazný ret a čistá pleť')],
    intro_body='Každé večerní líčení ladím k vašim šatům, účesu, světlu a charakteru akce. Na začátku si krátce řekneme, jak výrazný look chcete. Přijedu za vámi domů, do hotelu nebo na místo konání kdekoli v Praze; mimo Prahu je možnost dojezdu po domluvě.',
    chips=['Plesy, maturitní bály a galavečery', 'Koktejlové akce, večírky a oslavy', 'Make-up na focení', 'Česky i anglicky'],
    grid_title='Styly líčení', grid_sub='od soft glamu po smoky eyes', grid=[
        ('img', 'evening-13', 'Soft glam večerní look'), ('panel', '01', 'Soft glam', 'Zářivá pleť, jemně zvýrazněné oči a elegantní, nadčasový výsledek.', False),
        ('img', 'evening-12', 'Dramatický oční styling'), ('panel', '02', 'Smoky eyes', 'Kouřové oči a dramatický oční styling pro velké večery.', True),
        ('panel', '03', 'Výrazné rty', 'Čistá pleť a výrazný ret jako hlavní akcent celého looku.', True), ('img', 'evening-16', 'Výrazný kontur a rty'),
        ('panel', '04', 'Ples &amp; maturita', 'Plesový a maturitní styling, který vydrží celou noc i fotografie.', False), ('img', 'evening-4', 'Plesový a maturitní styling')],
    price_title='Speciální příležitosti', price_note='Ceny závisí na typu služby, lokaci a termínu. Napište mi detaily vaší akce a do 24 hodin vám pošlu osobní cenovou nabídku.',
    price_col=('Večer &amp; akce', 'Na vyžádání', ['Večerní líčení', 'Plesový make-up', 'Make-up na focení', 'Líčení na akce'], 'Poptat cenu +'),
    steps_title='Průběh večerního líčení', steps=[
        ('Poptávka', 'Napište mi datum, místo a typ akce – telefonicky, SMS, e-mailem nebo přes Instagram. Obvykle odpovídám do několika hodin.'),
        ('Nabídka a look', 'Do 24 hodin pošlu osobní nabídku. Probereme šaty, účes a jak výrazný look si přejete.'),
        ('Líčení', 'U vás doma, v hotelu nebo na místě konání – s produkty, které vydrží celý večer.'),
        ('Finální kontrola', 'Poslední úpravy před odchodem a tipy, jak si look během večera osvěžit.')],
    gal_title='Večerní looky', gallery=[('evening-6', 'Večerní look – svůdný oční make-up'), ('evening-7', 'Večerní look – zářivý večerní glam'),
        ('evening-10', 'Večerní look – klasický večerní glam'), ('evening-8', 'Večerní look – výrazný barevný oční look'),
        ('evening-11', 'Večerní look – make-up na galavečer'), ('evening-15', 'Večerní look – zářivá večerní tvář'),
        ('evening-14', 'Večerní look – moderní večerní styling'), ('evening-17', 'Večerní look – finální dotek večerního glamu')],
    rv_sub='líčení, které vydrží do večera', reviews=pick('nelli', 'stepanka', 'glenn'),
    faq_sub='otázky o večerním líčení', faq=[
        ('Jak dlouho dopředu si rezervovat termín?', 'Pro večerní líčení a focení obvykle stačí 2–3 týdny, někdy lze zařídit i last-minute termín – stačí mě kontaktovat.'),
        ('Kolik stojí večerní líčení v Praze?', 'Ceny závisí na typu služby, lokaci a termínu. Napište mi prosím detaily vaší akce a do 24 hodin vám pošlu osobní cenovou nabídku.'),
        ('Přijedete za mnou?', 'Ano. Pracuji ve všech pražských čtvrtích – včetně Prahy 1 (Staré Město), Prahy 2 (Vinohrady) a Prahy 7 – a cestuji i do dalších měst v České republice a po Evropě.'),
        ('Mluvíte anglicky?', 'Ano, mluvím plynně česky a anglicky, takže se domluvíme i s mezinárodními klienty a expaty žijícími v Praze.'), BOOK_FAQ],
    related=[('Svatební líčení', '/svatebni-liceni/', 'wedding-5'), ('Komerční líčení', '/komercni-liceni/', 'commercial-4')],
    f_label='Rezervujte si večerní líčení', f_text='Působím v Praze, ČR · Možnost dojezdu. Osobní nabídka do 24 hodin.')

NUDE = dict(
    posts=['summer', 'nyx'],
    path='/nude-liceni/', en='/en/nude-makeup/', crumb='Nude makeup', tone='tone-blush',
    title='Nude make-up Praha | Přirozené líčení – vizážistka Nikol Pavlova',
    desc='Přirozený nude make-up v Praze. Jemné líčení zaměřené na pleť pro zásnubní focení, portréty a civilní obřady – zdravá, zářivá pleť bez efektu „nalíčenosti“.',
    service_name='Nude make-up Praha', service_type='Přirozené líčení',
    offers=['Příprava pleti', 'Lehký podklad a korektor', 'Jemné zvýraznění očí a obočí', 'Přirozené tváře a rty'],
    big='Nude<br>makeup', sub='v Praze – líčení, které zvýrazní, ne změní',
    lead='Jemné looky zaměřené na pleť, které zdůrazňují přirozené rysy bez efektu „nalíčenosti“. Ideální pro zásnubní focení, denní portréty, civilní obřady a klientky, které preferují téměř neviditelný make-up se zdravě zářivou pletí.',
    buttons=[('Rezervovat termín +', CAL), ('Pro koho', '#grid-h')], hero_img='nude-1', hero_alt='Nude makeup Praha – přirozený no-makeup look',
    marquee=['No-makeup look', 'Zdravá záře', 'Dewy pleť', 'Zásnubní focení', 'Civilní obřady'],
    intro_title='Zdravá, zářivá pleť a vaše vlastní rysy', intro_tag='jako vy ve své nejlepší formě',
    intro_imgs=[('nude-2', 'Nude look – jemná přirozená záře'), ('nude-3', 'Nude look – svěží dewy pleť')],
    intro_body='Základem nude looku je pečlivá příprava pleti a lehké vrstvy produktů, které s pletí splynou. Make-up ladím k vašemu typu pleti, tónu a příležitosti, aby výsledek působil svěže na fotografiích i naživo – od rána do večera.',
    chips=['Příprava pleti jako základ', 'Lehké krytí bez efektu masky', 'Jemně zvýrazněné oči, obočí a rty', 'Česky i anglicky'],
    grid_title='Pro koho', grid_sub='kdy se hodí nude look', grid=[
        ('panel', '01', 'Zásnubní focení', 'Přirozený look, který na fotografiích působí svěže a nadčasově.', False), ('img', 'wedding-13', 'Přirozená svatební krása'),
        ('panel', '02', 'Denní portréty', 'Pracovní, profilové i osobní portréty v denním světle.', True), ('img', 'nude-3', 'Svěží dewy pleť'),
        ('img', 'wedding-1', 'Jemný svatební make-up'), ('panel', '03', 'Civilní obřady', 'Jemný svatební look pro menší a civilní obřady.', True),
        ('img', 'nude-2', 'Jemná přirozená záře'), ('panel', '04', 'Téměř bez make-upu', 'Zdravě zářivá pleť a minimum produktu.', False)],
    price_title='Přirozený look', price_note='Ceny závisí na typu služby, lokaci a termínu. Napište mi detaily a do 24 hodin vám pošlu osobní cenovou nabídku.',
    price_col=('Nude makeup', 'Na vyžádání', ['Příprava pleti', 'Lehký podklad a korektor', 'Jemné zvýraznění očí a obočí', 'Přirozené tváře a rty'], 'Poptat cenu +'),
    steps_title='Průběh líčení', steps=[
        ('Poptávka', 'Napište mi datum, místo a příležitost. Obvykle odpovídám do několika hodin.'),
        ('Příprava pleti', 'Look začíná péčí o pleť – podle jejího typu a potřeb.'),
        ('Lehké vrstvy', 'Krytí jen tam, kde je potřeba, a jemné zvýraznění vašich rysů.'),
        ('Finální kontrola', 'Kontrola v denním světle, aby look působil přirozeně naživo i na fotkách.')],
    gal_title='Přirozené looky', gallery=[('nude-1', 'Nude look – přirozený no-makeup look, Praha'), ('nude-2', 'Nude look – jemná přirozená záře'), ('nude-3', 'Nude look – svěží dewy pleť')],
    banner=f'''<section class="sec--tight" aria-label="Kurzy líčení"><div class="wrap"><a class="banner" href="/kurzy-liceni/"><span class="txt"><span class="lbl pink">Kurzy líčení</span><span class="mid-h">Chcete se přirozený look naučit sama?</span><span class="serif" style="font-size:20px;color:#E9DCD8">V osobní lekci probereme přípravu pleti, teorii barev a techniky přímo na vaší tváři.</span><span class="btn btn--pink">Kurzy líčení →</span></span><span class="img">{I('course', '', sizes='(max-width: 900px) 100vw, 50vw', style='object-position:50% 15%')}</span></a></div></section>
''',
    rv_sub='přirozená, svěží pleť', reviews=pick('karin', 'marie', 'beata'),
    faq_sub='otázky o nude make-upu', faq=[
        ('Hodí se nude look i na svatbu?', 'Ano. Přirozený nude patří mezi styly svatebního líčení, které nabízím – ideální pro civilní obřady a nevěsty, které chtějí vypadat jako samy sebe. Více na stránce <a href="/svatebni-liceni/">Svatební líčení</a>.'),
        ('Kolik stojí nude make-up?', 'Ceny závisí na typu služby, lokaci a termínu. Napište mi prosím detaily a do 24 hodin vám pošlu osobní cenovou nabídku.'),
        ('Jak dlouho dopředu rezervovat?', 'Pro focení a běžné akce obvykle stačí 2–3 týdny, někdy lze zařídit i last-minute termín – stačí mě kontaktovat.'), BOOK_FAQ],
    related=[('Svatební líčení', '/svatebni-liceni/', 'wedding-5'), ('Večerní líčení', '/vecerni-liceni/', 'evening-5')],
    f_label='Rezervujte si nude makeup', f_text='Působím v Praze, ČR · Možnost dojezdu. Osobní nabídka do 24 hodin.')

COMMERCIAL = dict(
    posts=['summer', 'nyx'],
    path='/komercni-liceni/', en='/en/commercial-makeup/', crumb='Komerční líčení', tone='tone-ink',
    title='Komerční a editoriální líčení Praha | Make-up na focení – Nikol Pavlova',
    desc='Komerční a editoriální make-up v Praze pro focení, kampaně, lookbooky a video. Líčení přizpůsobené světlu a konceptu s on-set retušemi během celého dne.',
    service_name='Komerční a editoriální líčení Praha', service_type='Make-up pro focení a reklamu',
    offers=['Konzultace konceptu a looků', 'Líčení podle světla a zadání', 'On-set retuše během dne', 'Cestování po ČR i Evropě'],
    big='Komerční<br>líčení', sub='v Praze – focení, kampaně a editorial',
    lead='Líčení pro focení, brandové kampaně, lookbooky, magazínové editorialy a video obsah. Přizpůsobeno světlu a konceptu každého focení – od čisté beauty práce až po výrazný editoriální styling – s on-set retušemi v průběhu celého produkčního dne.',
    buttons=[('Poslat zadání +', f'mailto:{MAIL}'), ('Typy zakázek', '#grid-h')], hero_img='commercial-4', hero_alt='Komerční líčení – focení pro beauty značku',
    marquee=['Beauty', 'Kampaně', 'Lookbooky', 'Editorial', 'Video obsah', 'On-set retuše'],
    intro_title='Make-up, který funguje před objektivem', intro_tag='od čisté beauty práce po výrazný editorial',
    intro_imgs=[('commercial-2', 'Komerční look – kampaňové focení'), ('commercial-3', 'Komerční look – magazínový editorial styling')],
    intro_body='Spolupracuji na focení v Praze i mimo ni. Před focením si projdeme koncept, světlo a počet looků, aby make-up odpovídal zadání a vydržel celý produkční den. Během focení zůstávám na place a průběžně dělám retuše, takže každý záběr vypadá stejně čistě jako ten první.',
    chips=['Přizpůsobeno světlu a konceptu', 'On-set retuše během celého dne', 'Cestování po ČR i Evropě', 'Česky i anglicky'],
    grid_title='Typy zakázek', grid_sub='na čem pracuji', grid=[
        ('img', 'commercial-1', 'Editorialové focení'), ('panel', '01', 'Beauty &amp; kampaně', 'Čistá beauty práce a brandové kampaně pro kosmetické i módní značky.', False),
        ('img', 'commercial-3', 'Magazínový editorial'), ('panel', '02', 'Editorial', 'Magazínové editorialy a výrazný styling podle konceptu.', True),
        ('panel', '03', 'Lookbooky', 'Konzistentní looky pro lookbooky a módní kolekce.', True), ('img', 'commercial-5', 'Fashion editorial líčení'),
        ('panel', '04', 'Video obsah', 'Make-up pro video a obsah ve vysokém rozlišení.', False), ('img', 'commercial-6', 'Mediální focení')],
    price_title='Komerční zakázky', price_note='Komerční zakázky cením individuálně podle rozsahu, lokace a termínu. Napište mi detaily focení a do 24 hodin vám pošlu osobní cenovou nabídku.',
    price_col=('Focení &amp; produkce', 'Na vyžádání', ['Konzultace konceptu a looků', 'Líčení podle světla a zadání', 'On-set retuše během dne', 'Cestování po ČR i Evropě'], 'Poptat focení +'),
    steps_title='Průběh spolupráce', steps=[
        ('Zadání', 'Pošlete mi datum, lokaci, koncept a počet looků. Obvykle odpovídám do několika hodin.'),
        ('Nabídka a příprava', 'Do 24 hodin pošlu nabídku a připravím looky podle konceptu a světla.'),
        ('Den focení', 'Líčení na place a změny looků podle harmonogramu produkce.'),
        ('On-set retuše', 'Průběžné kontroly a retuše, aby make-up vypadal perfektně v každém záběru.')],
    gal_title='Komerční looky', gallery=[('commercial-1', 'Komerční look – editorialové focení, Praha'), ('commercial-2', 'Komerční look – kampaňové focení'),
        ('commercial-3', 'Komerční look – magazínový editorial styling'), ('commercial-4', 'Komerční look – focení pro beauty značku'),
        ('commercial-5', 'Komerční look – fashion editorial líčení'), ('commercial-6', 'Komerční look – mediální focení')],
    rv_sub='focení a modeling', reviews=pick('polina', 'zoe_c', 'glenn'),
    faq_sub='otázky o komerčním líčení', faq=[
        ('Kolik stojí komerční líčení?', 'Komerční zakázky cením individuálně podle typu služby, lokace a termínu. Napište mi detaily a do 24 hodin vám pošlu osobní cenovou nabídku.'),
        ('Jak dlouho dopředu rezervovat focení?', 'Pro focení obvykle stačí 2–3 týdny, někdy lze zařídit i last-minute termín – stačí mě kontaktovat.'),
        ('Jezdíte na focení mimo Prahu?', 'Ano. Působím v Praze a za focením cestuji do dalších měst v České republice i po Evropě.'),
        ('Komunikujete anglicky?', 'Ano, mluvím plynně česky a anglicky, takže se domluvíme i s mezinárodními týmy.'), BOOK_FAQ],
    related=[('Večerní líčení', '/vecerni-liceni/', 'evening-5'), ('Nude makeup', '/nude-liceni/', 'nude-1')],
    f_label='Plánujete focení?', f_text='Pošlete mi datum, lokaci a koncept – osobní nabídku pošlu do 24 hodin.', f_primary=(f'mailto:{MAIL}', 'Poslat zadání e-mailem +'))


# ---------------------------------------------------------------- COURSES
def courses():
    path = '/kurzy-liceni/'
    title = 'Kurz líčení Praha | Individuální kurzy líčení – Nikol Pavlova'
    desc = 'Individuální kurzy líčení v Praze s profesionální vizážistkou Nikol Pavlovou. Osobní kurz líčení pro začátečnice i budoucí vizážistky – příprava pleti, teorie barev, techniky. Rezervujte termín.'
    faq_items = [
        ('Pro koho jsou kurzy líčení vhodné?', 'Kurzy jsou vhodné pro každého – úplné začátečnice učící se líčit samy sebe, přípravu na zvláštní příležitost i budoucí vizážistky budující profesionální dovednosti. Každý kurz je přizpůsoben vaší úrovni a cílům.'),
        ('Co kurz líčení obsahuje?', 'Individuální lekce zahrnují přípravu pleti, teorii barev, make-up a podklad, líčení očí a řasy, konturu a rozjasnění a výběr nástrojů a produktů. Pracujeme na vašem vlastním obličeji, abyste looky zvládli i doma.'),
        ('Jsou lekce individuální, nebo skupinové?', 'Lekce jsou individuální, takže se celá lekce věnuje výhradně vám. Menší soukromé skupinové lekce lze domluvit na vyžádání.'),
        ('Mám si přinést vlastní produkty?', 'Můžete přijít s produkty, které už máte, abychom pracovali s tím, co vlastníte, a doporučili vylepšení – nebo během lekce použijeme profesionální produkty. Po lekci dostanete osobní seznam produktů a nástrojů.'),
        ('Jak dlouho kurz trvá a kolik stojí?', 'Délka i cena závisí na vaší úrovni a cílech – od jedné cílené lekce po ucelenější program. Napište Nikol, co se chcete naučit, a do 24 hodin pošle osobní cenovou nabídku.'),
        ('Jsou kurzy dostupné v angličtině?', 'Ano. Nikol učí plynně anglicky i česky, takže jsou kurzy pohodlné pro zahraniční klienty a expaty žijící v Praze.'),
        ('Jak si rezervovat kurz líčení v Praze?', f'Rezervujte si online přes <a href="{CAL}">Calendly</a>, nebo kontaktujte Nikol telefonicky/SMS na <a href="tel:{TEL}">{TEL_H}</a>, e-mailem <a href="mailto:{MAIL}">{MAIL}</a> či na Instagramu <a href="{IG}">@nikol__mua</a>.'),
    ]
    h = head(LANG, title, desc, path, alts(path, '/en/courses/'), SITE + '/img/courses/IMG_7417.jpg', S.load('cs-courses'),
             preload('course', '(max-width: 900px) 100vw, 50vw'))
    h += header(LANG, path, '/en/courses/')
    h += hero_split(LANG, 'tone-sand', [HOME, SVC, ('Kurzy líčení', None)], 'Kurzy<br>líčení', 'v Praze – naučte se líčit jako profesionál',
                    'Individuální kurzy líčení v Praze – ať už se chcete naučit líčit samy sebe na každý den, nebo budovat profesionální dovednosti jako budoucí vizážistka. Pracujeme na vašem vlastním obličeji, vaším tempem.',
                    [('Rezervovat kurz online +', CAL), ('Varianty kurzu', '#packages')], 'course', 'Individuální kurz líčení v Praze s Nikol Pavlovou', '50% 15%')
    h += marquee(['Individuálně', 'Na vlastní tváři', 'Česky i anglicky', 'Pro začátečnice i profíky', 'Seznam produktů s sebou'])
    h += intro('O kurzu', 'Kurz líčení přesně na míru vám', 'žádný pevný scénář, jen to, co se chcete naučit', [],
               'Jako profesionální <b>vizážistka a lektorka v Praze</b> vedu individuální <b>kurzy líčení</b> postavené na vaší úrovni a cílech. Věnujeme se přesně tomu, co se chcete naučit, a pracujeme na vašem vlastním obličeji, abyste každý look zvládli i doma. Ať už jste štětec nikdy nedržela, nebo jste budoucí vizážistka pilující techniku, každá lekce je praktická, uvolněná a konkrétní – a odcházíte s osobním seznamem produktů a nástrojů.',
               ['Individuálně – celá lekce je jen o vás', 'Pro začátečnice i budoucí profesionálky', 'Výuka česky i anglicky', 'Osobní seznam produktů a nástrojů s sebou'],
               (CAL, 'Rezervovat lekci +'))
    h += checker('Co se naučíte', 'náplň kurzu', [
        ('img', 'nude-1', 'Přirozené denní líčení'), ('panel', '01', 'Příprava pleti &amp; podklad', 'Péče před líčením, podklad a dokonalý make-up, korektor a báze pro váš typ pleti.', False),
        ('img', 'nude-2', 'Jemný přirozený glow'), ('panel', '02', 'Teorie barev', 'Mapování obličeje a teorie barev, abyste volili odstíny, které sluší vašim rysům a tónu.', True),
        ('panel', '03', 'Oči &amp; řasy', 'Roztírání stínů, linka a aplikace umělých řas – od jemného denního po výrazný večerní look.', True), ('img', 'evening-7', 'Výrazné líčení očí'),
        ('panel', '04', 'Nástroje &amp; produkty', 'Kontura, tvářenka a rozjasnění a jak vybrat správné štětce a sestavit vlastní kosmetickou tašku.', False), ('img', 'evening-5', 'Večerní glamour look')])
    h += ox_pricing('Varianty kurzu', 'Vyberte si svůj kurz', 'Délka i cena kurzu se odvíjí od vaší úrovně a cílů. Osobní nabídku pošlu do 24 hodin.', [
        ('Osobní kurz líčení', 'Na vyžádání', ['Líčení pro sebe na každý den', 'Příprava pleti a podklad', 'Oči, řasy a finální look', 'Osobní seznam produktů', 'Individuálně v Praze'], 'Poptat kurz +'),
        ('Kurz pro budoucí vizážistky', 'Na vyžádání', ['Profesionální techniky', 'Teorie barev &amp; mapování', 'Hygiena &amp; kosmetická taška', 'Práce na klientech', 'Na míru vašim cílům'], 'Poptat kurz +')])
    h += steps('Průběh kurzu', 'jak to probíhá', [
        ('Úvodní konzultace', 'Probereme vaši úroveň, co se chcete naučit a looky, které máte rádi – osobně, telefonicky nebo přes videohovor pro zahraniční studenty.'),
        ('Plán na míru', 'Připravím plán lekce podle vašich cílů, typu pleti a produktů, které už máte, aby byla každá minuta relevantní.'),
        ('Praktická lekce', 'Pracujeme krok za krokem na vašem vlastním obličeji. Líčíte sami s mým vedením, aby vám techniky skutečně zůstaly.'),
        ('Seznam produktů &amp; podpora', 'Odcházíte s osobním seznamem produktů a nástrojů a poznámkami, abyste vše s jistotou zvládli i doma.')],
        'Každý kurz líčení v Praze je postavený na vás. Takto vypadá spolupráce od první zprávy až po následnou podporu.')
    h += f'''<section class="sec--tight" aria-labelledby="insp-h"><div class="wrap">
{sec_head('Looky, které se naučíte vytvořit', 'inspirace', '<a class="link-arrow" href="/portfolio/">Zobrazit celé portfolio →</a>', hid='insp-h')}
<ul class="cards3" role="list" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))">
<li><figure class="pcard"><div class="ph">{I('nude-1', 'Přirozené denní líčení – kurz líčení Praha')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Přirozený denní look</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('nude-2', 'Jemný přirozený glow – technika z lekce líčení')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Jemný glow</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-5', 'Večerní glamour look – kurz líčení Praha')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Večerní glamour</figcaption></figure></li>
<li><figure class="pcard"><div class="ph">{I('evening-7', 'Výrazné líčení očí – technika z lekce líčení')}</div><figcaption class="wide" style="font-size:15px;font-weight:600">Výrazné oči</figcaption></figure></li>
</ul></div></section>
<section class="sec sec--blush" aria-labelledby="students-h"><div class="wrap">
{sec_head('Spokojené studentky', 'co říkají o lekcích', f'<a class="btn" href="{CAL}">Rezervovat lekci +</a>', hid='students-h')}
<div class="quotes3">
<figure><blockquote><p>„Konečně rozumím tomu, jak se nalíčit. Nikol vše srozumitelně vysvětlila a nechala mě líčit samotnou – teď tyhle techniky používám každý den.“</p></blockquote><figcaption class="lbl"><cite>Tereza H.</cite> <span class="muted2">· Osobní lekce</span></figcaption></figure>
<figure><blockquote><p>„Jako začínající vizážistka jsem ocenila profesionální lekci – reálná technika, hygiena a rady ohledně produktů, které z videí nezískáte.“</p></blockquote><figcaption class="lbl"><cite>Marta S.</cite> <span class="muted2">· Profi kurz</span></figcaption></figure>
<figure><blockquote><p>„Jako expatka v Praze jsem si zarezervovala lekci v angličtině. Uvolněné, osobní a praktické – odešla jsem se seznamem produktů, který fakt používám.“</p></blockquote><figcaption class="lbl"><cite>Olivia R.</cite> <span class="muted2">· Osobní lekce</span></figcaption></figure>
</div></div></section>
<section class="sec" aria-labelledby="guide-h"><div class="wrap guide">
<aside><p class="lbl red">Průvodce kurzem líčení</p><h2 class="big-h" id="guide-h">Kurzy líčení v Praze</h2></aside>
<article>
<p class="opener">Hledáte kurz líčení v Praze? Ať už chcete konečně zvládnout svůj každodenní look, nebo udělat první kroky jako profesionál, individuální lekce je nejrychlejší cesta, jak se naučit techniky, které fungují právě na vašem obličeji.</p>
<section><h3>Pro koho jsou kurzy líčení v Praze?</h3><p class="body">Kurzy líčení jsou vhodné pro úplné začátečnice, pro přípravu na zvláštní příležitost i pro budoucí vizážistky. Protože jsou lekce individuální, obsah se přizpůsobí vaší úrovni – nikdo nezůstane pozadu a nikdo se nenudí.</p></section>
<section><h3>Co obsahuje lekce líčení?</h3><p class="body">Typická <b>lekce líčení</b> zahrnuje přípravu pleti, teorii barev a mapování obličeje, make-up a podklad, líčení očí a řasy, konturu a rozjasnění a výběr správných nástrojů a produktů. Líčíte sami s vedením, takže vám dovednosti zůstanou.</p></section>
<section><h3>Individuální vs. skupinové kurzy líčení</h3><p class="body">Skupinové kurzy mohou být zábava, ale <b>individuální lekce líčení</b> znamená, že celá lekce je postavená na vašich rysech, typu pleti a cílech. Pro většinu lidí, kteří se chtějí naučit rychleji a více si zapamatovat, jsou soukromé lekce lepší volbou.</p></section>
<section><h3>Kurzy líčení v Praze v angličtině</h3><p class="body">Pro expaty a zahraniční klienty je důležité učit se ve svém jazyce. Nikol učí plynně <b>anglicky i česky</b>, takže je každý krok jasný a můžete se kdykoli zeptat.</p></section>
<section><h3>Co po kurzu zvládnete</h3><dl class="rows"><div><dt class="k">Denní líčení</dt><dd class="v">rychlý, lichotivý look, který zvládnete s jistotou</dd></div><div><dt class="k">Líčení na příležitost</dt><dd class="v">elegantní look na události, rande a focení</dd></div><div><dt class="k">Profesionální techniku</dt><dd class="v">základ pro práci vizážistky</dd></div><div><dt class="k">Chytrý nákup</dt><dd class="v">seznam produktů a nástrojů na míru vám</dd></div></dl>
<p class="body" style="margin-top:16px">Napište Nikol, čeho chcete dosáhnout, a kurz postaví přímo na to – od jedné cílené lekce po ucelenější program.</p></section>
</article></div></section>
'''
    h += faq(LANG, 'otázky o kurzu líčení', faq_items)
    h += teaser(LANG, ['summer', 'nyx'], 'Procvičte si doma', 'tutoriály z blogu')
    h += tiles(LANG, [('Svatební líčení', '/svatebni-liceni/', 'wedding-5'), ('Nude makeup', '/nude-liceni/', 'nude-1')])
    h += footer(LANG, 'Rezervujte si kurz líčení', 'Kontaktujte mě', 'Lekce probíhají v Praze, ČR · Česky nebo anglicky. Osobní cenová nabídka do 24 hodin.',
                (CAL, 'Rezervovat kurz online +'))
    write(path, h)


# ---------------------------------------------------------------- PORTFOLIO
PORTFOLIO_ITEMS = {
    'wedding': ('Svatební', 'Svatební look', ['jemný glam svatební make-up, Praha', 'přirozený zářivý svatební make-up, Praha', 'dlouhotrvající svatební líčení', 'elegantní líčení v den svatby', 'jemná svatební záře, pražská svatba', 'romantický svatební styling', 'klasická svatební krása', 'moderní svatební líčení', 'destination svatba v Praze', 'výsledek svatební zkoušky', 'zářivá svatební pleť', 'styling nevěsty a družiček', 'přirozená svatební krása', 'soft glam svatební líčení', 'svatební líčení od Nikol Pavlové']),
    'evening': ('Večerní', 'Večerní look', ['glamour smoky eye, Praha', 'koktejlový styling', 'výrazný ret a čistá pleť', 'plesový a maturitní styling', 'elegantní glamour večerní make-up', 'svůdný oční make-up', 'zářivý večerní glam', 'výrazný barevný oční look', 'make-up na speciální příležitost', 'klasický večerní glam', 'make-up na galavečer', 'dramatický oční styling', 'soft glam večerní look', 'moderní večerní styling', 'zářivá večerní tvář', 'výrazný kontur a rty', 'finální dotek večerního glamu']),
    'nude': ('Nude', 'Nude look', ['přirozený no-makeup look, Praha', 'jemná přirozená záře', 'svěží dewy pleť']),
    'commercial': ('Komerční', 'Komerční look', ['editorialové focení, Praha', 'kampaňové focení', 'magazínový editorial styling', 'focení pro beauty značku', 'fashion editorial líčení', 'vysoké rozlišení mediální focení']),
    'courses': ('Kurzy', 'Kurz líčení', ['osobní one-on-one lekce v Praze']),
}


NOSCRIPT = '<noscript><style>.pgrid figure[hidden]{display:block}.more-wrap{display:none}</style></noscript>'


def portfolio_grid(lang, items_def, all_label, shown_tpl, more_tpl):
    figs, pills = '', f'<button class="pill" type="button" data-filter="all" aria-pressed="true">{all_label} <small>{sum(len(v[2]) for v in items_def.values())}</small></button>'
    n = 0
    for cat, (label, cap, descs) in items_def.items():
        pills += f'<button class="pill" type="button" data-filter="{cat}" aria-pressed="false">{label} <small>{len(descs)}</small></button>'
        for i, d in enumerate(descs):
            name = 'course' if cat == 'courses' else f'{cat}-{i + 1}'
            c = cap if cat == 'courses' else f'{cap} {i + 1}'
            hid = ' hidden' if n >= 16 else ''
            n += 1
            figs += f'<figure data-cat="{cat}"{hid}>{I(name, f"{c} – {d}", sizes="(max-width: 900px) 50vw, 25vw")}<figcaption class="glass"><b>{c}</b><span>{d}</span></figcaption></figure>'
    return pills, figs


def portfolio():
    path = '/portfolio/'
    title = 'Portfolio líčení Praha – Svatební, Večerní a Komerční Looky | Nikol Pavlova'
    desc = 'Portfolio profesionální vizážistky Nikol Pavlové z Prahy. Prohlédněte si svatební, večerní, nude a komerční líčení pro klientky v České republice i v Evropě.'
    total = sum(len(v[2]) for v in (PORTFOLIO_ITEMS if LANG == 'cs' else EN_ITEMS).values())
    pills, figs = portfolio_grid(LANG, PORTFOLIO_ITEMS, 'Vše', '', '')
    h = head(LANG, title, desc, path, alts(path, '/en/portfolio/'), SITE + '/img/wedding/wedding-1.png', S.load('cs-portfolio'), extra=NOSCRIPT)
    h += header(LANG, 'portfolio', '/en/portfolio/')
    h += f'''<section class="page-head" aria-labelledby="page-h1"><div class="wrap">
{crumbs(LANG, [HOME, ('Portfolio', None)])}
<div class="top"><h1 class="h1" id="page-h1"><span class="big wide">Portfolio</span><span class="sub serif">líčení – Nikol Pavlova, vizážistka Praha</span></h1>
<p class="body">Toto je pečlivě vybraná ukázka prací od <b>Nikol Pavlové</b>, profesionální vizážistky se sídlem v <b>Praze</b>. Portfolio zahrnuje svatební líčení pro svatby v Praze i napříč Evropou, glamour večerní a koktejlový make-up, jemné přirozené nude looky, komerční a editoriální práce pro focení a snímky z osobních kurzů líčení. Každý look je navržen tak, aby zdůraznil přirozenou krásu klientky a odrážel její osobitý styl i charakter dané příležitosti.</p></div>
</div></section>
<section class="sec--tight" aria-labelledby="looks-h">
<div class="wrap">{sec_head('Vyberte si look', 'filtrovat podle kategorie', f'<div class="filters" role="group" aria-label="Kategorie">{pills}</div>', hid='looks-h')}</div>
<div class="pgrid" data-portfolio data-label-shown="Zobrazeno {{n}} z {{t}}" data-label-more="Zobrazit další ({{n}}) ↓" aria-live="polite">{figs}</div>
<div class="more-wrap"><p class="serif muted2" data-status>Zobrazeno {min(16, total)} z {total}</p><button class="pill btn--lg" type="button" data-more>Zobrazit další ({max(0, total - 16)}) ↓</button></div>
</section>
<section class="sec sec--blush" aria-labelledby="cats-h"><div class="wrap">
{sec_head('O každé kategorii', 'uvnitř portfolia', hid='cats-h')}
<div class="cat-rows">
<a href="/svatebni-liceni/"><h3>Svatební líčení →</h3><p>Svatební looky navržené tak, aby vydržely od prvního polibku až po závěrečný tanec. Každá svatební služba zahrnuje předsvatební zkoušku v Praze, líčení v den svatby s dlouhotrvajícími produkty vhodnými pro české letní i zimní podmínky, individuální řasy a osobní touch-up kit. K dispozici pro obřady na Praze 1 (Staré Město), Vinohradech, zámeckých svatbách za Prahou i pro destination svatby po celé Evropě.</p></a>
<a href="/vecerni-liceni/"><h3>Večerní a koktejlový make-up →</h3><p>Glamour looky na galavečery, koktejlové akce, plesy, maturitní bály a speciální události v Praze. Smoky eyes, vymodelované lícní kosti, výrazné rty a zářivá pleť – dokončené technikami, které vydrží jak pod fotografickým bleskem, tak v ambientním večerním světle.</p></a>
<a href="/nude-liceni/"><h3>Nude a přirozený make-up →</h3><p>Jemné looky zaměřené na pleť, které zdůrazňují přirozené rysy bez efektu „nalíčenosti“. Ideální pro zásnubní focení, denní portréty, civilní obřady a klientky, které preferují téměř neviditelný make-up se zdravě zářivou pletí.</p></a>
<a href="/komercni-liceni/"><h3>Komerční a editoriální →</h3><p>Líčení pro focení, brandové kampaně, lookbooky, magazínové editorialy a video obsah. Přizpůsobeno světlu a konceptu každého focení – od čisté beauty práce až po výrazný editoriální styling – s on-set retušemi v průběhu celého produkčního dne.</p></a>
<a href="/kurzy-liceni/"><h3>Osobní kurzy líčení →</h3><p>Individuální (one-on-one) kurzy líčení přizpůsobené vaší úrovni – od klientek, které si chtějí osvojit běžné looky, až po začínající vizážistky budující profesionální dovednosti. Konají se v Praze a pokrývají přípravu pleti, teorii barev, aplikační techniky, výběr nástrojů a doporučení produktů přímo na vaší tváři.</p></a>
</div></div></section>
<section class="sec sec--ox" aria-labelledby="like-h"><div class="wrap ox-split" style="align-items:end">
<div style="display:flex;flex-direction:column;gap:22px"><p class="lbl pink">Líbí se vám?</p><h2 class="big-h" id="like-h">Vytvořme společně váš look</h2><p class="serif ox-note">Napište mi a probereme detaily vaší svatby, akce nebo focení. Do 24 hodin vám pošlu osobní cenovou nabídku a dostupnost termínů.</p>
<p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn--pink" href="{CAL}">Rezervovat termín +</a><a class="btn btn--ghost" href="mailto:{MAIL}">{MAIL}</a></p></div>
<dl class="kv"><div><dt class="lbl">Lokace</dt><dd>Praha, Česká republika</dd></div><div><dt class="lbl">Telefon</dt><dd><a href="tel:{TEL}">{TEL_H}</a></dd></div><div><dt class="lbl">Instagram</dt><dd><a href="{IG}">@nikol__mua</a></dd></div><div><dt class="lbl">Dojezd</dt><dd>ČR i Evropa</dd></div></dl>
</div></section>
'''
    h += footer(LANG, 'Kontaktujte mě', 'Máte dotaz nebo si přejete rezervovat termín?', 'Ráda vám pomohu vytvořit dokonalý look na váš speciální den.')
    write(path, h)


def build():
    home(); wedding(); service(EVENING); service(NUDE); service(COMMERCIAL); courses(); portfolio()
