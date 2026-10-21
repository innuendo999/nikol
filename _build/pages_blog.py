"""Blog: index pages (CZ + EN) and articles based on Nikol's YouTube videos."""
import re
from lib import *
from lib import img as I
import schema as S
from posts import POSTS, ORDER, fmt_date, cards, teaser

L_BLOG = {
    'cs': dict(home=('Domů', '/'), blog='Blog', blog_path='/blog/', read='min čtení', by='Autorka', role='vizážistka, Praha',
               toc='V článku', jump='Přejít na verdikt ↓', watch='Celé video na YouTube · mluvené v ukrajinštině',
               products='Produkty z videa', products_note='Odkazy vedou do obchodů, kde produkty koupíte.'),
    'en': dict(home=('Home', '/en/'), blog='Blog', blog_path='/en/blog/', read='min read', by='By', role='Professional Makeup Artist, Prague',
               toc='In this article', jump='Jump to the verdict ↓', watch='Watch the full video on YouTube · spoken in Ukrainian',
               products='Products in the video', products_note='Links go to shops where you can buy the products.'),
}

# ================================================================= SUMMER
SUMMER_PRODUCTS = [
    ('Chanel Les Beiges Water-Fresh Complexion Touch', 'https://sl1nk.com/p53o9mg'),
    ('Chanel Les Beiges Water-Fresh Tint', 'https://www.chanel.com/cz/make-up/p/158810/les-beiges-water-fresh-tint-vodove-svezi-rozjasnujici-gel-s-mikro-kapickami-pigmentu-nahy-efekt-prirozeny-a-zarivy-zdravy-vzhled/'),
    ('CU Skin Vitamin U CC Cream SPF 40', 'https://ksisters.cz/product/cu-skin-cu-vitamin-u-cc-cream-spf-40?sku=2106115'),
    ('Erborian CC Red Correct', 'https://l1nq.com/s50r6a5'),
    ('Medicube Exosome Cica Toner', 'https://l1nq.com/o8usjgt'),
    ("Paula's Choice 5% Vitamin C Sheer Moisturizer SPF 50", 'https://l1nq.com/vcn1mk7'),
    ('e.l.f. Halo Glow Liquid Filter', 'https://l1nq.com/zmllbes'),
    ('Dior Forever Glow Star Filter', 'https://sl1nk.com/s5hp67w'),
    ('Diorskin Forever', 'https://l1nq.com/tzrlqqi'),
    ('Hourglass Veil Mineral Primer', 'https://sl1nk.com/ot7uh20'),
    ('Charlotte Tilbury Hollywood Flawless Filter 6.5', 'https://l1nq.com/vlc4jux'),
    ('Make Up For Ever HD Skin Face Essentials', 'https://l1nq.com/ptz5am8'),
    ('Estée Lauder Double Wear Sheer', 'https://makeup.cz/product/606546/'),
    ('NYX Professional Makeup Bare With Me Concealer Serum', 'https://l1nq.com/85rx4ot'),
    ('ZOLA Powder Brow Pencil Blond', 'https://sl1nk.com/d45ss9i'),
    ('NYX Professional Makeup The Brow Glue', 'https://l1nq.com/yyl5tao'),
    ('Lancôme Lash Idôle Brown', 'https://sl1nk.com/p7anxue'),
    ('e.l.f. High Definition Powder Sheer', 'https://sl1nk.com/w1prq7k'),
    ('Hourglass Ambient Lighting Palette Volume 3', 'https://www.sephora.cz/p/ambient-lighting-palette-volume-3---paletka-rozjasnovacu-580979.html'),
    ('Lip pencil 01', 'https://l1nq.com/mc0sqp2'),
    ('Chanel Rouge Coco Flash 54', 'https://l1nq.com/vvf60qy'),
    ('unico Lip Gloss With Menthol, Crush', 'https://eva.ua/ua/pr1305491/#/159846'),
    ('Charlotte Tilbury Airbrush Flawless Finish Setting Spray', 'https://l1nq.com/4mgrp7t'),
    ("L'Oréal Paris Infaillible 3-Second Setting Mist", 'https://sl1nk.com/2h1uvqz'),
    ('Caudalie Beauty Elixir', 'https://l1nq.com/mhr8ts1'),
    ('Fenty Beauty You Mist', 'https://l1nq.com/ohxr7ne'),
    ("d'Alba White Truffle First Spray Serum", 'https://sl1nk.com/rjjd9iu'),
    ('Charlotte Tilbury Beauty Light Wand', 'https://l1nq.com/id477qa'),
    ('Givenchy Prisme Libre Prep & Set Glow Mist', 'https://l1nq.com/zu44x5v'),
]
SUMMER_BRANDS = ['Chanel', 'CU Skin', 'Erborian', 'Medicube', "Paula's Choice", 'e.l.f. Cosmetics', 'Dior', 'Hourglass', 'Charlotte Tilbury',
                 'Make Up For Ever', 'Estée Lauder', 'NYX Professional Makeup', 'Zola', 'Lancôme', 'unico', "L'Oréal Paris", 'Caudalie',
                 'Fenty Beauty', "d'Alba", 'Givenchy', 'Sephora']

