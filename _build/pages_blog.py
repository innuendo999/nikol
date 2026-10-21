"""Blog: index pages (CZ + EN) and articles based on Nikol's YouTube videos."""
import re
from lib import *
from lib import img as I
import schema as S

PUBLISHED = '2026-10-21'

POSTS = {
    'summer': {
        'video': 'pg2rs7CB6lA',
        'cs': dict(path='/blog/letni-make-up-bez-make-upu/', crumb='Letní make-up bez make-upu',
                   title='Letní make-up bez make-upu: rutina vizážistky na horké dny',
                   seo_title='Letní make-up bez make-upu: rutina vizážistky | Nikol Pavlova',
                   desc='Vizážistka z Prahy ukazuje lehký letní make-up: péče s SPF, odstín make-upu pro pihovatou pleť, blur místo lesku, krémové barvy prsty a fixační spreje, které se vyplatí.',
                   tag='Tutoriál', card='Lehký letní make-up, který se nebojí horka: odstín pro pihovatou pleť, blur jen tam, kde je potřeba, a test fixačních sprejů.'),
        'en': dict(path='/en/blog/summer-no-makeup-makeup/', crumb='Summer no-makeup makeup',
                   title="Summer No-Makeup Makeup: A Makeup Artist's Routine for Hot Days",
                   seo_title='Summer No-Makeup Makeup Routine | Nikol Pavlova, Prague MUA',
                   desc='Prague makeup artist Nikol Pavlova shares her light summer routine: SPF skin prep, matching foundation on freckled skin, blur instead of shine, cream colour with fingers and the setting sprays worth buying.',
                   tag='Tutorial', card='A light summer face that copes with heat: foundation shades for freckled skin, blur only where you need it, and a setting spray test.'),
    },
}
NYX = dict(path='/en/blog/full-face-of-nyx-review/', title="Full Face of NYX: A Makeup Artist's Honest Review", date='2026-03-20',
           card='I tested a full face of NYX and wore it through a working day: what earned a place in my kit and what I would skip.')

L_BLOG = {
    'cs': dict(home=('Domů', '/'), blog='Blog', blog_path='/blog/', read='min čtení', by='Autorka', role='vizážistka, Praha',
               toc='V článku', watch='Celý tutoriál na YouTube · mluvený v ukrajinštině', jump='Přejít na verdikt ↓',
               months=['ledna', 'února', 'března', 'dubna', 'května', 'června', 'července', 'srpna', 'září', 'října', 'listopadu', 'prosince']),
    'en': dict(home=('Home', '/en/'), blog='Blog', blog_path='/en/blog/', read='min read', by='By', role='Professional Makeup Artist, Prague',
               toc='In this article', watch='Watch the full tutorial on YouTube · spoken in Ukrainian', jump='Jump to the verdict ↓',
               months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
}


def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split('-'))
    mn = L_BLOG[lang]['months'][m - 1]
    return f'{d}. {mn} {y}' if lang == 'cs' else f'{d} {mn} {y}'


# ---------------------------------------------------------------- article copy
SUMMER = {}