SUMMER = {}
SUMMER['cs'] = dict(
    toc=[('kratce', 'Postup v kostce'), ('pece', 'Péče a SPF'), ('odstin', 'Odstín pro pihovatou pleť'), ('fluidy', 'Lehké fluidy a CC krémy'),
         ('blur', 'Blur místo lesku'), ('teplo', 'Teplo do pleti'), ('korekce', 'Korekce bez korektoru'), ('oboci', 'Obočí'),
         ('tvare', 'Tváře a rty prsty'), ('oci', 'Řasy'), ('pudr', 'Pudr a rty'), ('spreje', 'Fixační spreje'), ('zaver', 'Rozjasnění a SPF přes den'),
         ('verdikt', 'Verdikt'), ('produkty', 'Produkty z videa'), ('faq', 'Časté dotazy')],
    opener='Make-up bez make-upu je v létě můj nejčastější look. Pleť má vypadat svěže a lehce, v horku nesmí stékat a hlavně ho chci kdykoli smýt, obnovit SPF a během deseti minut udělat znovu. V tomhle tutoriálu ukazuji celý postup krok za krokem a u každého produktu říkám, co si o něm myslím jako vizážistka.',
    summary_h='Postup v kostce',
    steps=['Tonikum a SPF 50 i na krk a dekolt', 'Odstín make-upu podle důlku nad hrudní kostí, ne podle krku', 'Lehký fluid jen tam, kde je potřeba', 'Silikonová báze s blur efektem jen na T-zónu a stíny', 'Krémový bronzer pro teplo', 'Krémová paleta prsty na kruhy a zarudnutí', 'Obočí, řasenka, pudr jen na problémová místa', 'Fixační sprej a kapka rozjasňovače'],
    tested_h='Pro koho a jak jsem to testovala',
    tested='<p>Tenhle postup není pro vás, pokud chcete plné krytí nebo výrazný večerní make-up. Je pro dny u vody, na dovolené nebo ve městě v horku, kdy chcete vypadat odpočatě, ale ne „namalovaně“. Na videu mám lehčí verzi; níže popisuji i kroky, které můžete přidat.</p><p>Mám smíšenou pleť, která je s věkem a v horku mastnější, hlavně když málo piju. K tomu pihy s teplým khaki podtónem, zarudnutí kolem nosu a studený fialový stín pod jedním okem. Podklad jsem měla na sobě několik hodin, než jsem začala natáčet, a pořád vypadal svěže.</p>',
    sections=[
        ('pece', 'Krok 1: péče a SPF', '''<p>Pěnové čisticí přípravky většinou vynechávám, moje pleť je nepotřebuje. Začínám tonikem <b>Medicube Exosome Cica Toner</b>: je řídké, lehké a nezanechává pocit „právě umyté“ pleti. Hodí se i pro mastnou pleť.</p>
<p>Pak přichází <b>Paula's Choice 5% Vitamin C Sheer Moisturizer SPF 50</b>. Je to pro mě tři v jednom: hydratuje, chrání a rozjasňuje, takže v létě vynechávám sérum i krém. Má tekutou, nelepivou texturu, což pomáhá všem, kdo nesnášejí pocit opalovacího krému na obličeji. Nanáším ho i pod oči, na krk a na dekolt.</p>
<aside class="note"><p class="lbl red">Pozor</p><p>Vitamin C může citlivou pleť dráždit. Pokud máte reaktivní pleť, zkuste SPF nejdřív na malé ploše.</p></aside>'''),
        ('odstin', 'Krok 2: odstín make-upu pro pihovatou pleť', '''<p>Pihovatá pleť se studeným, narůžovělým podtónem vypadá ve světlém make-upu snadno šedě. Pleť je potřeba trochu zahřát, ale ne tolik, aby obličej zoranžověl a tělo zůstalo bílé. Mně funguje <b>Chanel Les Beiges v odstínu B30</b>: díky teplému tónu pihy nešednou.</p>
<aside class="note"><p class="lbl red">Tip vizážistky</p><p class="serif fs-20">Odstín nevybírejte podle krku. Ten se často neopálí a bývá světlejší. Porovnávejte s důlkem nad hrudní kostí, mezi krkem a dekoltem.</p></aside>
<p>Lidé s pihami je mívají na zádech, rukou a ramenou, ale na krku málokdy. Proto je krk pro výběr odstínu zavádějící.</p>'''),
        ('fluidy', 'Krok 3: lehké fluidy a CC krémy', '''<p>Porovnávám dva fluidy od Chanel. <b>Les Beiges Water-Fresh Tint</b> pleť jen jemně sjednotí a zarudnutí nepřekryje. Pro mě je skoro zbytečný, dopotřebovávám ho, aby se nezkazil. <b>Les Beiges Water-Fresh Complexion Touch</b> kryje znatelně víc, vydrží dlouho a koupila bych ho znovu, i když je drahý. Sahám po něm ve dny, kdy nemám čas a chci rychle zakrýt červený nos.</p>
<p>Pro mastnou pleť bývá lepší lehčí Tint. Výdrž mají oba podobnou a během dne se mohou trochu setřít, což u make-upu bez make-upu nevadí.</p>
<p>Ukazuji i dva CC krémy. <b>CU Skin Vitamin U CC Cream SPF 40</b> má spíš oranžový tón a sedne mnoha lidem, odstín si ale vyzkoušejte v obchodě. SPF 40 na dovolenou samo nestačí, takže pod něj musíte dát další SPF. <b>Erborian CC Red Correct</b> se hodí spíš na světlou pleť, pleť, která se teprve začíná opalovat, nebo na dny doma.</p>'''),
        ('blur', 'Krok 4: blur místo lesku', '''<p>Moje nová fáze: místo jednoho podkladového produktu vrstvím několik a hlavně používám <b>silikonové báze s blur efektem</b> jen tam, kde lesk nechci. Lesk je krásný na dokonale hladké pleti bez viditelných pórů a stínů. Na mé pleti se začínají objevovat první změny, třeba nová vráska, takže už nelesknu celý obličej.</p>
<p>Nanáším je na T-zónu, kousek na čelo, po stranách nosu a do prohlubní, kde vznikají stíny. Kam přesně, zjistíte jednoduše: natočte obličej ke světlu a podívejte se, kde se odráží.</p>
<ul><li><b>Hourglass Veil Mineral Primer</b> používám hlavně na klientky.</li><li><b>Dior Forever Glow Star Filter</b> a <b>Diorskin Forever</b> jsou o něco lehčí, ale mastnější a na práci se mi hodí méně.</li><li>Pro sebe mám levnější <b>e.l.f. Halo Glow Liquid Filter</b> s lehkým tónem; je mastnější, proto na klientky ne.</li></ul>
<p>Produkt před použitím dobře protřepejte, aby se pigment rozmíchal. Stačí jedna pumpička. Nanáším prstem a na přesná místa štětcem, nezapomínám na uši, vlasovou linii, klíční kosti a dekolt. Cílem není plochý obličej, ale satén: vyvážený lesk a blur.</p>'''),
        ('teplo', 'Krok 5: teplo do pleti', '''<p>Jako krémový bronzer používám mini <b>Charlotte Tilbury Hollywood Flawless Filter v odstínu 6.5</b>. Dlouho vydrží, odráží světlo a pleť vypadá přirozeně. Má ale výrazně oranžový podtón, který nesedne každému. Na pihovatou pleť v létě ho mám ráda.</p>
<p>Tady můžete klidně skončit: přidejte lesk na rty, rozjasňovač a obočí a look je hotový.</p>'''),
        ('korekce', 'Krok 6: korekce bez korektoru', '''<p>Na kruhy pod očima, zarudnutí a jemné stínování používám krémovou paletu <b>Make Up For Ever HD Skin Face Essentials</b>, kterou jsem si dlouho přála a koupila na masterclassu. Má odstíny na kruhy, zarudnutí i bronzování a tvářenky jsou úžasné.</p>
<p>Na svatby a klientky, které potřebují dlouhou výdrž a plné krytí, ale není. Je jemná, méně pigmentovaná a snadno se setře. Na focení ano, na celý den ne. Je to drahý produkt, takže je dobré znát jeho limity.</p>
<p><b>Postup pod očima:</b> druhý nejsvětlejší odstín vtiskněte jedním prstem do místa, kde je kruh nejtmavší, a druhým prstem rozmažte jen okraje. Střed nechte, tam má být nejvíc pigmentu. Pod oči dávám korektor málokdy, kůže se tam při mimice krčí a u make-upu bez make-upu platí: čím méně, tím lépe.</p>
<p>Na zarudnutí stačí prstem poklepat, jemný kontur pod lícní kosti a trochu světla na čelo přidají objem. Místo palety poslouží jakýkoli lehký, nemastný make-up na silikonové bázi; já jsem <b>Estée Lauder Double Wear Sheer</b> dala jen na zarudnutí, ne pod oči. Pro detaily používám sérum korektor <b>NYX Bare With Me</b> v odstínu Vanilla, který jsem testovala ve <a href="/blog/recenze-nyx-cely-oblicej/">velké recenzi NYX</a>. Modřinu pod okem každý den úplně nezakrývám, s plným krytím se necítím tak živě.</p>'''),
        ('oboci', 'Krok 7: obočí', '<p>Mezery doplňuji suchou, pudrovou tužkou <b>ZOLA Powder Brow Pencil v odstínu Blond</b>, která má skvělý pigment, a fixuji gelem <b>NYX The Brow Glue</b>. Víc nedělám.</p>'),
        ('tvare', 'Krok 8: tváře a rty prsty', '''<p>Pro efekt „políbené sluncem“ přidávám jen kapku bronzeru. Tvářenku a bronzer zároveň moc nenosím. Krémový produkt nanáším jedním prstem a čistým prstem roztírám. Na pleti není make-up, takže se všechno krásně prolne. Stejný produkt dávám prsty i na rty.</p>
<p>Když je něco moc výrazné, přejdu to zbytkem korektoru.</p>'''),
        ('oci', 'Krok 9: řasy', '<p>Mám dlouhé, rovné řasy, takže je natáčím. Natočím jedno oko, udělám make-up a pak natočím druhé, protože řasy rychle padají. Používám hnědou řasenku <b>Lancôme Lash Idôle</b>, která se na rozdíl od mnoha jiných nikdy nedrolí. Nanáším ji i na spodní řasy. Některé dny řasy vynechám úplně.</p>'),
        ('pudr', 'Krok 10: pudr jen tam, kde je potřeba, a rty', '''<p>Fixační pudr <b>e.l.f. High Definition Powder</b> v odstínu Sheer je neuvěřitelný a stačí ho opravdu málo. Naberu ho na štětec, skoro všechno oklepu a vtisknu jen tam, kde nechci lesk: pod oči, na bradu, kolem nosu a na čelo. Hlavně ho tisknu na místa s korektorem, aby se nekrčil. Pleť je rozmazaná a zafixovaná, ale nevypadá napudrovaně ani vysušeně. Pokud chcete jemné světlo pudrem, druhá věc z masterclassu je <b>Hourglass Ambient Lighting Palette Volume 3</b>.</p>
<p>Na rty jsem si vzala konturovací tužku v odstínu 01 a navrch rtěnku <b>Chanel Rouge Coco Flash v odstínu 54 Boy</b>, kterou jsem objevila nedávno a zamilovala si ji. Nanáším ji schválně trochu neuspořádaně, aby působila přirozeně. Jako alternativu mám lesk <b>unico Lip Gloss With Menthol</b> v odstínu Crush.</p>'''),
        ('spreje', 'Krok 11: fixační spreje v testu', '''<p>Fixačních sprejů mám víc, tak jsem je porovnala:</p>
<dl class="rows">
<div><dt class="k">Charlotte Tilbury Airbrush Flawless Finish</dt><dd class="v">můj favorit pro sebe i na práci; fixuje a dodá pěkný glow</dd></div>
<div><dt class="k">Fenty Beauty You Mist</dt><dd class="v">krásný lesk a příjemná vůně, ale po bakingu a ve velkém množství se slije</dd></div>
<div><dt class="k">Caudalie Beauty Elixir</dt><dd class="v">nefixuje, hydratuje a voní létem; obsahuje alkohol</dd></div>
<div><dt class="k">d'Alba White Truffle First Spray Serum</dt><dd class="v">není fixační sprej; hydratační sérum ve spreji pro suchou pleť</dd></div>
<div><dt class="k">Mini spreje e.l.f. a Sephora</dt><dd class="v">nefixují vůbec nic</dd></div>
<div><dt class="k">Silné fixační spreje</dt><dd class="v">jako lak na vlasy pro obličej; na lehký make-up zbytečné</dd></div>
</dl>
<p class="mt-16">U Charlotte Tilbury nejdřív jednou stříkněte stranou, aby velké kapky nedopadly na obličej. Caudalie mám od roku 2021, kdy jsem se přestěhovala do Česka, a je to asi moje třetí nebo čtvrtá lahvička. Pokud vám alkohol v kosmetice nedělá dobře, zkontrolujte složení. Ve videu ukazuji i <b>L'Oréal Paris Infaillible 3-Second Setting Mist</b> a <b>Givenchy Prisme Libre Prep &amp; Set Glow Mist</b>.</p>'''),
        ('zaver', 'Krok 12: rozjasnění a SPF přes den', '''<p>Na lícní kosti dávám prstem trochu rozjasňovače <b>Charlotte Tilbury Beauty Light Wand</b> s jemně růžovým tónem. Třpytivé tyčinky na okraje obličeje fungují, ale ne na pleti s texturou, rozšířenými póry nebo jizvami. Přes den nepřeplácávám akcenty; večer, kdy se mění světlo, přidávám víc bronzeru a tvářenky. Jak vypadá výraznější verze, najdete u <a href="/vecerni-liceni/">večerního líčení</a>.</p>
<p><b>SPF přes den:</b> krémové SPF přes make-up nevrstvím, na zaprášenou pleť pod make-upem to podle mě není dobrý nápad. Proto je celá rutina tak lehká: na pláži obličej umyju, obnovím SPF a za pár minut ji udělám znovu.</p>'''),
    ],
    verdict_h='Verdikt: co se vyplatí',
    verdict=[('Vyplatí se', 'vtag v-yes', ['Charlotte Tilbury Airbrush Flawless Finish', 'Lancôme Lash Idôle, hnědá', 'NYX Bare With Me', 'e.l.f. High Definition Powder', 'Chanel Rouge Coco Flash 54', 'Chanel Water-Fresh Complexion Touch', 'Caudalie Beauty Elixir (hydratace)']),
             ('Záleží na pleti', 'vtag v-dep', ['Hollywood Flawless Filter (oranžový tón)', 'Make Up For Ever HD Skin Face Essentials (nízká výdrž)', 'Fenty Beauty You Mist (v malém množství)', "Paula's Choice SPF 50 s vitaminem C (citlivá pleť)"]),
             ('Spíš ne', 'vtag v-sw', ['Chanel Water-Fresh Tint (na moji pleť)', 'Mini spreje e.l.f. a Sephora', 'Silné fixační spreje na lehký make-up'])],
    verdict_foot='',
    lessons_h='Tři věci, které si z toho vzít',
    lessons=[('Odstín vybírejte podle hrudníku, ne podle krku.', 'U pihovaté pleti rozhoduje teplý tón. Šedý obličej prozradí špatný odstín víc než jakékoli krytí.'),
             ('Blur jen tam, kde je potřeba.', 'Zbytek pleti nechte přirozeně saténový. Dokonale matný obličej v létě nevypadá svěže.'),
             ('Méně korektoru pod očima.', 'Pigment vtiskněte do nejtmavšího místa a rozmažte jen okraje. Make-up se pak nekrčí.')],
    learn_h='Chcete se to naučit?',
    cta_note='Tenhle postup procházíme na <a href="/kurzy-liceni/">individuálním kurzu líčení</a>: s vašimi produkty a s ohledem na typ vaší pleti.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Nechte se nalíčit na focení nebo událost',
    cta_text='Přirozený look, který vydrží focení i celý den, dělám i pro klientky: na zásnubní focení, portréty nebo civilní obřad.',
    cta_links=[('Nude líčení', '/nude-liceni/'), ('Svatební líčení', '/svatebni-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Co je make-up bez make-upu?', 'Lehký look, který sjednotí pleť, opraví jen to, co je vidět, a zvýrazní vaše rysy tak, aby make-up nebyl poznat. Místo plného krytí se pracuje s lehkými fluidy, krémovými produkty a pudrem jen na vybraná místa.'),
         ('Jak vybrat odstín make-upu, když mám pihy?', 'Porovnávejte s důlkem nad hrudní kostí, ne s krkem, který bývá světlejší. Pihovatá pleť se studeným podtónem potřebuje trochu teplejší odstín, jinak vypadá šedě, ale ne tak teplý, aby obličej zoranžověl.'),
         ('Jak v létě omezit lesk, aby pleť nevypadala plochá?', 'Silikonovou bázi s blur efektem dejte jen na T-zónu, kolem nosu a do prohlubní, kde vznikají stíny. Pudr vtiskněte jen na stejná místa. Zbytek pleti nechte saténový.'),
         ('Jaký fixační sprej je nejlepší na léto?', 'Na fixaci se mi nejvíc osvědčil Charlotte Tilbury Airbrush Flawless Finish, na hydrataci Caudalie Beauty Elixir. Mini spreje e.l.f. a Sephora podle mého testu nefixují.'),
         ('Můžu přes make-up během dne obnovit SPF?', 'Krémové SPF přes make-up nevrstvím, na zaprášenou pleť to podle mě není dobrý nápad. Tahle rutina je proto tak lehká, aby se dala smýt, obnovit SPF a za pár minut udělat znovu.'),
         ('Můžu se tenhle look naučit?', 'Ano. Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> v Praze ho projdeme krok za krokem na vaší pleti a s vašimi produkty. Pokud chcete look na focení nebo obřad, podívejte se na <a href="/nude-liceni/">nude líčení</a>.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

SUMMER['en'] = dict(
    toc=[('summary', 'The routine in short'), ('skin', 'Skin prep and SPF'), ('shade', 'Shades for freckled skin'), ('fluids', 'Light fluids and CC creams'),
         ('blur', 'Blur instead of shine'), ('warmth', 'Warmth'), ('correct', 'Correcting without concealer'), ('brows', 'Brows'),
         ('cheeks', 'Cheeks and lips with fingers'), ('lashes', 'Lashes'), ('powder', 'Powder and lips'), ('sprays', 'Setting sprays'), ('finish', 'Glow and SPF during the day'),
         ('verdict', 'The verdict'), ('products', 'Products in the video'), ('faq', 'FAQ')],
    opener='No-makeup makeup is my most worn look every summer. Skin should look fresh and light, it must survive the heat, and above all I want to be able to wash it off, reapply SPF and redo it in ten minutes. In this tutorial I go through the whole routine step by step and tell you what I honestly think of every product as a makeup artist.',
    summary_h='The routine in short',
    steps=['Toner and SPF 50, including neck and décolleté', 'Match foundation to the hollow above your breastbone, not your neck', 'A light fluid only where you need it', 'A blurring silicone primer only on the T-zone and shadows', 'A cream bronzer for warmth', 'A cream palette with fingers for circles and redness', 'Brows, mascara, powder only where it shines', 'Setting spray and a touch of highlighter'],
    tested_h='Who it is for and how I tested it',
    tested="<p>This routine isn't for you if you want full coverage or a statement evening look. It's for beach days, holidays and hot city days when you want to look rested, not \"done\". In the video I wear a lighter version; below I also describe the steps you can add.</p><p>My skin is combination and has become oilier with age and heat, especially when I don't drink enough water. I have freckles with a warm khaki undertone, redness around the nose and a cool purple shadow under one eye. I had been wearing the base for a few hours before filming and it still looked fresh.</p>",
    sections=[
        ('skin', 'Step 1: skin prep and SPF', '''<p>I usually skip foaming cleansers; my skin doesn't need them. I start with the <b>Medicube Exosome Cica Toner</b>: thin, light and without that "just washed" tight feeling. It suits oily skin too.</p>
<p>Next comes <b>Paula's Choice 5% Vitamin C Sheer Moisturizer SPF 50</b>. For me it's three in one: it hydrates, protects and brightens, so in summer I skip serum and moisturiser. The texture is liquid and not sticky, which helps anyone who hates the feel of sunscreen on the face. I apply it under the eyes, on the neck and on the décolleté too.</p>
<aside class="note"><p class="lbl red">Note</p><p>Vitamin C can irritate sensitive skin. If your skin is reactive, patch-test the SPF first.</p></aside>'''),
        ('shade', 'Step 2: foundation shades for freckled skin', '''<p>Freckled skin with a cool, pinkish undertone easily looks grey in a light foundation. You need to warm the complexion up, but not so much that the face turns orange while the body stays white. What works for me is <b>Chanel Les Beiges in B30</b>: the warm tone keeps freckles from going grey.</p>
<aside class="note"><p class="lbl red">Pro tip</p><p class="serif fs-20">Don't match your foundation to your neck. It often doesn't tan and is usually lighter. Match it to the hollow above your breastbone, between the neck and the chest.</p></aside>
<p>People with freckles tend to have them on the back, arms and shoulders, but rarely on the neck. That's why the neck is misleading when you choose a shade.</p>'''),
        ('fluids', 'Step 3: light fluids and CC creams', '''<p>I compare two Chanel fluids. <b>Les Beiges Water-Fresh Tint</b> only slightly evens out the skin and doesn't cover redness. For me it's almost pointless; I'm only using it up so it doesn't expire. <b>Les Beiges Water-Fresh Complexion Touch</b> covers noticeably more, lasts well and I would buy it again even though it's expensive. I reach for it on days when I have no time and want to cover my red nose quickly.</p>
<p>The lighter Tint is usually better for oily skin. Both last about the same and can wear off a little during the day, which doesn't matter for a no-makeup look.</p>
<p>I also show two CC creams. <b>CU Skin Vitamin U CC Cream SPF 40</b> leans orange and suits a lot of people, but test the shade in store. SPF 40 alone isn't enough for a holiday, so you need extra SPF underneath. <b>Erborian CC Red Correct</b> works better for fair skin, skin that is only starting to tan, or days at home.</p>'''),
        ('blur', 'Step 4: blur instead of shine', '''<p>My new phase: instead of one base product I layer several, and above all I use <b>blurring silicone primers</b> only where I don't want shine. Glow looks beautiful on perfectly smooth skin without visible pores or shadows. My skin is starting to show the first changes, like a new crease, so I no longer make the whole face glow.</p>
<p>I apply them to the T-zone, a little on the forehead, along the sides of the nose and into the hollows where shadows form. To find the right spots, turn your face towards the light and look at where it reflects.</p>
<ul><li><b>Hourglass Veil Mineral Primer</b> is the one I use mostly on clients.</li><li><b>Dior Forever Glow Star Filter</b> and <b>Diorskin Forever</b> are a little lighter but oilier, and work less well for me professionally.</li><li>For myself I use the cheaper tinted <b>e.l.f. Halo Glow Liquid Filter</b>; it's greasier, so not for clients.</li></ul>
<p>Shake the product well so the pigment mixes. One pump is enough. I apply it with a finger and use a brush for precise areas, and I don't forget the ears, hairline, collarbones and chest. The goal isn't a flat face but a satin finish: a balance of glow and blur.</p>'''),
        ('warmth', 'Step 5: warmth', '''<p>As a cream bronzer I use a mini <b>Charlotte Tilbury Hollywood Flawless Filter in shade 6.5</b>. It lasts, reflects light and looks natural on the skin. It does have a distinctly orange undertone that won't suit everyone. On freckled skin in summer, I love it.</p>
<p>You can stop here: add lip gloss, highlighter and brows, and the look is done.</p>'''),
        ('correct', 'Step 6: correcting without concealer', '''<p>For under-eye circles, redness and soft shading I use the <b>Make Up For Ever HD Skin Face Essentials</b> cream palette, which I'd wanted for a long time and finally bought at a masterclass. It has shades for circles, redness and bronzing, and the blushes are amazing.</p>
<p>It isn't for weddings or clients who need long wear and full coverage, though. It's delicate, less pigmented and wears off easily. Great for photo shoots, not for a full day. It's an expensive product, so it's worth knowing its limits.</p>
<p><b>Under-eye technique:</b> press the second-lightest shade with one finger into the darkest part of the circle, and blend only the edges with another finger. Leave the centre alone; that's where you want the most pigment. I rarely put concealer under my eyes because the skin creases with expression, and for no-makeup makeup less is more.</p>
<p>Tap the redness with a finger, add a soft contour under the cheekbones and a little light on the forehead for dimension. Any light, non-greasy silicone-based foundation can replace the palette; I used <b>Estée Lauder Double Wear Sheer</b> only on redness, not under the eyes. For details I use the <b>NYX Bare With Me</b> serum concealer in Vanilla, which I tested in my <a href="/en/blog/full-face-of-nyx-review/">full NYX review</a>. I don't fully cover the bruise under my eye every day; with full coverage I don't feel as lively.</p>'''),
        ('brows', 'Step 7: brows', '<p>I fill the gaps with the dry, powdery <b>ZOLA Powder Brow Pencil in Blond</b>, which has great pigment, and set them with <b>NYX The Brow Glue</b>. That\'s all.</p>'),
        ('cheeks', 'Step 8: cheeks and lips with fingers', '''<p>For a sun-kissed effect I add just a touch of bronzer; I rarely wear blush and bronzer together. I apply the cream with one finger and blend with a clean one. There's no foundation on the skin, so everything melts in easily. I put the same product on my lips with my fingers.</p>
<p>If something looks too strong, I go over it with what's left of the concealer.</p>'''),
        ('lashes', 'Step 9: lashes', '<p>My lashes are long and straight, so I curl them. I curl one eye, do my makeup, then curl the other, because the curl drops quickly. I use <b>Lancôme Lash Idôle</b> in brown, which unlike many mascaras never flakes. I apply it to the lower lashes too. Some days I skip lashes altogether.</p>'),
        ('powder', 'Step 10: powder only where you need it, and lips', '''<p>The <b>e.l.f. High Definition Powder</b> in Sheer is incredible and you need very little. I pick it up with a brush, tap almost all of it off and press it only where I don't want shine: under the eyes, on the chin, around the nose and on the forehead. Above all I press it over concealer so it doesn't crease. The skin looks blurred and set, but not powdery or dry. If you want a soft powder glow, the second thing I bought at the masterclass is the <b>Hourglass Ambient Lighting Palette Volume 3</b>.</p>
<p>On the lips I used lip pencil 01 and on top <b>Chanel Rouge Coco Flash in 54 Boy</b>, which I discovered recently and fell in love with. I apply it slightly messy on purpose so it looks natural. As an alternative I like the <b>unico Lip Gloss With Menthol</b> in Crush.</p>'''),
        ('sprays', 'Step 11: setting sprays, tested', '''<p>I own several setting sprays, so I compared them:</p>
<dl class="rows">
<div><dt class="k">Charlotte Tilbury Airbrush Flawless Finish</dt><dd class="v">my favourite for myself and for work; sets and adds a nice glow</dd></div>
<div><dt class="k">Fenty Beauty You Mist</dt><dd class="v">lovely glow and scent, but cakes if you drench it over baked powder</dd></div>
<div><dt class="k">Caudalie Beauty Elixir</dt><dd class="v">doesn't set; hydrates and smells like summer; contains alcohol</dd></div>
<div><dt class="k">d'Alba White Truffle First Spray Serum</dt><dd class="v">not a setting spray; a hydrating spray serum for dry skin</dd></div>
<div><dt class="k">e.l.f. and Sephora minis</dt><dd class="v">don't set anything at all</dd></div>
<div><dt class="k">Heavy-duty setting sprays</dt><dd class="v">hairspray for the face; pointless for light makeup</dd></div>
</dl>
<p class="mt-16">With Charlotte Tilbury, spray once to the side first so the big droplets don't land on your face. I've used Caudalie since 2021, when I moved to the Czech Republic; this is probably my third or fourth bottle. If alcohol in skincare doesn't agree with you, check the ingredients. In the video I also show <b>L'Oréal Paris Infaillible 3-Second Setting Mist</b> and <b>Givenchy Prisme Libre Prep &amp; Set Glow Mist</b>.</p>'''),
        ('finish', 'Step 12: glow and SPF during the day', '''<p>I tap a little <b>Charlotte Tilbury Beauty Light Wand</b> with a soft rosy tone onto my cheekbones with a finger. Shimmer sticks on the outer face work, but not on skin with texture, enlarged pores or scarring. During the day I don't overdo accents; in the evening, when the light changes, I add more bronzer and blush. You can see the bolder version on my <a href="/en/evening-makeup/">evening makeup</a> page.</p>
<p><b>SPF during the day:</b> I don't layer cream SPF over makeup; on dusty skin under makeup I don't think it's a good idea. That's exactly why the routine is so light: at the beach I wash my face, reapply SPF and redo it in a few minutes.</p>'''),
    ],
    verdict_h='The verdict: what is worth buying',
    verdict=[('Worth buying', 'vtag v-yes', ['Charlotte Tilbury Airbrush Flawless Finish', 'Lancôme Lash Idôle, brown', 'NYX Bare With Me', 'e.l.f. High Definition Powder', 'Chanel Rouge Coco Flash 54', 'Chanel Water-Fresh Complexion Touch', 'Caudalie Beauty Elixir (hydration)']),
             ('Depends on your skin', 'vtag v-dep', ['Hollywood Flawless Filter (orange undertone)', 'Make Up For Ever HD Skin Face Essentials (short wear)', 'Fenty Beauty You Mist (use lightly)', "Paula's Choice SPF 50 with vitamin C (sensitive skin)"]),
             ('Skip', 'vtag v-sw', ['Chanel Water-Fresh Tint (on my skin)', 'e.l.f. and Sephora mini sprays', 'Heavy-duty sprays on light makeup'])],
    verdict_foot='',
    lessons_h='Three things to take away',
    lessons=[('Match your chest, not your neck.', 'On freckled skin the warm undertone matters most. A grey face gives away the wrong shade more than any coverage does.'),
             ('Blur only where you need it.', 'Leave the rest of the skin naturally satin. A fully matte face never looks fresh in summer.'),
             ('Less concealer under the eyes.', 'Press pigment into the darkest spot and blend only the edges. That way the makeup doesn\'t crease.')],
    learn_h='Want to learn this properly?',
    cta_note='We work through this routine in my <a href="/en/courses/">one-on-one makeup courses</a>: with your own products and your skin type in mind.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Get the look for a shoot or an event',
    cta_text='I create natural looks that last through a shoot or a whole day for clients too: engagement shoots, portraits or a civil ceremony.',
    cta_links=[('Nude makeup', '/en/nude-makeup/'), ('Wedding makeup', '/en/wedding/')],
    faq_h='Frequently asked questions',
    faq=[('What is no-makeup makeup?', 'A light look that evens out the skin, corrects only what shows and enhances your features so the makeup isn\'t noticeable. Instead of full coverage it relies on light fluids, cream products and powder only in selected areas.'),
         ('How do I choose a foundation shade if I have freckles?', 'Match it to the hollow above your breastbone, not to your neck, which is usually lighter. Freckled skin with a cool undertone needs a slightly warmer shade, otherwise it looks grey, but not so warm that the face turns orange.'),
         ('How do I control shine in summer without looking flat?', 'Put a blurring silicone primer only on the T-zone, around the nose and in the hollows where shadows form, and press powder into the same areas. Leave the rest of the skin satin.'),
         ('Which setting spray is best for summer?', 'For setting, Charlotte Tilbury Airbrush Flawless Finish worked best for me; for hydration, Caudalie Beauty Elixir. In my test the e.l.f. and Sephora mini sprays didn\'t set at all.'),
         ('Can I reapply SPF over makeup during the day?', 'I don\'t layer cream SPF over makeup; on dusty skin I don\'t think it\'s a good idea. That\'s why this routine is so light: you can wash it off, reapply SPF and redo it in a few minutes.'),
         ('Can I learn this look?', 'Yes. In a <a href="/en/courses/">one-on-one makeup course</a> in Prague we go through it step by step on your skin and with your products. If you want the look for a shoot or ceremony, see <a href="/en/nude-makeup/">nude makeup</a>.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

# ================================================================= NYX
NYX_BRANDS = ['NYX Professional Makeup']
NYX = {}
NYX['en'] = dict(
    toc=[('verdict', 'The verdict at a glance'), ('primer', 'Skin prep'), ('concealer', 'Complexion'), ('brows', 'Brows'), ('bronzer', 'Warmth'),
         ('powder', 'Setting the base'), ('eyes', 'Eyes'), ('lips', 'Lips'), ('spray', 'The finish'), ('wear', 'A full day of wear'),
         ('worth', 'Is it worth it?'), ('lessons', 'Three lessons'), ('faq', 'FAQ')],
    opener='NYX has always sat in an interesting spot for me. It is no longer truly cheap, yet it never pretends to be luxury either, and that quiet confidence is exactly why it holds one of the most stable reputations in the drugstore world. So I put it to the test the only way that really counts: a full face, start to finish, using nothing but NYX.',
    pre='''<p>Bestsellers, a few brand-new launches I had been dying to try, and most importantly an honest wear test at the end of the day. Below is everything that earned its place in my kit, and everything I would happily leave on the shelf.</p>
<aside class="note"><p class="lbl red">How I tested it</p><p>I applied a complete look on camera, from skin prep through to setting spray, then wore it through a full working day and checked it again that night, and once more the next day. For reference, my skin is normal-to-combination.</p></aside>''',
    verdict_h='The verdict at a glance',
    verdict=[('Worth buying', 'vtag v-yes', ['The cult bronzer', 'Pressed powder', 'Brow glue', 'Mascara', 'Concealer (spot coverage)', 'Long-wear eyeliner*']),
             ('Depends on your skin', 'vtag v-dep', ['Plumping primer', 'Setting spray']),
             ('Swatch first', 'vtag v-sw', ['Matte eyeshadow palette', 'Warm lip liner'])],
    verdict_foot='*Brilliant longevity, but unforgiving: best for confident hands.',
    sections=[
        ('primer', 'Skin prep: the plumping primer', '''<p class="vtag v-dep">Depends on skin type</p>
<p>This is the brand's hero of the moment: a light gel-emulsion that promises to be serum and primer in one, with a pleasant, neutral scent. On me it turned tacky very quickly and the tight feeling only built through the day. That stickiness can actually help foundation grip, so I would happily recommend it for combination or oily skin. On dry or flaky skin it will not smooth those dry patches, and the pulled feeling is not for everyone. Not quite the universal hero the label suggests.</p>'''),
        ('concealer', 'Complexion: the serum concealer', '''<p class="vtag v-yes">Worth it for targeted coverage</p>
<p>Surprisingly dense and full-coverage for something sold as a "serum" concealer. It stays put, does not slide, and the slim tube means you will actually use every last drop. It leans slightly drying, and my shade ran a touch warmer than a true cool vanilla, so check your undertone. For targeted coverage it is excellent; over the whole face the usage adds up fast. I still use it in my <a href="/en/blog/summer-no-makeup-makeup/">summer no-makeup routine</a>.</p>
<aside class="note"><p class="lbl red">Pro move</p><p class="serif fs-20">Mix a little into your serum or moisturiser to turn it into a sheer tint.</p></aside>'''),
        ('brows', 'Brows: pencils, micro-liners and the brow glue', '''<p class="vtag v-yes">Worth it: find your shade</p>
<p>The pencils are genuinely good: consistent, easy to work with and very wearable. One thing to watch: a couple of the taupe-leaning shades can oxidise slightly green on me over time, so I have switched to the cooler blond shade, which also draws beautifully over the brow glue. The glue itself gives serious, laminated hold, perfect if you love that brushed-up, locked-in look. I prefer a softer, more natural shape these days, so I used it with a lighter hand. Tip: set your brows <strong>before</strong> foundation for the cleanest finish.</p>'''),
        ('bronzer', 'Warmth: the cult bronzer (and a word on blush)', '''<p class="vtag v-yes">Worth it</p>
<p>A deserved classic. Only the warm shade was in stock, so my face ran a little golden, but the formula is the real story. It smells like a chocolate-vanilla dessert, it is not baked, and yet it still does not go patchy, which is rare at this price. Around 10–15 €, easy top marks. I pressed it into place rather than buffing, because the skin underneath was a touch tacky.</p>
<aside class="note"><p class="lbl red">A pro note on hygiene</p><p>For blush I reached for a powder I have owned since long before I became a makeup artist, and that is something to flag, not to copy. Powders carry a period-after-opening for a reason. My honest advice as a professional is to respect those dates and replace anything well past them.</p></aside>'''),
        ('powder', 'Setting the base: the pressed powder', '''<p class="vtag v-yes">Worth it</p>
<p>It lives up to the hype. It sets the base and controls shine without clinging to dry patches or exaggerating texture, the exact failure point of so many heavier budget powders. One of my favourite finds of the whole haul.</p>'''),
        ('eyes', 'Eyes: palette, liner and mascara', '''<h3>The matte eyeshadow palette</h3><p class="vtag v-sw">Swatch first</p>
<p>A very on-trend warm-neutral palette with a few cooler, pinky tones. The shades are pretty, but pigmentation sits on the softer side, especially layered over powder, which sheered them further. The look still came together nicely; next time I would skip powdering the lid first.</p>
<h3>The eyeliner</h3><p class="vtag v-yes">Worth it for steady hands</p>
<p>Honestly, a wow. It is intensely long-wearing and does not budge or transfer once it sets, which is also the catch: there is almost no room for error, so it is not the most forgiving choice for beginners. I built a soft winged shape and loved how crisp it stayed all day.</p>
<h3>The mascara</h3><p class="vtag v-yes">Worth it</p>
<p>Fresh from the tube it applied cleanly with a classic brush, adding volume rather than just length, which is my preference. Pending a proper flake test over a few wears, this is one I would repurchase.</p>'''),
        ('lips', 'Lips: liner and matte balm', '''<p class="vtag v-mix">Mixed</p>
<p>The lip liner is a long-standing favourite, though a reformulation made it noticeably warmer. It reads quite orange-warm on me now, so it suited today's warm look but will not be everyone's everyday shade. The matte "whip" balm gives a soft tint with a comfortable, slightly slippery feel and a lovely sweet scent; I also dabbed it on the cheeks as a quick cream blush to tie the whole look together.</p>'''),
        ('spray', 'The finish: setting spray', '''<p class="vtag v-dep">Depends on skin type</p>
<p>Last year's much-hyped spray (mine had settled, so it is clearly powder-infused: shake well). The applicator is punchy and it genuinely locks everything down. For a true matte finish it is great; on drier skin, combined with the primer, it was simply too much fixation for me.</p>'''),
        ('wear', 'The part that actually matters: a full day of wear', '''<p>Swatches and first impressions are easy. What separates a good product from a great one is how it looks after hours of real life, so here is the honest timeline.</p>
<dl class="timeline">
<div><dt>After 3–4 hours</dt><dd>The skin had picked up a natural sheen but still looked alive, nothing had creased under the eyes, and the brows held their shape.</dd></div>
<div><dt>End of the day</dt><dd>The complexion was shiny (which I do not mind), under-eyes stayed clean, the lip tint held on beautifully and the brows had softened only minimally. The honest downside: my skin felt tight all day, which I put down to the primer and setting spray together being too much fixation for my normal-combination skin.</dd></div>
<div><dt>Day two</dt><dd>I re-tested just the concealer and powder over my usual skin prep and foundation. They barely moved after five hours. That told me the concealer and powder are genuinely excellent; the tight, dry feeling was the primer, not the base.</dd></div>
</dl>'''),
        ('worth', 'So, is a full face of NYX worth it?', '''<p>NYX is exactly what its reputation suggests: a confident, dependable brand that has quietly graduated from pure drugstore into the lower mid-range. The pieces I would happily keep in a working kit: the bronzer, the pressed powder, the brow glue, the mascara, the long-wear liner (for confident hands) and the concealer for targeted coverage. The plumping primer and setting spray depend on skin type: wonderful for combination and oily skin, a lot for dry skin. The matte palette is pretty but worth swatching for pigment first. Match the right pieces to your skin, and NYX absolutely earns its place.</p>'''),
    ],
    lessons_h='Three things this look can teach you about your own makeup',
    lessons=[('A product is only as good as its fit for your skin.', 'My primer struggle was not a "bad product"; it was the wrong product for my skin that day. Learning to read your own skin is half of great makeup.'),
             ('Placement beats pigment.', 'Whether you powder before shadow, press or buff your bronzer, or sheer out a dense concealer, technique decides the result far more than price does.'),
             ('Build for the day you will actually have.', 'For <a href="/en/evening-makeup/">events</a> and <a href="/en/wedding/">weddings</a> I lean on the long-wear pieces: powder, a locking liner, brow gel, and adjust fixation to the skin in front of me.')],
    learn_h='Want to learn this properly?',
    cta_note='These are exactly the skills we work through, one-on-one, in my <a href="/en/courses/">personalised makeup courses</a>: using your own face, your own skin type and products that genuinely suit you.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title="Let's create your look",
    cta_text='Whether you want flawless, long-lasting makeup for your wedding or a special event, or you would like to learn these techniques yourself, I would love to help.',
    cta_links=[('Wedding makeup', '/en/wedding/'), ('Evening makeup', '/en/evening-makeup/')],
    faq_h='Frequently asked questions',
    faq=[('Do professional makeup artists really use drugstore brands like NYX?', 'Absolutely. A working kit is a mix of price points; what matters is how a product performs, not its label. Several NYX products, including the bronzer, powder, mascara and long-wear liner, hold their own next to far pricier options.'),
         ('What were the best NYX products in this test?', 'The cult bronzer, the pressed powder, the brow glue, the mascara, the long-wear eyeliner, and the concealer for targeted spot coverage.'),
         ('Is NYX makeup good enough for a wedding or a long event?', 'The long-wear pieces (powder, setting spray, locking liner and brow glue) can last impressively well. For your wedding day I would still recommend a professional application and a trial first. You can see what that involves on my <a href="/en/wedding/">wedding makeup</a> page.'),
         ('Which NYX products should I be careful with?', 'The plumping primer can feel tight on dry or flaky skin, and the matte eyeshadows are lovely but lower in pigment: swatch them in store first.'),
         ('Can I learn to create a full-face look like this myself?', 'Yes. That is exactly what my <a href="/en/courses/">one-on-one makeup courses</a> are for, tailored to your skin type and goals, from everyday looks to professional techniques.'),
         ('Where are you based?', 'I am an English-speaking makeup artist based in Prague, and I travel across the Czech Republic and Europe for weddings, shoots and events. <a href="#contact">Get in touch here.</a>')],
    bio='Bridal, evening and editorial makeup artist based in Prague, offering personalised services and one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

NYX['cs'] = dict(
    toc=[('verdikt', 'Verdikt v kostce'), ('baze', 'Příprava pleti'), ('korektor', 'Pleť'), ('oboci', 'Obočí'), ('bronzer', 'Teplo'),
         ('pudr', 'Fixace podkladu'), ('oci', 'Oči'), ('rty', 'Rty'), ('sprej', 'Fixační sprej'), ('vydrz', 'Celý den v make-upu'),
         ('vyplati', 'Vyplatí se?'), ('lekce', 'Tři ponaučení'), ('faq', 'Časté dotazy')],
    opener='NYX pro mě vždycky stál na zajímavém místě. Už není úplně levný, ale nikdy si nehraje na luxus, a právě díky tomu má jednu z nejstabilnějších pověstí mezi drogerkovými značkami. Tak jsem ho otestovala jediným způsobem, který má smysl: celý obličej od začátku do konce, jen produkty NYX.',
    pre='''<p>Bestsellery, pár novinek, které jsem chtěla vyzkoušet, a hlavně poctivý test výdrže na konci dne. Níže najdete všechno, co si zasloužilo místo v mém kufru, i to, co bych klidně nechala v regálu.</p>
<aside class="note"><p class="lbl red">Jak jsem testovala</p><p>Celý look jsem nanesla před kamerou, od přípravy pleti po fixační sprej, pak jsem v něm byla celý pracovní den, večer jsem ho zkontrolovala znovu a ještě jednou další den. Pro představu: mám normální až smíšenou pleť.</p></aside>''',
    verdict_h='Verdikt v kostce',
    verdict=[('Vyplatí se', 'vtag v-yes', ['Kultovní bronzer', 'Kompaktní pudr', 'Gel na obočí The Brow Glue', 'Řasenka', 'Korektor (na lokální krytí)', 'Dlouhotrvající linky*']),
             ('Záleží na pleti', 'vtag v-dep', ['Vyplňující báze', 'Fixační sprej']),
             ('Nejdřív vyzkoušet', 'vtag v-sw', ['Paleta matných stínů', 'Teplá konturovací tužka na rty'])],
    verdict_foot='*Skvělá výdrž, ale neodpouští chyby: spíš pro jistou ruku.',
    sections=[
        ('baze', 'Příprava pleti: vyplňující báze', '''<p class="vtag v-dep">Záleží na typu pleti</p>
<p>Současný hit značky: lehká gelová emulze, která slibuje sérum a bázi v jednom, s příjemnou neutrální vůní. Na mně se velmi rychle stala lepivou a pocit napětí během dne jen sílil. Lepivost může make-upu pomoct lépe přilnout, takže na smíšenou nebo mastnou pleť ji klidně doporučím. Na suché nebo olupující se pleti suchá místa nevyhladí a pocit stažení nebude vyhovovat každému. Univerzální hit, jak slibuje obal, to úplně není.</p>'''),
        ('korektor', 'Pleť: sérum korektor', '''<p class="vtag v-yes">Vyplatí se na lokální krytí</p>
<p>Na korektor, který se prodává jako „sérum“, je překvapivě hustý a dobře kryje. Drží na místě, neklouže a díky tenké tubě opravdu spotřebujete každou kapku. Trochu vysušuje a můj odstín byl o kousek teplejší než skutečně studená vanilka, takže si zkontrolujte podtón. Na lokální krytí je výborný, na celém obličeji se spotřeba rychle sčítá. Používám ho i v <a href="/blog/letni-make-up-bez-make-upu/">letní rutině make-upu bez make-upu</a>.</p>
<aside class="note"><p class="lbl red">Tip vizážistky</p><p class="serif fs-20">Smíchejte trochu se sérem nebo krémem a máte lehký tónovací krém.</p></aside>'''),
        ('oboci', 'Obočí: tužky, mikro-linery a gel', '''<p class="vtag v-yes">Vyplatí se: najděte svůj odstín</p>
<p>Tužky jsou opravdu dobré: stálé, snadno se s nimi pracuje a dobře se nosí. Jedna věc: pár odstínů do taupe na mně časem lehce oxiduje do zelena, proto jsem přešla na chladnější blond odstín, který krásně kreslí i přes gel. Samotný gel The Brow Glue drží jako laminace, ideální, pokud máte rádi vyčesané, zafixované obočí. Já dnes dávám přednost jemnějšímu, přirozenějšímu tvaru, takže jsem ho použila s lehčí rukou. Tip: obočí zafixujte <strong>před</strong> make-upem, výsledek bude nejčistší.</p>'''),
        ('bronzer', 'Teplo: kultovní bronzer (a pár slov o tvářence)', '''<p class="vtag v-yes">Vyplatí se</p>
<p>Zasloužená klasika. Skladem byl jen teplý odstín, takže obličej vyšel trochu do zlata, ale hlavní je receptura. Voní jako čokoládovo-vanilkový dezert, není zapečený, a přesto se nedělá do skvrn, což je v téhle cenové hladině vzácné. Kolem 10–15 €, jasná jednička. Bronzer jsem do pleti spíš vtiskla, než roztírala, protože pleť pod ním byla trochu lepivá.</p>
<aside class="note"><p class="lbl red">Poznámka k hygieně</p><p>Na tvářenku jsem sáhla po pudru, který mám ještě z doby, než jsem se stala vizážistkou. To je věc k upozornění, ne k napodobení. Pudry mají dobu použitelnosti po otevření z dobrého důvodu. Jako profesionálka radím tato data dodržovat a staré produkty vyměnit.</p></aside>'''),
        ('pudr', 'Fixace podkladu: kompaktní pudr', '''<p class="vtag v-yes">Vyplatí se</p>
<p>Splňuje očekávání. Zafixuje podklad a zkrotí lesk, aniž by se chytal suchých míst nebo zvýrazňoval texturu, což je přesně slabina mnoha těžších levných pudrů. Jeden z mých nejoblíbenějších objevů celého testu.</p>'''),
        ('oci', 'Oči: paleta, linky a řasenka', '''<h3>Paleta matných stínů</h3><p class="vtag v-sw">Nejdřív vyzkoušet</p>
<p>Velmi aktuální teple neutrální paleta s několika chladnějšími, narůžovělými tóny. Odstíny jsou hezké, ale pigmentace je spíš jemná, hlavně přes pudr, který je ještě zeslabil. Look se i tak hezky poskládal; příště bych víčko předem nepudrovala.</p>
<h3>Oční linky</h3><p class="vtag v-yes">Vyplatí se pro jistou ruku</p>
<p>Upřímně: wow. Drží extrémně dlouho a po zaschnutí se nehne ani neotiskne, což je zároveň háček: na chybu není skoro žádný prostor, takže pro začátečnice to není nejshovívavější volba. Udělala jsem jemnou kočičí linku a celý den zůstala ostrá.</p>
<h3>Řasenka</h3><p class="vtag v-yes">Vyplatí se</p>
<p>Čerstvě otevřená se nanášela čistě klasickým kartáčkem a dodala spíš objem než jen délku, což mám ráda. Uvidíme po pár nošeních, jestli se nedrolí, ale tuhle bych si koupila znovu.</p>'''),
        ('rty', 'Rty: tužka a matný balzám', '''<p class="vtag v-mix">Smíšené</p>
<p>Konturovací tužka je dlouholetá oblíbenkyně, ale po změně receptury je znatelně teplejší. Na mně teď působí dost oranžově, takže k dnešnímu teplému looku se hodila, ale každodenní odstín pro každou to nebude. Matný „whip“ balzám dává jemný odstín, příjemný, lehce kluzký pocit a sladkou vůni; trochu jsem ho dala i na tváře jako rychlou krémovou tvářenku, aby look držel pohromadě.</p>'''),
        ('sprej', 'Finiš: fixační sprej', '''<p class="vtag v-dep">Záleží na typu pleti</p>
<p>Loňský velmi populární sprej (v mém se usadil prášek, takže je zjevně s pudrem: dobře protřepat). Rozprašovač je silný a opravdu všechno zafixuje. Na matný finiš je skvělý; na sušší pleti v kombinaci s bází to pro mě byla prostě příliš silná fixace.</p>'''),
        ('vydrz', 'To podstatné: celý den v make-upu', '''<p>Swatche a první dojem jsou snadné. Dobrý produkt od skvělého odliší to, jak vypadá po hodinách běžného dne. Tady je poctivá časová osa.</p>
<dl class="timeline">
<div><dt>Po 3–4 hodinách</dt><dd>Pleť dostala přirozený lesk, ale pořád vypadala živě, pod očima se nic nezakrčilo a obočí drželo tvar.</dd></div>
<div><dt>Na konci dne</dt><dd>Pleť se leskla (což mi nevadí), pod očima zůstalo čisto, odstín na rtech krásně držel a obočí změklo jen minimálně. Poctivá nevýhoda: pleť jsem měla celý den staženou, což připisuji kombinaci báze a fixačního spreje, která byla na moji normální až smíšenou pleť příliš.</dd></div>
<div><dt>Druhý den</dt><dd>Znovu jsem otestovala jen korektor a pudr přes svou běžnou péči a make-up. Po pěti hodinách se skoro nepohnuly. Korektor a pudr jsou tedy opravdu výborné; stažená, suchá pleť šla na vrub báze, ne podkladu.</dd></div>
</dl>'''),
        ('vyplati', 'Vyplatí se tedy celý obličej NYX?', '''<p>NYX je přesně tím, co slibuje jeho pověst: sebevědomá, spolehlivá značka, která se nenápadně posunula z drogerie do nižší střední třídy. Do pracovního kufru bych si klidně nechala bronzer, kompaktní pudr, gel na obočí, řasenku, dlouhotrvající linky (pro jistou ruku) a korektor na lokální krytí. Vyplňující báze a fixační sprej záleží na typu pleti: skvělé pro smíšenou a mastnou pleť, na suchou pleť je toho moc. Matná paleta je hezká, ale pigment si nejdřív vyzkoušejte. Když zvolíte produkty podle své pleti, NYX si své místo rozhodně zaslouží.</p>'''),
    ],
    lessons_h='Tři věci, které vás tenhle look naučí o vlastním líčení',
    lessons=[('Produkt je tak dobrý, jak dobře sedí vaší pleti.', 'Můj problém s bází nebyl „špatný produkt“, ale špatný produkt pro moji pleť ten den. Naučit se číst vlastní pleť je polovina dobrého make-upu.'),
             ('Technika vítězí nad pigmentem.', 'Jestli pudrujete před stíny, bronzer vtiskáváte nebo roztíráte, nebo hustý korektor zeslabíte, rozhoduje o výsledku mnohem víc technika než cena.'),
             ('Líčení podle dne, který vás čeká.', 'Na <a href="/vecerni-liceni/">akce</a> a <a href="/svatebni-liceni/">svatby</a> sahám po dlouhotrvajících produktech: pudr, voděodolné linky, gel na obočí, a fixaci přizpůsobuji pleti, kterou mám před sebou.')],
    learn_h='Chcete se to naučit pořádně?',
    cta_note='Přesně tyhle dovednosti procházíme individuálně na <a href="/kurzy-liceni/">kurzu líčení</a>: na vašem obličeji, s ohledem na typ vaší pleti a s produkty, které vám opravdu sedí.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Vytvořme váš look',
    cta_text='Ať chcete dokonalý a dlouhotrvající make-up na svatbu nebo jinou událost, nebo se chcete tyto techniky naučit sami, ráda vám pomůžu.',
    cta_links=[('Svatební líčení', '/svatebni-liceni/'), ('Večerní líčení', '/vecerni-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Používají profesionální vizážistky opravdu drogerkové značky jako NYX?', 'Rozhodně. Pracovní kufr je mix cenových kategorií; rozhoduje, jak produkt funguje, ne jeho značka. Několik produktů NYX, třeba bronzer, pudr, řasenka a dlouhotrvající linky, obstojí vedle mnohem dražších.'),
         ('Které produkty NYX v testu dopadly nejlépe?', 'Kultovní bronzer, kompaktní pudr, gel na obočí, řasenka, dlouhotrvající oční linky a korektor na lokální krytí.'),
         ('Je make-up NYX dost dobrý na svatbu nebo dlouhou akci?', 'Dlouhotrvající produkty (pudr, fixační sprej, linky a gel na obočí) vydrží překvapivě dobře. Na svatební den bych přesto doporučila profesionální líčení a předem zkoušku. Co to obnáší, najdete na stránce <a href="/svatebni-liceni/">svatební líčení</a>.'),
         ('Na které produkty NYX si dát pozor?', 'Vyplňující báze může na suché nebo olupující se pleti táhnout a matné stíny jsou hezké, ale méně pigmentované: vyzkoušejte je nejdřív v obchodě.'),
         ('Můžu se takový look naučit sama?', 'Ano, přesně k tomu slouží moje <a href="/kurzy-liceni/">individuální kurzy líčení</a>, přizpůsobené typu vaší pleti a vašim cílům, od každodenního líčení po profesionální techniky.'),
         ('Kde působíte?', 'Jsem vizážistka v Praze a za svatbami, focením a akcemi jezdím po celé České republice i Evropě. <a href="#contact">Kontaktujte mě.</a>')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a editoriálnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

CONTENT = {'summer': SUMMER, 'nyx': NYX}
EXTRA = {'summer': dict(products=SUMMER_PRODUCTS, brands=SUMMER_BRANDS, about=('Make-up bez make-upu', 'No-makeup makeup'), video_name='Summer makeup 2.0'),
         'nyx': dict(products=[], brands=NYX_BRANDS, about=('Recenze NYX', 'NYX makeup review'), video_name='Все обличчя NYX',
                     upload='2026-03-20', video_desc='Nikol Pavlova applies a complete look using only NYX products and tests how it wears over a full day.')}


def words(s):
    return len(re.sub(r'<[^>]+>', ' ', s).split())


def article(key, lang):
    meta, c, t, ex, P = POSTS[key][lang], CONTENT[key][lang], L_BLOG[lang], EXTRA[key], POSTS[key]
    other = POSTS[key]['en' if lang == 'cs' else 'cs']
    path, vid, date = meta['path'], P['video'], P['date']
    body = c['opener'] + c.get('pre', '') + c.get('tested', '') + ''.join(s[2] for s in c['sections'])
    n_words = words(body)
    mins = max(1, round(n_words / 200))
    url = SITE + path
    og = f'{SITE}/assets/og/{og_slug(path)}.jpg'
    art = {'@type': 'BlogPosting', '@id': url + '#article', 'headline': meta['title'], 'description': meta['desc'], 'inLanguage': lang,
           'url': url, 'mainEntityOfPage': url, 'image': og, 'datePublished': date, 'dateModified': '2026-10-21',
           'wordCount': n_words, 'author': {'@id': SITE + '/#person'}, 'publisher': {'@id': SITE + '/#business'},
           'isPartOf': {'@type': 'Blog', '@id': SITE + t['blog_path'] + '#blog', 'name': f'Nikol Pavlova – {t["blog"]}', 'url': SITE + t['blog_path']},
           'about': {'@type': 'Thing', 'name': ex['about'][0 if lang == 'cs' else 1]},
           'mentions': [{'@type': 'Brand', 'name': b} for b in ex['brands']]}
    graph = [art,
             {'@type': 'Person', '@id': SITE + '/#person', 'name': 'Nikol Pavlova', 'jobTitle': 'Vizážistka' if lang == 'cs' else 'Makeup artist',
              'url': SITE + ('/' if lang == 'cs' else '/en/'), 'sameAs': [IG, FB, TH, 'https://www.youtube.com/@nikolpavlova_mua']},
             S.breadcrumb(path, [t['home'], (t['blog'], t['blog_path']), (meta['crumb'], path)]),
             S.faq(path, lang, c['faq'])]
    if ex.get('upload'):
        art['video'] = {'@id': url + '#video'}
        graph.append({'@type': 'VideoObject', '@id': url + '#video', 'name': ex['video_name'], 'description': ex['video_desc'], 'inLanguage': 'uk',
                      'thumbnailUrl': f'https://i.ytimg.com/vi/{vid}/maxresdefault.jpg', 'uploadDate': ex['upload'],
                      'contentUrl': f'https://www.youtube.com/watch?v={vid}', 'embedUrl': f'https://www.youtube.com/embed/{vid}'})
    else:
        art['subjectOf'] = {'@type': 'CreativeWork', 'url': f'https://www.youtube.com/watch?v={vid}', 'name': ex['video_name'] + ' (YouTube)'}
    alt = [('cs', POSTS[key]['cs']['path']), ('en', POSTS[key]['en']['path']), ('x-default', POSTS[key]['cs']['path'])]
    himg = P['img']
    h = head(lang, meta['seo_title'], meta['desc'], path, alt, og, [{'@context': 'https://schema.org', '@graph': graph}],
             preload(himg, '(max-width: 900px) 100vw, 50vw'), og_type='article',
             extra=f'<meta property="article:published_time" content="{date}">')
    h += header(lang, 'blog', other['path'])
    vid_id = 'verdict' if lang == 'en' else 'verdikt'
    toc = ''.join(f'<a href="#{i}">{n}</a>' for i, n in c['toc'])
    steps_html = ''
    if c.get('steps'):
        steps_html = f'<h2 id="{c["toc"][0][0]}">{c["summary_h"]}</h2>\n<ol class="steps-list">{"".join(f"<li>{s}</li>" for s in c["steps"])}</ol>\n'
        steps_html += f'<aside class="note"><p class="lbl red">{c["tested_h"]}</p>{c["tested"]}</aside>\n'
    verdict_html = f'<h2 id="{vid_id}">{c["verdict_h"]}</h2>\n<div class="verdict">' + ''.join(
        f'<div><p class="{cls}">{lab}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for lab, cls, items in c['verdict']) + '</div>\n'
    if c.get('verdict_foot'):
        verdict_html += f'<p class="fine-print">{c["verdict_foot"]}</p>\n'
    secs = ''.join(f'<h2 id="{i}">{ti}</h2>\n{ht}\n' for i, ti, ht in c['sections'])
    lessons_id = 'lessons' if lang == 'en' else 'lekce'
    lessons = ''.join(f'<li><span class="n" aria-hidden="true">{k + 1}</span><div><p><strong>{a_}</strong></p><p class="fs-16">{b_}</p></div></li>' for k, (a_, b_) in enumerate(c['lessons']))
    faq_html = ''.join(f'<details{" open" if k == 0 else ""}><summary><h3>{q}</h3><span class="pm" aria-hidden="true">+</span></summary><div><p>{a_}</p></div></details>' for k, (q, a_) in enumerate(c['faq']))
    links = ''.join(f'<a class="btn btn--ghost c-white" href="{u}">{n}</a>' for n, u in c['cta_links'])
    prod_html = ''
    if ex['products']:
        pid = 'produkty' if lang == 'cs' else 'products'
        prod_html = (f'<h2 id="{pid}">{t["products"]}</h2>\n<p class="fine-print">{t["products_note"]}</p>\n<ul class="prod-list">'
                     + ''.join(f'<li><a href="{u}" rel="nofollow sponsored">{n}</a></li>' for n, u in ex['products']) + '</ul>\n')
    verdict_top = key == 'nyx'
    h += f'''<article aria-labelledby="page-h1">
<header class="page-head post-head pb-48"><div class="wrap stack-28">
{crumbs(lang, [t['home'], (t['blog'], t['blog_path']), (meta['crumb'], None)])}
<p class="lbl muted meta-row"><span class="red">{meta['tag']}</span><time datetime="{date}">{fmt_date(lang, date)}</time><span>{mins} {t['read']}</span></p>
<h1 class="wide big mw-1180" id="page-h1">{meta['title']}</h1>
<div class="byline-bar">
<p class="byline">{I('nikol-portrait', '', sizes='52px', cls='avatar')}<span class="body">{t['by']} <a rel="author" href="{t['home'][1]}#about"><b>Nikol Pavlova</b></a> <span class="serif fs-18">– {t['role']}</span></span></p>
<a class="link-arrow" href="#{vid_id}">{t['jump']}</a></div>
</div></header>
<a class="video-split" href="https://www.youtube.com/watch?v={vid}">{I(himg, meta['title'], sizes='(max-width: 900px) 100vw, 50vw', priority=True)}<span class="vs-panel"><span class="play glass" aria-hidden="true"><svg width="34" height="34" viewBox="0 0 24 24" fill="#A8232F"><path d="M8 5l12 7-12 7z"/></svg></span><span class="lbl">{t['watch']}</span><span class="serif vs-title">{ex['video_name']}</span></span></a>
<div class="sec"><div class="wrap post-layout">
<aside class="post-toc"><p class="lbl red">{t['toc']}</p><nav class="toc bt-ink" aria-label="{t['toc']}">{toc}</nav></aside>
<div class="art">
<p class="opener">{c['opener']}</p>
{c.get('pre', '')}
{steps_html}{verdict_html if verdict_top else ''}{secs}
{'' if verdict_top else verdict_html}
<h2 id="{lessons_id}">{c['lessons_h']}</h2>
<ol class="lessons">{lessons}</ol>
<aside class="note note--row"><div class="mw-480"><p class="wide note-title">{c['learn_h']}</p><p>{c['cta_note']}</p></div><a class="btn" href="{c['cta_btn'][1]}">{c['cta_btn'][0]}</a></aside>
<section class="cta-box" aria-labelledby="cta-h">
<h2 id="cta-h" class="cta-box__title">{c['cta_title']}</h2>
<p class="serif lead-on-ox">{c['cta_text']}</p>
<p class="actions-sm"><a class="btn btn--pink c-ox" href="{CAL}">{'Rezervace online +' if lang == 'cs' else 'Book online +'}</a>{links}</p>
</section>
{prod_html}<h2 id="faq">{c['faq_h']}</h2>
<div class="faq bt-0">{faq_html}</div>
<div class="author">{I('nikol-portrait', 'Nikol Pavlova', sizes='112px')}<div class="author-body"><p class="wide author-name">Nikol Pavlova</p><p class="serif muted2 fs-18">{'Vizážistka · Praha' if lang == 'cs' else 'Makeup Artist · Prague'}</p><p class="small-copy">{c['bio']}</p><p class="actions-sm"><a class="lbl" href="{IG}">Instagram</a><a class="lbl" href="https://www.youtube.com/@nikolpavlova_mua">YouTube</a></p></div></div>
</div></div></div>
</article>
'''
    h += teaser(lang, [k for k in ORDER if k != key], 'Další články' if lang == 'cs' else 'More articles', 'z blogu' if lang == 'cs' else 'from the blog', hid='more-h')
    h += footer(lang, 'Kontaktujte mě' if lang == 'cs' else 'Contact me',
                'Potřebujete pomoc s líčením?' if lang == 'cs' else 'Do you need help with creative make-up?',
                'Profesionální vizážistka v Praze. Líčení, které zvýrazní vaši přirozenou krásu.' if lang == 'cs' else 'Professional makeup artist based in Prague. Designing bespoke beauty looks that reflect your distinct personality.')
    write(path, h)


# ---------------------------------------------------------------- blog index
def index(lang):
    t = L_BLOG[lang]
    path = t['blog_path']
    P = POSTS[ORDER[0]]
    p = P[lang]
    if lang == 'cs':
        title = 'Blog – tutoriály, recenze a tipy vizážistky | Nikol Pavlova, Praha'
        desc = 'Tutoriály, poctivé recenze kosmetiky a profesionální tipy od vizážistky Nikol Pavlové z Prahy.'
        h1, sub = 'Blog', '– tutoriály, recenze a tipy vizážistky z Prahy'
        lead = 'Postupy, které používám na klientkách i na sobě, a poctivé recenze produktů. Psáno tak, abyste si vybrali lepší kosmetiku a vytvořili look, který vám sedí.'
        latest, more, topics_h, topics_sub, read_btn = 'Nejnovější článek', 'Další články', 'Témata', 'o čem píšu', 'Číst článek →'
        topics = [('Tutoriály', 'Krok za krokem: přirozený, letní i večerní make-up.', '1 článek', True),
                  ('Recenze produktů', 'Testuji kosmetiku na sobě i v práci a říkám, co se vyplatí.', '1 článek', True),
                  ('Svatby a akce', 'Jak se připravit na make-up, který vydrží celý den.', 'Připravujeme', False)]
        alt = [('cs', path), ('en', '/en/blog/'), ('x-default', path)]
    else:
        title = 'Blog – Makeup Tutorials, Reviews & Tips | Nikol Pavlova, Prague'
        desc = 'Makeup tutorials, honest product reviews and professional tips from Nikol Pavlova, an English-speaking makeup artist based in Prague.'
        h1, sub = 'The Blog', '– makeup tutorials, reviews &amp; tips from Prague'
        lead = 'Routines I use on clients and on myself, plus honest product reviews, written to help you choose better products and create looks that suit you.'
        latest, more, topics_h, topics_sub, read_btn = 'Latest article', 'More articles', 'Topics', 'what I write about', 'Read the article →'
        topics = [('Tutorials', 'Step by step: natural, summer and evening makeup.', '1 article', True),
                  ('Product reviews', 'I test products on myself and at work and tell you what is worth it.', '1 article', True),
                  ('Bridal &amp; events', 'How to prepare for makeup that lasts all day.', 'Coming soon', False)]
        alt = [('cs', '/blog/'), ('en', path), ('x-default', '/blog/')]
    graph = [{'@type': 'Blog', '@id': SITE + path + '#blog', 'name': f'Nikol Pavlova – {t["blog"]}', 'url': SITE + path, 'inLanguage': lang,
              'author': {'@id': SITE + '/#person'}, 'publisher': {'@id': SITE + '/#business'},
              'blogPost': [{'@id': SITE + POSTS[k][lang]['path'] + '#article'} for k in ORDER]},
             S.breadcrumb(path, [t['home'], (t['blog'], path)])]
    h = head(lang, title, desc, path, alt, '', [{'@context': 'https://schema.org', '@graph': graph}])
    h += header(lang, 'blog', '/en/blog/' if lang == 'cs' else '/blog/')
    topic_html = ''.join(f'<li><h3>{a_}</h3><p>{b_}</p><span class="lbl {"red" if live else "muted2"}">{n}</span></li>' for a_, b_, n, live in topics)
    h += f'''<section class="page-head" aria-labelledby="page-h1"><div class="wrap">
{crumbs(lang, [t['home'], (t['blog'], None)])}
<div class="top"><h1 class="h1" id="page-h1"><span class="big wide">{h1}</span><span class="sub serif">{sub}</span></h1>
<p class="body">{lead}</p></div>
</div></section>
<section class="sec--tight" aria-labelledby="latest-h"><div class="wrap">
<h2 class="visually-hidden" id="latest-h">{latest}</h2>
<article><a class="feat" href="{p['path']}">{I(P['img'], p['title'], sizes='(max-width: 900px) 100vw, 1280px', cls='fp-30', priority=True)}<span class="badge lbl glass">{latest}</span>
<div class="card glass"><p class="lbl muted meta-row-sm"><span class="red">{p['tag']}</span><time datetime="{P['date']}">{fmt_date(lang, P['date'])}</time></p>
<h3 class="wide feat-title">{p['title']}</h3>
<p class="c-text">{p['card']}</p>
<span class="btn self-start">{read_btn}</span></div></a></article>
</div></section>
<section class="sec--tight" aria-labelledby="more-h"><div class="wrap">
{sec_head(more, '', hid='more-h')}
{cards(lang, ORDER[1:])}
</div></section>
<section class="sec sec--blush" aria-labelledby="topics-h"><div class="wrap">
{sec_head(topics_h, topics_sub, hid='topics-h')}
<ul class="topic-rows">{topic_html}</ul></div></section>
'''
    h += footer(lang, 'Kontaktujte mě' if lang == 'cs' else 'Contact me',
                'Potřebujete pomoc s líčením?' if lang == 'cs' else 'Do you need help with creative make-up?',
                'Profesionální vizážistka v Praze.' if lang == 'cs' else 'Professional makeup artist based in Prague.')
    write(path, h)


def build():
    for lang in ('cs', 'en'):
        index(lang)
        for k in ORDER:
            article(k, lang)