SUMMER['cs'] = dict(
    toc=[('kratce', 'Postup v kostce'), ('pece', 'Péče a SPF'), ('odstin', 'Odstín pro pihovatou pleť'), ('fluidy', 'Lehké fluidy'),
         ('blur', 'Blur místo lesku'), ('teplo', 'Teplo do pleti'), ('korekce', 'Korekce bez korektoru'), ('oboci', 'Obočí'),
         ('tvare', 'Tváře a rty prsty'), ('oci', 'Řasy'), ('pudr', 'Pudr a rty'), ('spreje', 'Fixační spreje'), ('zaver', 'Rozjasnění a SPF přes den'),
         ('verdikt', 'Verdikt'), ('faq', 'Časté dotazy')],
    opener='Make-up bez make-upu je v létě můj nejčastější look. Pleť má vypadat svěže a lehce, v horku nesmí stékat a hlavně ho chci kdykoli smýt, obnovit SPF a během deseti minut udělat znovu. V tomhle tutoriálu ukazuji celý postup krok za krokem a u každého produktu říkám, co si o něm myslím jako vizážistka.',
    intro='Tenhle postup není pro vás, pokud chcete plné krytí nebo výrazný večerní make-up. Je pro dny u vody, na dovolené nebo ve městě v horku, kdy chcete vypadat odpočatě, ale ne „namalovaně“. Na videu mám lehčí verzi; níže popisuji i kroky, které můžete přidat.',
    tested='Mám smíšenou pleť, která je s věkem a v horku mastnější, hlavně když málo piju. K tomu pihy s teplým khaki podtónem, zarudnutí kolem nosu a studený fialový stín pod jedním okem. Podklad jsem měla na sobě několik hodin, než jsem začala natáčet, a pořád vypadal svěže.',
    steps=['Tonikum a SPF 50 i na krk a dekolt', 'Odstín make-upu podle důlku nad hrudní kostí, ne podle krku', 'Lehký fluid jen tam, kde je potřeba', 'Silikonová báze s blur efektem jen na T-zónu a stíny', 'Krémový bronzer pro teplo', 'Krémová paleta prsty na kruhy a zarudnutí', 'Obočí, řasenka, pudr jen na problémová místa', 'Fixační sprej a kapka rozjasňovače'],
    sections=[
        ('pece', 'Krok 1: péče a SPF', '''<p>Pěnové čisticí přípravky většinou vynechávám, moje pleť je nepotřebuje. Začínám tonikem od <b>Medicube</b>: je řídké, lehké a nezanechává pocit „právě umyté“ pleti. Hodí se i pro mastnou pleť.</p>
<p>Pak přichází <b>SPF 50 s vitaminem C</b>. Je to pro mě tři v jednom: hydratuje, chrání a rozjasňuje, takže v létě vynechávám sérum i krém. Má tekutou, nelepivou texturu, což pomáhá všem, kdo nesnášejí pocit opalovacího krému na obličeji. Nanáším ho i pod oči, na krk a na dekolt.</p>
<aside class="note"><p class="lbl red">Pozor</p><p>Vitamin C může citlivou pleť dráždit. Pokud máte reaktivní pleť, zkuste SPF nejdřív na malé ploše.</p></aside>'''),
        ('odstin', 'Krok 2: odstín make-upu pro pihovatou pleť', '''<p>Pihovatá pleť se studeným, narůžovělým podtónem vypadá ve světlém make-upu snadno šedě. Pleť je potřeba trochu zahřát, ale ne tolik, aby obličej zoranžověl a tělo zůstalo bílé. Mně funguje <b>Chanel Les Beiges v odstínu B30</b>: díky teplému tónu pihy nešednou.</p>
<aside class="note"><p class="lbl red">Tip vizážistky</p><p class="serif fs-20">Odstín nevybírejte podle krku. Ten se často neopálí a bývá světlejší. Porovnávejte s důlkem nad hrudní kostí, mezi krkem a dekoltem.</p></aside>
<p>Lidé s pihami je mívají na zádech, rukou a ramenou, ale na krku málokdy. Proto je krk pro výběr odstínu zavádějící.</p>'''),
        ('fluidy', 'Krok 3: lehké fluidy místo make-upu', '''<p>Porovnávám dva fluidy. První, velmi lehký tónovací fluid, pleť jen jemně sjednotí a zarudnutí nepřekryje. Pro mě je skoro zbytečný, dopotřebovávám ho, aby se nezkazil. Hustší fluid na vodní bázi kryje znatelně víc, vydrží dlouho a koupila bych ho znovu, i když je drahý. Sahám po něm ve dny, kdy nemám čas a chci rychle zakrýt červený nos.</p>
<p>Pro mastnou pleť bývá lepší ta lehčí varianta. Výdrž mají oba podobnou a během dne se mohou trochu setřít, což u make-upu bez make-upu nevadí.</p>'''),
        ('blur', 'Krok 4: blur místo lesku', '''<p>Moje nová fáze: místo jednoho podkladového produktu vrstvím několik a hlavně používám <b>silikonové báze s blur efektem</b> jen tam, kde lesk nechci. Lesk je krásný na dokonale hladké pleti bez viditelných pórů a stínů. Na mé pleti se začínají objevovat první změny, třeba nová vráska, takže už nelesknu celý obličej.</p>
<p>Nanáším je na T-zónu, kousek na čelo, po stranách nosu a do prohlubní, kde vznikají stíny. Kam přesně, zjistíte jednoduše: natočte obličej ke světlu a podívejte se, kde se odráží.</p>
<ul><li><b>Hourglass Veil</b> používám hlavně na klientky.</li><li><b>Dior</b> je o něco lehčí, ale mastnější a na práci se mi hodí méně.</li><li>Pro sebe mám levnější <b>e.l.f.</b> s lehkým tónem; je mastnější, proto na klientky ne.</li></ul>
<p>Produkt před použitím dobře protřepejte, aby se pigment rozmíchal. Stačí jedna pumpička. Nanáším prstem a na přesná místa štětcem, nezapomínám na uši, vlasovou linii, klíční kosti a dekolt. Cílem není plochý obličej, ale satén: vyvážený lesk a blur.</p>'''),
        ('teplo', 'Krok 5: teplo do pleti', '''<p>Jako krémový bronzer používám mini <b>Charlotte Tilbury Hollywood Flawless Filter</b> v jednom z tmavších odstínů. Dlouho vydrží, odráží světlo a pleť vypadá přirozeně. Má ale výrazně oranžový podtón, který nesedne každému. Na pihovatou pleť v létě ho mám ráda.</p>
<p>Tady můžete klidně skončit: přidejte lesk na rty, rozjasňovač a obočí a look je hotový.</p>'''),
        ('korekce', 'Krok 6: korekce bez korektoru', '''<p>Na kruhy pod očima, zarudnutí a jemné stínování používám krémovou paletu <b>Make Up For Ever</b>, kterou jsem si dlouho přála a koupila na masterclassu. Má odstíny na kruhy, zarudnutí i bronzování a tvářenky jsou úžasné.</p>
<p>Na svatby a klientky, které potřebují dlouhou výdrž a plné krytí, ale není. Je jemná, méně pigmentovaná a snadno se setře. Na focení ano, na celý den ne. Je to drahý produkt, takže je dobré znát jeho limity.</p>
<p><b>Postup pod očima:</b> druhý nejsvětlejší odstín vtiskněte jedním prstem do místa, kde je kruh nejtmavší, a druhým prstem rozmažte jen okraje. Střed nechte, tam má být nejvíc pigmentu. Pod oči dávám korektor málokdy, kůže se tam při mimice krčí a u make-upu bez make-upu platí: čím méně, tím lépe.</p>
<p>Na zarudnutí stačí prstem poklepat, jemný kontur pod lícní kosti a trochu světla na čelo přidají objem. Místo palety poslouží jakýkoli lehký, nemastný make-up na silikonové bázi. Pro detaily používám sérum korektor <b>NYX Bare With Me</b> v odstínu Vanilla, který jsem testovala ve <a href="/en/blog/full-face-of-nyx-review/" hreflang="en">velké recenzi NYX</a>. Modřinu pod okem každý den úplně nezakrývám, s plným krytím se necítím tak živě.</p>'''),
        ('oboci', 'Krok 7: obočí', '<p>Mezery doplňuji suchou, pudrovou tužkou <b>Zola</b> pro blondýnky, která má skvělý pigment, a fixuji gelem <b>NYX The Brow Glue</b>. Víc nedělám.</p>'),
        ('tvare', 'Krok 8: tváře a rty prsty', '''<p>Pro efekt „políbené sluncem“ přidávám jen kapku bronzeru. Tvářenku a bronzer zároveň moc nenosím. Krémový produkt nanáším jedním prstem a čistým prstem roztírám. Na pleti není make-up, takže se všechno krásně prolne. Stejný produkt dávám prsty i na rty.</p>
<p>Když je něco moc výrazné, přejdu to zbytkem korektoru.</p>'''),
        ('oci', 'Krok 9: řasy', '<p>Mám dlouhé, rovné řasy, takže je natáčím. Natočím jedno oko, udělám make-up a pak natočím druhé, protože řasy rychle padají. Používám hnědou řasenku <b>Lancôme Lash Idôle</b>, která se na rozdíl od mnoha jiných nikdy nedrolí. Nanáším ji i na spodní řasy. Některé dny řasy vynechám úplně.</p>'),
        ('pudr', 'Krok 10: pudr jen tam, kde je potřeba, a rty', '''<p>Fixační pudr <b>e.l.f.</b> je neuvěřitelný a stačí ho opravdu málo. Naberu ho na štětec, skoro všechno oklepu a vtisknu jen tam, kde nechci lesk: pod oči, na bradu, kolem nosu a na čelo. Hlavně ho tisknu na místa s korektorem, aby se nekrčil. Pleť je rozmazaná a zafixovaná, ale nevypadá napudrovaně ani vysušeně.</p>
<p>Na rty jsem si vzala odstín 01 od <b>Yves Rocher</b> a navrch rtěnku <b>Chanel Rouge Coco v odstínu 54 Boy</b>, kterou jsem objevila nedávno a zamilovala si ji. Nanáším ji schválně trochu neuspořádaně, aby působila přirozeně.</p>'''),
        ('spreje', 'Krok 11: fixační spreje v testu', '''<p>Fixačních sprejů mám víc, tak jsem je porovnala:</p>
<dl class="rows">
<div><dt class="k">Charlotte Tilbury Airbrush Flawless</dt><dd class="v">můj favorit pro sebe i na práci; fixuje a dodá pěkný glow</dd></div>
<div><dt class="k">Fenty Beauty</dt><dd class="v">krásný lesk a příjemná vůně, ale po bakingu a ve velkém množství se slije</dd></div>
<div><dt class="k">Caudalie Beauty Elixir</dt><dd class="v">nefixuje, hydratuje a voní létem; obsahuje alkohol</dd></div>
<div><dt class="k">Mini spreje e.l.f. a Sephora</dt><dd class="v">nefixují vůbec nic</dd></div>
<div><dt class="k">Silné fixační spreje</dt><dd class="v">jako lak na vlasy pro obličej; na lehký make-up zbytečné</dd></div>
</dl>
<p class="mt-16">U Charlotte Tilbury nejdřív jednou stříkněte stranou, aby velké kapky nedopadly na obličej. Caudalie mám od roku 2021, kdy jsem se přestěhovala do Česka, a je to asi moje třetí nebo čtvrtá lahvička. Pokud vám alkohol v kosmetice nedělá dobře, zkontrolujte složení.</p>'''),
        ('zaver', 'Krok 12: rozjasnění a SPF přes den', '''<p>Na lícní kosti dávám prstem trochu rozjasňovače <b>Charlotte Tilbury</b> s jemně růžovým tónem. Třpytivé tyčinky na okraje obličeje fungují, ale ne na pleti s texturou, rozšířenými póry nebo jizvami. Přes den nepřeplácávám akcenty; večer, kdy se mění světlo, přidávám víc bronzeru a tvářenky.</p>
<p><b>SPF přes den:</b> krémové SPF přes make-up nevrstvím, na zaprášenou pleť pod make-upem to podle mě není dobrý nápad. Proto je celá rutina tak lehká: na pláži obličej umyju, obnovím SPF a za pár minut ji udělám znovu.</p>'''),
    ],
    verdict=[('Vyplatí se', 'vtag v-yes', ['Charlotte Tilbury Airbrush Flawless sprej', 'Lancôme Lash Idôle, hnědá', 'NYX Bare With Me korektor', 'Fixační pudr e.l.f.', 'Chanel Rouge Coco 54 Boy', 'Caudalie Beauty Elixir (hydratace)']),
             ('Záleží na pleti', 'vtag v-dep', ['Hollywood Flawless Filter (oranžový tón)', 'Paleta Make Up For Ever (nízká výdrž)', 'Sprej Fenty Beauty (v malém množství)', 'SPF s vitaminem C (citlivá pleť)']),
             ('Spíš ne', 'vtag v-sw', ['Mini spreje e.l.f. a Sephora', 'Silné fixační spreje na lehký make-up'])],
    lessons=[('Odstín vybírejte podle hrudníku, ne podle krku.', 'U pihovaté pleti rozhoduje teplý tón. Šedý obličej prozradí špatný odstín víc než jakékoli krytí.'),
             ('Blur jen tam, kde je potřeba.', 'Zbytek pleti nechte přirozeně saténový. Dokonale matný obličej v létě nevypadá svěže.'),
             ('Méně korektoru pod očima.', 'Pigment vtiskněte do nejtmavšího místa a rozmažte jen okraje. Make-up se pak nekrčí.')],
    cta_note='Chcete se tenhle postup naučit na vlastní pleti? Přesně to procházíme na <a href="/kurzy-liceni/">individuálním kurzu líčení</a>: s vašimi produkty a s ohledem na typ vaší pleti.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Nechte se nalíčit na focení nebo událost',
    cta_text='Přirozený look, který vydrží focení i celý den, dělám i pro klientky: na zásnubní focení, portréty nebo civilní obřad.',
    cta_links=[('Nude líčení', '/nude-liceni/'), ('Kurzy líčení', '/kurzy-liceni/')],
    faq=[('Co je make-up bez make-upu?', 'Lehký look, který sjednotí pleť, opraví jen to, co je vidět, a zvýrazní vaše rysy tak, aby make-up nebyl poznat. Místo plného krytí se pracuje s lehkými fluidy, krémovými produkty a pudrem jen na vybraná místa.'),
         ('Jak vybrat odstín make-upu, když mám pihy?', 'Porovnávejte s důlkem nad hrudní kostí, ne s krkem, který bývá světlejší. Pihovatá pleť se studeným podtónem potřebuje trochu teplejší odstín, jinak vypadá šedě, ale ne tak teplý, aby obličej zoranžověl.'),
         ('Jak v létě omezit lesk, aby pleť nevypadala plochá?', 'Silikonovou bázi s blur efektem dejte jen na T-zónu, kolem nosu a do prohlubní, kde vznikají stíny. Pudr vtiskněte jen na stejná místa. Zbytek pleti nechte saténový.'),
         ('Jaký fixační sprej je nejlepší na léto?', 'Na fixaci se mi nejvíc osvědčil Charlotte Tilbury Airbrush Flawless, na hydrataci Caudalie Beauty Elixir. Mini spreje e.l.f. a Sephora podle mého testu nefixují.'),
         ('Můžu přes make-up během dne obnovit SPF?', 'Krémové SPF přes make-up nevrstvím, na zaprášenou pleť to podle mě není dobrý nápad. Tahle rutina je proto tak lehká, aby se dala smýt, obnovit SPF a za pár minut udělat znovu.'),
         ('Můžu se tenhle look naučit?', 'Ano. Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> v Praze ho projdeme krok za krokem na vaší pleti a s vašimi produkty. Pokud chcete look na focení nebo obřad, podívejte se na <a href="/nude-liceni/">nude líčení</a>.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

SUMMER['en'] = dict(
    toc=[('summary', 'The routine in short'), ('skin', 'Skin prep and SPF'), ('shade', 'Shades for freckled skin'), ('fluids', 'Light fluids'),
         ('blur', 'Blur instead of shine'), ('warmth', 'Warmth'), ('correct', 'Correcting without concealer'), ('brows', 'Brows'),
         ('cheeks', 'Cheeks and lips with fingers'), ('lashes', 'Lashes'), ('powder', 'Powder and lips'), ('sprays', 'Setting sprays'), ('finish', 'Glow and SPF during the day'),
         ('verdict', 'The verdict'), ('faq', 'FAQ')],
    opener='No-makeup makeup is my most worn look every summer. Skin should look fresh and light, it must survive the heat, and above all I want to be able to wash it off, reapply SPF and redo it in ten minutes. In this tutorial I go through the whole routine step by step and tell you what I honestly think of every product as a makeup artist.',
    intro="This routine isn't for you if you want full coverage or a statement evening look. It's for beach days, holidays and hot city days when you want to look rested, not \"done\". In the video I wear a lighter version; below I also describe the steps you can add.",
    tested="My skin is combination and has become oilier with age and heat, especially when I don't drink enough water. I have freckles with a warm khaki undertone, redness around the nose and a cool purple shadow under one eye. I had been wearing the base for a few hours before filming and it still looked fresh.",
    steps=['Toner and SPF 50, including neck and décolleté', 'Match foundation to the hollow above your breastbone, not your neck', 'A light fluid only where you need it', 'A blurring silicone primer only on the T-zone and shadows', 'A cream bronzer for warmth', 'A cream palette with fingers for circles and redness', 'Brows, mascara, powder only where it shines', 'Setting spray and a touch of highlighter'],
    sections=[
        ('skin', 'Step 1: skin prep and SPF', '''<p>I usually skip foaming cleansers; my skin doesn't need them. I start with a <b>Medicube</b> toner: thin, light and without that "just washed" tight feeling. It suits oily skin too.</p>
<p>Next comes an <b>SPF 50 with vitamin C</b>. For me it's three in one: it hydrates, protects and brightens, so in summer I skip serum and moisturiser. The texture is liquid and not sticky, which helps anyone who hates the feel of sunscreen on the face. I apply it under the eyes, on the neck and on the décolleté too.</p>
<aside class="note"><p class="lbl red">Note</p><p>Vitamin C can irritate sensitive skin. If your skin is reactive, patch-test the SPF first.</p></aside>'''),
        ('shade', 'Step 2: foundation shades for freckled skin', '''<p>Freckled skin with a cool, pinkish undertone easily looks grey in a light foundation. You need to warm the complexion up, but not so much that the face turns orange while the body stays white. What works for me is <b>Chanel Les Beiges in B30</b>: the warm tone keeps freckles from going grey.</p>
<aside class="note"><p class="lbl red">Pro tip</p><p class="serif fs-20">Don't match your foundation to your neck. It often doesn't tan and is usually lighter. Match it to the hollow above your breastbone, between the neck and the chest.</p></aside>
<p>People with freckles tend to have them on the back, arms and shoulders, but rarely on the neck. That's why the neck is misleading when you choose a shade.</p>'''),
        ('fluids', 'Step 3: light fluids instead of foundation', '''<p>I compare two fluids. The first, a very sheer tinted fluid, only slightly evens out the skin and doesn't cover redness. For me it's almost pointless; I'm only using it up so it doesn't expire. The second, a denser water-based fluid, covers noticeably more, lasts well and I would buy it again even though it's expensive. I reach for it on days when I have no time and want to cover my red nose quickly.</p>
<p>The lighter one is usually better for oily skin. Both last about the same and can wear off a little during the day, which doesn't matter for a no-makeup look.</p>'''),
        ('blur', 'Step 4: blur instead of shine', '''<p>My new phase: instead of one base product I layer several, and above all I use <b>blurring silicone primers</b> only where I don't want shine. Glow looks beautiful on perfectly smooth skin without visible pores or shadows. My skin is starting to show the first changes, like a new crease, so I no longer make the whole face glow.</p>
<p>I apply them to the T-zone, a little on the forehead, along the sides of the nose and into the hollows where shadows form. To find the right spots, turn your face towards the light and look at where it reflects.</p>
<ul><li><b>Hourglass Veil</b> is the one I use mostly on clients.</li><li><b>Dior</b> is a little lighter but oilier, and works less well for me professionally.</li><li>For myself I use a cheaper tinted <b>e.l.f.</b> primer; it's greasier, so not for clients.</li></ul>
<p>Shake the product well so the pigment mixes. One pump is enough. I apply it with a finger and use a brush for precise areas, and I don't forget the ears, hairline, collarbones and chest. The goal isn't a flat face but a satin finish: a balance of glow and blur.</p>'''),
        ('warmth', 'Step 5: warmth', '''<p>As a cream bronzer I use a mini <b>Charlotte Tilbury Hollywood Flawless Filter</b> in one of the deeper shades. It lasts, reflects light and looks natural on the skin. It does have a distinctly orange undertone that won't suit everyone. On freckled skin in summer, I love it.</p>
<p>You can stop here: add lip gloss, highlighter and brows, and the look is done.</p>'''),
        ('correct', 'Step 6: correcting without concealer', '''<p>For under-eye circles, redness and soft shading I use a <b>Make Up For Ever</b> cream palette that I'd wanted for a long time and finally bought at a masterclass. It has shades for circles, redness and bronzing, and the blushes are amazing.</p>
<p>It isn't for weddings or clients who need long wear and full coverage, though. It's delicate, less pigmented and wears off easily. Great for photo shoots, not for a full day. It's an expensive product, so it's worth knowing its limits.</p>
<p><b>Under-eye technique:</b> press the second-lightest shade with one finger into the darkest part of the circle, and blend only the edges with another finger. Leave the centre alone; that's where you want the most pigment. I rarely put concealer under my eyes because the skin creases with expression, and for no-makeup makeup less is more.</p>
<p>Tap the redness with a finger, add a soft contour under the cheekbones and a little light on the forehead for dimension. Any light, non-greasy silicone-based foundation can replace the palette. For details I use the <b>NYX Bare With Me</b> serum concealer in Vanilla, which I tested in my <a href="/en/blog/full-face-of-nyx-review/">full NYX review</a>. I don't fully cover the bruise under my eye every day; with full coverage I don't feel as lively.</p>'''),
        ('brows', 'Step 7: brows', '<p>I fill the gaps with a dry, powdery <b>Zola</b> pencil for blondes, which has great pigment, and set them with <b>NYX The Brow Glue</b>. That\'s all.</p>'),
        ('cheeks', 'Step 8: cheeks and lips with fingers', '''<p>For a sun-kissed effect I add just a touch of bronzer; I rarely wear blush and bronzer together. I apply the cream with one finger and blend with a clean one. There's no foundation on the skin, so everything melts in easily. I put the same product on my lips with my fingers.</p>
<p>If something looks too strong, I go over it with what's left of the concealer.</p>'''),
        ('lashes', 'Step 9: lashes', '<p>My lashes are long and straight, so I curl them. I curl one eye, do my makeup, then curl the other, because the curl drops quickly. I use <b>Lancôme Lash Idôle</b> in brown, which unlike many mascaras never flakes. I apply it to the lower lashes too. Some days I skip lashes altogether.</p>'),
        ('powder', 'Step 10: powder only where you need it, and lips', '''<p>The <b>e.l.f.</b> setting powder is incredible and you need very little. I pick it up with a brush, tap almost all of it off and press it only where I don't want shine: under the eyes, on the chin, around the nose and on the forehead. Above all I press it over concealer so it doesn't crease. The skin looks blurred and set, but not powdery or dry.</p>
<p>On the lips I used shade 01 from <b>Yves Rocher</b> and on top <b>Chanel Rouge Coco in 54 Boy</b>, which I discovered recently and fell in love with. I apply it slightly messy on purpose so it looks natural.</p>'''),
        ('sprays', 'Step 11: setting sprays, tested', '''<p>I own several setting sprays, so I compared them:</p>
<dl class="rows">
<div><dt class="k">Charlotte Tilbury Airbrush Flawless</dt><dd class="v">my favourite for myself and for work; sets and adds a nice glow</dd></div>
<div><dt class="k">Fenty Beauty</dt><dd class="v">lovely glow and scent, but cakes if you drench it over baked powder</dd></div>
<div><dt class="k">Caudalie Beauty Elixir</dt><dd class="v">doesn't set; hydrates and smells like summer; contains alcohol</dd></div>
<div><dt class="k">e.l.f. and Sephora minis</dt><dd class="v">don't set anything at all</dd></div>
<div><dt class="k">Heavy-duty setting sprays</dt><dd class="v">hairspray for the face; pointless for light makeup</dd></div>
</dl>
<p class="mt-16">With Charlotte Tilbury, spray once to the side first so the big droplets don't land on your face. I've used Caudalie since 2021, when I moved to the Czech Republic; this is probably my third or fourth bottle. If alcohol in skincare doesn't agree with you, check the ingredients.</p>'''),
        ('finish', 'Step 12: glow and SPF during the day', '''<p>I tap a little <b>Charlotte Tilbury</b> highlighter with a soft rosy tone onto my cheekbones with a finger. Shimmer sticks on the outer face work, but not on skin with texture, enlarged pores or scarring. During the day I don't overdo accents; in the evening, when the light changes, I add more bronzer and blush.</p>
<p><b>SPF during the day:</b> I don't layer cream SPF over makeup; on dusty skin under makeup I don't think it's a good idea. That's exactly why the routine is so light: at the beach I wash my face, reapply SPF and redo it in a few minutes.</p>'''),
    ],
    verdict=[('Worth buying', 'vtag v-yes', ['Charlotte Tilbury Airbrush Flawless spray', 'Lancôme Lash Idôle, brown', 'NYX Bare With Me concealer', 'e.l.f. setting powder', 'Chanel Rouge Coco 54 Boy', 'Caudalie Beauty Elixir (hydration)']),
             ('Depends on your skin', 'vtag v-dep', ['Hollywood Flawless Filter (orange undertone)', 'Make Up For Ever palette (short wear)', 'Fenty Beauty spray (use lightly)', 'SPF with vitamin C (sensitive skin)']),
             ('Skip', 'vtag v-sw', ['e.l.f. and Sephora mini sprays', 'Heavy-duty sprays on light makeup'])],
    lessons=[('Match your chest, not your neck.', 'On freckled skin the warm undertone matters most. A grey face gives away the wrong shade more than any coverage does.'),
             ('Blur only where you need it.', 'Leave the rest of the skin naturally satin. A fully matte face never looks fresh in summer.'),
             ('Less concealer under the eyes.', 'Press pigment into the darkest spot and blend only the edges. That way the makeup doesn\'t crease.')],
    cta_note='Want to learn this routine on your own skin? That\'s exactly what we work through in my <a href="/en/courses/">one-on-one makeup courses</a>: with your own products and your skin type in mind.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Get the look for a shoot or an event',
    cta_text='I create natural looks that last through a shoot or a whole day for clients too: engagement shoots, portraits or a civil ceremony.',
    cta_links=[('Nude makeup', '/en/nude-makeup/'), ('Makeup courses', '/en/courses/')],
    faq=[('What is no-makeup makeup?', 'A light look that evens out the skin, corrects only what shows and enhances your features so the makeup isn\'t noticeable. Instead of full coverage it relies on light fluids, cream products and powder only in selected areas.'),
         ('How do I choose a foundation shade if I have freckles?', 'Match it to the hollow above your breastbone, not to your neck, which is usually lighter. Freckled skin with a cool undertone needs a slightly warmer shade, otherwise it looks grey, but not so warm that the face turns orange.'),
         ('How do I control shine in summer without looking flat?', 'Put a blurring silicone primer only on the T-zone, around the nose and in the hollows where shadows form, and press powder into the same areas. Leave the rest of the skin satin.'),
         ('Which setting spray is best for summer?', 'For setting, Charlotte Tilbury Airbrush Flawless worked best for me; for hydration, Caudalie Beauty Elixir. In my test the e.l.f. and Sephora mini sprays didn\'t set at all.'),
         ('Can I reapply SPF over makeup during the day?', 'I don\'t layer cream SPF over makeup; on dusty skin I don\'t think it\'s a good idea. That\'s why this routine is so light: you can wash it off, reapply SPF and redo it in a few minutes.'),
         ('Can I learn this look?', 'Yes. In a <a href="/en/courses/">one-on-one makeup course</a> in Prague we go through it step by step on your skin and with your products. If you want the look for a shoot or ceremony, see <a href="/en/nude-makeup/">nude makeup</a>.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

MENTIONS = ['Medicube', 'Chanel', 'Hourglass', 'Dior', 'e.l.f. Cosmetics', 'Charlotte Tilbury', 'Make Up For Ever', 'NYX Professional Makeup',
            'Lancôme', 'Yves Rocher', 'Fenty Beauty', 'Caudalie', 'Sephora']


def words(s):
    return len(re.sub(r'<[^>]+>', ' ', s).split())


def article(lang):
    meta, c, t = POSTS['summer'][lang], SUMMER[lang], L_BLOG[lang]
    other = POSTS['summer']['en' if lang == 'cs' else 'cs']
    path, vid = meta['path'], POSTS['summer']['video']
    body = c['opener'] + c['intro'] + c['tested'] + ''.join(s[2] for s in c['sections'])
    mins = max(1, round(words(body) / 200))
    blog_name = t['blog']
    crumbs_items = [t['home'], (blog_name, t['blog_path']), (meta['crumb'], None)]
    url = SITE + path
    og = f'{SITE}/assets/og/{og_slug(path)}.jpg'
    graph = [
        {'@type': 'BlogPosting', '@id': url + '#article', 'headline': meta['title'], 'description': meta['desc'], 'inLanguage': lang,
         'url': url, 'mainEntityOfPage': url, 'image': og, 'datePublished': PUBLISHED, 'dateModified': PUBLISHED,
         'wordCount': words(body), 'author': {'@id': SITE + '/#person'}, 'publisher': {'@id': SITE + '/#business'},
         'isPartOf': {'@type': 'Blog', '@id': SITE + t['blog_path'] + '#blog', 'name': f'Nikol Pavlova – {blog_name}', 'url': SITE + t['blog_path']},
         'about': {'@type': 'Thing', 'name': 'No-makeup makeup' if lang == 'en' else 'Make-up bez make-upu'},
         'mentions': [{'@type': 'Brand', 'name': b} for b in MENTIONS],
         'subjectOf': {'@type': 'CreativeWork', 'url': f'https://www.youtube.com/watch?v={vid}', 'name': 'Summer makeup 2.0 (YouTube)'}},
        {'@type': 'Person', '@id': SITE + '/#person', 'name': 'Nikol Pavlova', 'jobTitle': 'Makeup artist' if lang == 'en' else 'Vizážistka',
         'url': SITE + ('/en/' if lang == 'en' else '/'), 'sameAs': [IG, FB, TH, 'https://www.youtube.com/@nikolpavlova_mua']},
        S.breadcrumb(path, [(t['home'][0], t['home'][1]), (blog_name, t['blog_path']), (meta['crumb'], path)]),
        S.faq(path, lang, c['faq']),
    ]
    sch = [{'@context': 'https://schema.org', '@graph': graph}]
    alt = [('cs', POSTS['summer']['cs']['path']), ('en', POSTS['summer']['en']['path']), ('x-default', POSTS['summer']['cs']['path'])]
    h = head(lang, meta['seo_title'], meta['desc'], path, alt, og, sch, preload('nude-3', '(max-width: 900px) 100vw, 50vw'), og_type='article',
             extra=f'<meta property="article:published_time" content="{PUBLISHED}">')
    h += header(lang, 'blog', other['path'])
    toc = ''.join(f'<a href="#{i}">{n}</a>' for i, n in c['toc'])
    steps = ''.join(f'<li>{s}</li>' for s in c['steps'])
    secs = ''.join(f'<h2 id="{i}">{title}</h2>\n{html}\n' for i, title, html in c['sections'])
    verdict = ''.join(f'<div><p class="{cls}">{lab}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for lab, cls, items in c['verdict'])
    lessons = ''.join(f'<li><span class="n" aria-hidden="true">{k + 1}</span><div><p><strong>{a_}</strong></p><p class="fs-16">{b_}</p></div></li>' for k, (a_, b_) in enumerate(c['lessons']))
    faq_html = ''.join(f'<details{" open" if k == 0 else ""}><summary><h3>{q}</h3><span class="pm" aria-hidden="true">+</span></summary><div><p>{a_}</p></div></details>' for k, (q, a_) in enumerate(c['faq']))
    links = ''.join(f'<a class="btn btn--ghost c-white" href="{u}">{n}</a>' for n, u in c['cta_links'])
    sum_h = 'Postup v kostce' if lang == 'cs' else 'The routine in short'
    tested_h = 'Pro koho a jak jsem to testovala' if lang == 'cs' else 'Who it is for and how I tested it'
    verdict_h = 'Verdikt: co se vyplatí' if lang == 'cs' else 'The verdict: what is worth buying'
    lessons_h = 'Tři věci, které si z toho vzít' if lang == 'cs' else 'Three things to take away'
    faq_h = 'Časté dotazy' if lang == 'cs' else 'Frequently asked questions'
    learn = 'Chcete se to naučit?' if lang == 'cs' else 'Want to learn this properly?'
    alt_hero = 'Přirozený letní make-up bez make-upu – Nikol Pavlova' if lang == 'cs' else 'Natural summer no-makeup makeup look by Nikol Pavlova'
    h += f'''<article aria-labelledby="page-h1">
<header class="page-head post-head pb-48"><div class="wrap stack-28">
{crumbs(lang, crumbs_items)}
<p class="lbl muted meta-row"><span class="red">{meta['tag']}</span><time datetime="{PUBLISHED}">{fmt_date(lang, PUBLISHED)}</time><span>{mins} {t['read']}</span></p>
<h1 class="wide big mw-1180" id="page-h1">{meta['title']}</h1>
<div class="byline-bar">
<p class="byline">{I('nikol-portrait', '', sizes='52px', cls='avatar')}<span class="body">{t['by']} <a rel="author" href="{t['home'][1]}#about"><b>Nikol Pavlova</b></a> <span class="serif fs-18">– {t['role']}</span></span></p>
<a class="link-arrow" href="#{c['toc'][-2][0]}">{t['jump']}</a></div>
</div></header>
<a class="video-split" href="https://www.youtube.com/watch?v={vid}">{I('nude-3', alt_hero, sizes='(max-width: 900px) 100vw, 50vw', priority=True)}<span class="vs-panel"><span class="play glass" aria-hidden="true"><svg width="34" height="34" viewBox="0 0 24 24" fill="#A8232F"><path d="M8 5l12 7-12 7z"/></svg></span><span class="lbl">{t['watch']}</span><span class="serif vs-title">Summer makeup 2.0</span></span></a>
<div class="sec"><div class="wrap post-layout">
<aside class="post-toc"><p class="lbl red">{t['toc']}</p><nav class="toc bt-ink" aria-label="{t['toc']}">{toc}</nav></aside>
<div class="art">
<p class="opener">{c['opener']}</p>
<h2 id="{c['toc'][0][0]}">{sum_h}</h2>
<ol class="steps-list">{steps}</ol>
<aside class="note"><p class="lbl red">{tested_h}</p><p>{c['intro']}</p><p>{c['tested']}</p></aside>
{secs}
<figure class="art-pair">{I('nude-1', alt_hero, sizes='(max-width: 900px) 50vw, 380px')}{I('nude-2', alt_hero, sizes='(max-width: 900px) 50vw, 380px')}</figure>
<h2 id="{c['toc'][-2][0]}">{verdict_h}</h2>
<div class="verdict">{verdict}</div>
<h2>{lessons_h}</h2>
<ol class="lessons">{lessons}</ol>
<aside class="note note--row"><div class="mw-480"><p class="wide note-title">{learn}</p><p>{c['cta_note']}</p></div><a class="btn" href="{c['cta_btn'][1]}">{c['cta_btn'][0]}</a></aside>
<section class="cta-box" aria-labelledby="cta-h">
<h2 id="cta-h" class="cta-box__title">{c['cta_title']}</h2>
<p class="serif lead-on-ox">{c['cta_text']}</p>
<p class="actions-sm"><a class="btn btn--pink c-ox" href="{CAL}">{'Rezervace online +' if lang == 'cs' else 'Book online +'}</a>{links}</p>
</section>
<h2 id="{c['toc'][-1][0]}">{faq_h}</h2>
<div class="faq bt-0">{faq_html}</div>
<div class="author">{I('nikol-portrait', 'Nikol Pavlova', sizes='112px')}<div class="author-body"><p class="wide author-name">Nikol Pavlova</p><p class="serif muted2 fs-18">{'Vizážistka · Praha' if lang == 'cs' else 'Makeup Artist · Prague'}</p><p class="small-copy">{c['bio']}</p><p class="actions-sm"><a class="lbl" href="{IG}">Instagram</a><a class="lbl" href="https://www.youtube.com/@nikolpavlova_mua">YouTube</a></p></div></div>
</div></div></div>
</article>
'''
    h += footer(lang, 'Kontaktujte mě' if lang == 'cs' else 'Contact me',
                'Potřebujete pomoc s líčením?' if lang == 'cs' else 'Do you need help with creative make-up?',
                'Profesionální vizážistka v Praze. Líčení, které zvýrazní vaši přirozenou krásu.' if lang == 'cs' else 'Professional makeup artist based in Prague. Designing bespoke beauty looks that reflect your distinct personality.')
    write(path, h)


# ---------------------------------------------------------------- blog index
def index(lang):
    t = L_BLOG[lang]
    path = t['blog_path']
    p = POSTS['summer'][lang]
    if lang == 'cs':
        title = 'Blog – tutoriály, recenze a tipy vizážistky | Nikol Pavlova, Praha'
        desc = 'Tutoriály, poctivé recenze kosmetiky a profesionální tipy od vizážistky Nikol Pavlové z Prahy.'
        h1, sub = 'Blog', '– tutoriály, recenze a tipy vizážistky z Prahy'
        lead = 'Postupy, které používám na klientkách i na sobě, a poctivé recenze produktů. Psáno tak, abyste si vybrali lepší kosmetiku a vytvořili look, který vám sedí.'
        latest, more, topics_h, topics_sub = 'Nejnovější článek', 'Další články', 'Témata', 'o čem píšu'
        nyx_lang = ' <span class="muted2">(anglicky)</span>'
        topics = [('Tutoriály', 'Krok za krokem: přirozený, letní i večerní make-up.', '1 článek', True),
                  ('Recenze produktů', 'Testuji kosmetiku na sobě i v práci a říkám, co se vyplatí.', '1 článek (EN)', True),
                  ('Svatby a akce', 'Jak se připravit na make-up, který vydrží celý den.', 'Připravujeme', False)]
        read_btn = 'Číst článek →'
        alt = [('cs', path), ('en', '/en/blog/'), ('x-default', path)]
    else:
        title = 'Blog – Makeup Tutorials, Reviews & Tips | Nikol Pavlova, Prague'
        desc = 'Makeup tutorials, honest product reviews and professional tips from Nikol Pavlova, an English-speaking makeup artist based in Prague.'
        h1, sub = 'The Blog', '– makeup tutorials, reviews &amp; tips from Prague'
        lead = 'Routines I use on clients and on myself, plus honest product reviews, written to help you choose better products and create looks that suit you.'
        latest, more, topics_h, topics_sub = 'Latest article', 'More articles', 'Topics', 'what I write about'
        nyx_lang = ''
        topics = [('Tutorials', 'Step by step: natural, summer and evening makeup.', '1 article', True),
                  ('Product reviews', 'I test products on myself and at work and tell you what is worth it.', '1 article', True),
                  ('Bridal &amp; events', 'How to prepare for makeup that lasts all day.', 'Coming soon', False)]
        read_btn = 'Read the article →'
        alt = [('cs', '/blog/'), ('en', path), ('x-default', '/blog/')]
    graph = [{'@type': 'Blog', '@id': SITE + path + '#blog', 'name': f'Nikol Pavlova – {t["blog"]}', 'url': SITE + path, 'inLanguage': lang,
              'author': {'@id': SITE + '/#person'}, 'publisher': {'@id': SITE + '/#business'},
              'blogPost': [{'@id': SITE + p['path'] + '#article'}] + ([{'@type': 'Article', 'url': SITE + NYX['path'], 'headline': NYX['title']}] if True else [])},
             S.breadcrumb(path, [(t['home'][0], t['home'][1]), (t['blog'], path)])]
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
<article><a class="feat" href="{p['path']}">{I('nude-3', p['title'], sizes='(max-width: 900px) 100vw, 1280px', cls='fp-30', priority=True)}<span class="badge lbl glass">{latest}</span>
<div class="card glass"><p class="lbl muted meta-row-sm"><span class="red">{p['tag']}</span><time datetime="{PUBLISHED}">{fmt_date(lang, PUBLISHED)}</time></p>
<h3 class="wide feat-title">{p['title']}</h3>
<p class="c-text">{p['card']}</p>
<span class="btn self-start">{read_btn}</span></div></a></article>
</div></section>
<section class="sec--tight" aria-labelledby="more-h"><div class="wrap">
{sec_head(more, '', hid='more-h')}
<ul class="cards3" role="list">
<li><article><a class="pcard" href="{NYX['path']}"{' hreflang="en"' if lang == 'cs' else ''}><div class="ph">{I('nikol-hero', NYX['title'], sizes='(max-width: 900px) 100vw, 33vw')}<span class="tag lbl glass">{'Recenze' if lang == 'cs' else 'Review'}</span></div><div class="row"><h3>{NYX['title']}{nyx_lang}</h3></div><p class="body"><time datetime="{NYX['date']}">{fmt_date(lang, NYX['date'])}</time> · {NYX['card']}</p></a></article></li>
</ul></div></section>
<section class="sec sec--blush" aria-labelledby="topics-h"><div class="wrap">
{sec_head(topics_h, topics_sub, hid='topics-h')}
<ul class="topic-rows">{topic_html}</ul></div></section>
'''
    h += footer(lang, 'Kontaktujte mě' if lang == 'cs' else 'Contact me',
                'Potřebujete pomoc s líčením?' if lang == 'cs' else 'Do you need help with creative make-up?',
                'Profesionální vizážistka v Praze.' if lang == 'cs' else 'Professional makeup artist based in Prague.')
    write(path, h)


def build():
    index('cs'); index('en'); article('cs'); article('en')
