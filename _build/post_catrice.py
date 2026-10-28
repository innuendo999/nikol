"""Article: full face of Catrice (video lJGqeU8JfXA). Products from the Catrice Twinkling Treasures advent calendar 2025
plus the HD Liquid Coverage foundation and Melted Sun bronzer.

Product photos (Catrice packshots, cut from the official calendar flat lay): drop files into img/products/catrice/<slug>.jpg|png|webp, run python3 _build/images.py, then build."""

# slug, product name, verdict class, verdict label cs / en
PRODUCTS = [
    ('hd-liquid-coverage', 'Catrice HD Liquid Coverage Foundation', 'v-dep', 'Záleží na pleti · 6/10', 'Depends on skin · 6/10'),
    ('melted-sun-020', 'Catrice Melted Sun Cream Bronzer 020 Beach Babe', 'v-yes', 'Doporučuji', 'Recommended'),
    ('blush-baked-apple-pink', 'Catrice Blush C01 Baked Apple Pink', 'v-yes', 'Top produkt', 'Top pick'),
    ('highlighter-holly-jolly', 'Catrice Highlighter C01 Holly Jolly Shine', 'v-yes', 'Doporučuji', 'Recommended'),
    ('jelly-topper', 'Catrice Jelly Eyeshadow Topper C01 Twinkling Crystal', 'v-yes', 'Top produkt', 'Top pick'),
    ('peptide-lip-tint', 'Catrice Peptide Lip Tint C01 Merry Night Shine', 'v-yes', 'Doporučuji', 'Recommended'),
    ('lipliner-snowy-rose', 'Catrice Lipliner C01 Snowy Rose', 'v-yes', 'Doporučuji', 'Recommended'),
    ('glow-stick', 'Catrice Highlighter Glow Stick C01 Glow Ho Ho', 'v-yes', 'Dobrý', 'Good'),
    ('juicy-lip-balm-champagne', 'Catrice Juicy Lip Balm C01 Champagne Fizz', 'v-yes', 'Dobrý za ty peníze', 'Good value'),
    ('mascara-glam-doll', 'Catrice Glam & Doll Volume Mini Mascara C01 Holly Glam', 'v-dep', '7/10', '7/10'),
    ('eyeshadow-brush', 'Catrice Eyeshadow Brush C01 Midnight Glamour', 'v-dep', 'Ucházející', 'Decent'),
    ('lipgloss-stick', 'Catrice Lipgloss Stick C01 Merry Me?', 'v-dep', 'Ucházející', 'Decent'),
    ('blush-stick-candy-cane', 'Catrice Blush Stick C01 Candy Cane', 'v-sw', 'Sporné', 'Questionable'),
    ('liquid-eyeshadow', 'Catrice Liquid Eyeshadow C01 Golden Treasure', 'v-sw', 'Ne pro mě', 'Not for me'),
    ('lipliner-winterberry', 'Catrice Lipliner C02 Winterberry', 'v-sw', 'Ne můj odstín', 'Not my shade'),
    ('juicy-lip-balm-burgundy', 'Catrice Juicy Lip Balm C02 Burgundy Bliss', 'v-sw', 'Ne můj odstín', 'Not my shade'),
    ('eyepencil-ruby-noel', 'Catrice Eyepencil C01 Ruby Noel', 'v-sw', '1/10', '1/10'),
    ('eyepencil-golden-eve', 'Catrice Eyepencil C02 Golden Eve', 'v-sw', 'Nedoporučuji', 'Skip'),
]

BRANDS = ['Catrice', 'Estée Lauder', 'Rare Beauty']

C = {}
C['cs'] = dict(
    toc=[('verdikt', 'Verdikt v kostce'), ('produkty', 'Produkty v testu'), ('rty-priprava', 'Příprava rtů'), ('make-up', 'Make-up HD Liquid Coverage'),
         ('bronzer', 'Bronzer Melted Sun'), ('tvarenka-stick', 'Krémová tvářenka'), ('oci', 'Oči'), ('tvare', 'Pečená tvářenka a rozjasňovače'),
         ('rty', 'Rty'), ('zaver', 'Celkový dojem'), ('lekce', 'Tipy vizážistky'), ('faq', 'Časté dotazy')],
    opener='Začínám novou tradici: celý obličej od jedné značky. Jako první přichází Catrice. Ze zimního adventního kalendáře se mi nasbíralo hodně produktů, tak jsem je otestovala na celém obličeji, zblízka, aby byly vidět póry a jak produkty na pleti opravdu vypadají. Některé vám budu určitě doporučovat, jiné rozhodně ne.',
    pre='''<p>Většina produktů pochází z adventního kalendáře <b>Catrice Twinkling Treasures</b>, k nim jsem přidala make-up HD Liquid Coverage a bronzer Melted Sun, které znám dlouho. Obočí v tomhle díle neřeším, produkty na obočí jsem testovala v minulém videu.</p>
<aside class="note"><p class="lbl red">Jak jsem testovala</p><p>Všechno nanáším tak, jak by to dělala většina lidí doma, a u některých produktů porovnávám dvě metody na každé polovině obličeje. Na konci každý produkt upřímně hodnotím.</p></aside>''',
    verdict_h='Verdikt v kostce',
    verdict=[('Doporučuji', 'vtag v-yes', ['Pečená tvářenka Baked Apple Pink', 'Topper Twinkling Crystal', 'Bronzer Melted Sun 020', 'Rozjasňovač Holly Jolly Shine', 'Peptide Lip Tint', 'Tužka na rty Snowy Rose']),
             ('Záleží na pleti', 'vtag v-dep', ['Make-up HD Liquid Coverage (6/10)', 'Řasenka Glam & Doll (7/10)', 'Rozjasňovač Glow Ho Ho', 'Balzám Champagne Fizz']),
             ('Nedoporučuji', 'vtag v-sw', ['Tvářenka v tyčince Candy Cane', 'Tekuté stíny Golden Treasure', 'Tužky na oči Ruby Noel a Golden Eve'])],
    verdict_foot='Hodnocení je podle mé pleti a mého stylu; u make-upu hraje velkou roli i reakce pleti.',
    grid_h='Produkty v testu',
    sections=[
        ('rty-priprava', 'Příprava rtů: Juicy Lip Balm Champagne Fizz', '''<p class="vtag v-yes">Dobrý za ty peníze</p>
<p>Péče o pleť je dnes minimální, začínám jen hydratací rtů. Balzám mě zaujal už při rozbalování kalendáře. Je vazelínový, dodá jemný broskvový odstín, krásně se leskne a nelepí. Rty se mi pořád zdají trochu suché, ale pokud máte rádi lesky, které se lesknou a nelepí, je to skvělá levná volba.</p>'''),
        ('make-up', 'Make-up: HD Liquid Coverage', '''<p class="vtag v-dep">Záleží na pleti · 6/10</p>
<p>Asi první levný make-up, který jsem si koupila jako vizážistka, protože ho všichni doporučovali. Napoprvé jsem ho nepochopila, minulý rok jsem zjistila, že je to opravdu dobrý make-up. Kryje hodně, dá se nanést tence i hustě a pro natáčení videí ho mám ráda.</p>
<p>Má ale dvě nevýhody. Pokaždé mi způsobí vyrážky; ve složení je niacinamid a ten v jeho formě mou pleť dráždí a může vysušovat, takže make-up pak může zapadat do pórů a působit „cakey“. A výrazně oxiduje, jako většina matných make-upů. Hydratační make-upy to dělají méně často.</p>
<p>Plus je, že díky vysoké pigmentaci a fixaci zvládne roli korektoru. Pod oči ho nanáším plochým, oboustranně zkoseným štětcem <b>Eyeshadow Brush Midnight Glamour</b> z kalendáře: je trochu tvrdší, ale na levný štětec je hustý a nadějný. Modřinu pod okem úplně nezakrývám, nemám ráda silně zamazané oči. Hodně lidí ho staví na úroveň Estée Lauder Double Wear; dá se vrstvit, ale časem u mě začne vypadat cakey.</p>'''),
        ('bronzer', 'Bronzer: Melted Sun 020 Beach Babe', '''<p class="vtag v-yes">Doporučuji</p>
<p>Oblíbený, všemi známý krémový bronzer. Nepoužívám ho poprvé a mám ho pro sebe i do práce. Je neutrální, ne moc rezavý, a jeho trumfem je odstín za tuhle cenu. Je velmi plastický a nezatuhne hned, takže s ním zvládnou pracovat i začátečníci.</p>
<p>Platí takové pravidlo: na matný make-up se krémové produkty s voskem nanášejí obtížně, vosk může matný podklad „rozleptat“ a vzniknou skvrny. Tenhle bronzer má vosk na prvním místě složení, a přesto je mega uživatelsky přívětivý. Můžete ho nanést hustě a přebytek stáhnout houbičkou, nebo nechat výraznou konturu.</p>'''),
        ('tvarenka-stick', 'Krémová tvářenka: Blush Stick Candy Cane', '''<p class="vtag v-sw">Sporné</p>
<p>Krásný odstín čajové růže a produktu je hodně. Na jednu polovinu obličeje jsem ji nanesla přímo z tyčinky, jak to dělá většina lidí doma: roztírala se špatně, asi protože se nestihla zahřát, a šla do skvrn. Na druhou stranu jsem ji zahřála na ruce a nanesla štětcem, to jde lépe a nemusíte tlačit.</p>
<p>S bronzerem se ale pohádala a vznikl „špinavý“ obraz, i když jsou od stejné značky. Opravila jsem to make-upem na štětci. Tam bylo vidět, jak moc HD Liquid Coverage oxiduje: čerstvě nanesený byl výrazně světlejší.</p>'''),
        ('oci', 'Oči: krémové stíny, topper, tužky a řasenka', '''<h3>Liquid Eyeshadow Golden Treasure</h3><p class="vtag v-sw">Ne pro mě</p>
<p>Teplé zlaté krémové stíny. V kalendáři byly jen krémové. Chytily se okamžitě, při nanášení jsem cítila lehký chlad (možná se odpařoval alkohol) a lepí se na víčku. Nejspíš vydrží dlouho, ale krémové stíny nejsou můj produkt.</p>
<h3>Jelly Eyeshadow Topper Twinkling Crystal</h3><p class="vtag v-yes">Top produkt</p>
<p>Fantastický třpytivý topper. Na teple zlatých stínech dělá chladný lesk a vznikne moc hezký efekt. Toppery nanáším prstem, vrství se tak zajímavěji než štětcem.</p>
<h3>Eyepencil Ruby Noel a Golden Eve</h3><p class="vtag v-sw">Nedoporučuji · 1/10</p>
<p>Vínová tužka má krásný odstín, ale je suchá, po krémových stínech kreslí špatně a kus se ulomil. Linka z ní vyšla jen hodně „podmíněná“, tak jsem ji rozmazala do kouřové. Světle zlatá tužka do vnitřního koutku se taky ulomila a na sliznici nedrží. Za barvu dávám jedničku z deseti a to je vše.</p>
<aside class="note"><p class="lbl red">Trik s pudřenkou</p><p class="serif fs-20">Když kreslíte linky, položte pod ruku pudřenku nebo obláček a opřete se o něj. Nesetřete si make-up a ruka je stabilní. Linku kreslete s otevřenýma očima: nejdřív linie, z ní pak ocásek.</p></aside>
<h3>Glam & Doll Volume Mini Mascara</h3><p class="vtag v-dep">7/10</p>
<p>Nanáší se snadno a hezky. Slibuje objem, mně spíš prodloužila. Řasy mám normální, takže na mně vypadá dobře skoro každá řasenka; výdrž je potřeba vyzkoušet během dne. Dávám sedmičku.</p>'''),
        ('tvare', 'Pečená tvářenka a rozjasňovače', '''<h3>Blush Baked Apple Pink</h3><p class="vtag v-yes">Top produkt</p>
<p>Krabička jako dóm i se zrcátkem, vypadá draze. A výsledek: krásná růžová, kterou jsem dlouho hledala, a jemně se třpytí. Velmi nadýchaným štětcem dá jemný nádech, hustším, třeba syntetickým, bude pigmentovanější. Trochu jsem ji dala i na oči pro hloubku. Je pečená, takže se dá nanést velmi tence, a když jsem ji vozila s sebou, nerozbila se. Podobné produkty od Rare Beauty ve stejném typu balení se podle mé zkušenosti rozbíjejí strašně snadno.</p>
<h3>Highlighter Holly Jolly Shine</h3><p class="vtag v-yes">Doporučuji</p>
<p>Zlatý rozjasňovač. Tvářenka už sama třpytí, takže ho není potřeba hodně. Rozjasňovače Catrice znám a mám je ráda: levné produkty, krásná záře, a v tvrdém světle bude odlesk ještě hezčí.</p>
<h3>Highlighter Glow Stick Glow Ho Ho</h3><p class="vtag v-yes">Dobrý</p>
<p>Voskový rozjasňovač v tyčince, odstínem o něco chladnější a ten se mi líbí víc. Přímo na obličej ho nedávám, protože by stoprocentně začal stahovat suché produkty. Naberu ho na prsty, zahřeje se a lépe pracuje, a pak ho můžete dát i přes pudrové produkty bez skvrn. Má 5,5 g, takže vydrží dlouho.</p>'''),
        ('rty', 'Rty: tužky, rtěnky a tint', '''<h3>Lipliner Snowy Rose a Lipgloss Stick Merry Me?</h3><p class="vtag v-yes">Tužka doporučuji</p>
<p>Béžová teplá tužka má odstín přesně jako na obalu, je měkká, vysouvací, stálá a kreslí se s ní velmi pohodlně. Lesklá rtěnka nemá žádnou chuť, jen vosk a glycerin, a vypadá hezky.</p>
<h3>Lipliner Winterberry a Juicy Lip Balm Burgundy Bliss</h3><p class="vtag v-sw">Ne můj odstín</p>
<p>Červeno-růžová kombinace. Tužka působí stále, možná trochu vysušuje, ale to je jen můj dojem a je potřeba ji nosit déle. Balzám má příchuť a voní, to mám ráda. Jen takhle výrazné, agresivní barvy na sobě nenosím a skoro na nikom je nemám ráda.</p>
<h3>Peptide Lip Tint Merry Night Shine</h3><p class="vtag v-yes">Doporučuji</p>
<p>Lip tinty mám obecně ráda a tenhle je moc pěkný: nelepí, není hořký a má krásný lesk, k jemnému make-upu sedí. Nejvíc se mi líbila kombinace béžové tužky Snowy Rose na celé rty a tohoto tintu navrch.</p>'''),
        ('zaver', 'Celkový dojem', '''<p>Čekala jsem víc. Na první pohled mi produkty slibovaly hodně zajímavý make-up, ale výsledek byl podle mě průměrný, bez efektu „wow“. Tohle video je jedno z mála na mém kanálu, kde mě produkty nijak zvlášť nenadchly, a proto je i kratší než obvykle.</p>
<p>Přesto Catrice obecně doporučuji. Je to dobrá kosmetika pro všechny, kdo si teprve skládají kosmetickou taštičku nebo chtějí zkusit něco nového. S některými produkty se ale musíte naučit pracovat. Pro srovnání se podívejte na moji <a href="/blog/recenze-nyx-cely-oblicej/">recenzi celého obličeje NYX</a>.</p>'''),
    ],
    lessons_h='Tipy vizážistky z tohoto testu',
    lessons=[('Krémové produkty zahřejte v prstech.', 'Voskové tvářenky a rozjasňovače přímo z tyčinky na matném make-upu snadno udělají skvrny. Zahřáté na prstech nebo nanesené štětcem se prolnou čistě.'),
             ('Matné make-upy oxidují.', 'Odstín vybírejte s ohledem na to, že po pár minutách ztmavne. U <a href="/svatebni-liceni/">svatebního líčení</a> to testujeme na zkoušce.'),
             ('Pečené produkty jsou ideální na cesty.', 'Pečená tvářenka a rozjasňovač se dají nanést velmi tence a v kufru se nerozbijí.')],
    learn_h='Začínáte s líčením?',
    cta_note='Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> projdeme vaši kosmetiku, vysvětlím, které produkty spolu fungují, a naučíte se triky jako ten s pudřenkou.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Třpyt na večer nebo ples?',
    cta_text='Toppery, rozjasňovače a výrazné rty používám i na klientkách. Večerní make-up, který vydrží celou noc, vám ráda udělám.',
    cta_links=[('Večerní líčení', '/vecerni-liceni/'), ('Svatební líčení', '/svatebni-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Je make-up Catrice HD Liquid Coverage dobrý?', 'Hodně kryje, dá se nanést tence i hustě a zvládne i roli korektoru. Výrazně ale oxiduje a mně kvůli niacinamidu ve složení způsobuje vyrážky. Celkově mu dávám 6 z 10.'),
         ('Je Catrice HD Liquid Coverage dupe Estée Lauder Double Wear?', 'Hodně lidí ho staví na stejnou úroveň. Dá se vrstvit, ale u mě časem začne vypadat cakey, takže je to sporná otázka.'),
         ('Které produkty Catrice z testu se vyplatí?', 'Pečená tvářenka Baked Apple Pink, topper Jelly Eyeshadow Topper, krémový bronzer Melted Sun 020, rozjasňovač Holly Jolly Shine, Peptide Lip Tint a tužka na rty Snowy Rose.'),
         ('Jak nanést krémovou tvářenku na matný make-up bez skvrn?', 'Produkt zahřejte na hřbetu ruky nebo v prstech a naneste štětcem bez tlaku. Přímo z tyčinky na matném podkladu snadno vzniknou skvrny.'),
         ('Hodí se Catrice pro začátečníky?', 'Ano. Bronzer Melted Sun je velmi plastický a odpouští chyby a celá značka je dobrá na sestavení první kosmetické taštičky. S některými produkty se ale musíte naučit pracovat, a to procházíme i na <a href="/kurzy-liceni/">kurzu líčení</a>.'),
         ('Jak nakreslit linky, aniž bych si setřela make-up?', 'Pod ruku si položte pudřenku nebo obláček a opřete se o něj. Linku kreslete s otevřenýma očima: nejdřív linii, z ní pak ocásek.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

C['en'] = dict(
    toc=[('verdict', 'The verdict at a glance'), ('products', 'Products tested'), ('lip-prep', 'Lip prep'), ('foundation', 'HD Liquid Coverage foundation'),
         ('bronzer', 'Melted Sun bronzer'), ('blush-stick', 'Cream blush stick'), ('eyes', 'Eyes'), ('cheeks', 'Baked blush and highlighters'),
         ('lips', 'Lips'), ('overall', 'Overall impression'), ('lessons', 'Pro tips'), ('faq', 'FAQ')],
    opener="I'm starting a new tradition: a full face from one brand. First up is Catrice. I'd collected a lot of products from its winter advent calendar, so I tested them on my whole face, up close, so you can see the pores and how the products really look on skin. Some I'll definitely recommend, others I definitely won't.",
    pre='''<p>Most of the products come from the <b>Catrice Twinkling Treasures</b> advent calendar, and I added the HD Liquid Coverage foundation and the Melted Sun bronzer, which I've known for a long time. I skip brows in this episode; I tested brow products in the previous video.</p>
<aside class="note"><p class="lbl red">How I tested</p><p>I apply everything the way most people would at home, and for some products I compare two methods, one on each side of the face. At the end I rate every product honestly.</p></aside>''',
    verdict_h='The verdict at a glance',
    verdict=[('Recommended', 'vtag v-yes', ['Baked Apple Pink baked blush', 'Twinkling Crystal topper', 'Melted Sun bronzer 020', 'Holly Jolly Shine highlighter', 'Peptide Lip Tint', 'Snowy Rose lip liner']),
             ('Depends on your skin', 'vtag v-dep', ['HD Liquid Coverage foundation (6/10)', 'Glam & Doll mascara (7/10)', 'Glow Ho Ho highlighter stick', 'Champagne Fizz lip balm']),
             ('Skip', 'vtag v-sw', ['Candy Cane blush stick', 'Golden Treasure liquid eyeshadow', 'Ruby Noel and Golden Eve eye pencils'])],
    verdict_foot='Ratings reflect my skin and my style; with foundation, how your skin reacts matters a lot.',
    grid_h='Products tested',
    sections=[
        ('lip-prep', 'Lip prep: Juicy Lip Balm Champagne Fizz', '''<p class="vtag v-yes">Good value</p>
<p>Skin prep is minimal today; I only start by hydrating my lips. This balm caught my eye when I unboxed the calendar. It's Vaseline-like, gives a soft peachy tint, shines beautifully and isn't sticky. My lips still feel a little dry, but if you love glosses that shine without sticking, it's a great budget option.</p>'''),
        ('foundation', 'Foundation: HD Liquid Coverage', '''<p class="vtag v-dep">Depends on skin · 6/10</p>
<p>Probably the first budget foundation I bought as a makeup artist, because everyone recommended it. I didn't get it at first; last year I realised it really is a good foundation. It's high coverage, can be applied thin or thick, and I like it for filming videos.</p>
<p>It has two downsides, though. It gives me breakouts every time: it contains niacinamide, and in this formula it irritates my skin and can be drying, so the foundation can sink into pores and look cakey. And it oxidises noticeably, like most matte foundations. Hydrating foundations do this less often.</p>
<p>On the plus side, its high pigment and grip mean it can double as concealer. I apply it under the eyes with the flat, double-angled <b>Eyeshadow Brush Midnight Glamour</b> from the calendar: a little stiff, but dense and decent for a cheap brush. I don't fully cover the bruise under my eye; I don't like heavily covered under-eyes. Many people put it on a par with Estée Lauder Double Wear; it layers, but over time it starts to look cakey on me.</p>'''),
        ('bronzer', 'Bronzer: Melted Sun 020 Beach Babe', '''<p class="vtag v-yes">Recommended</p>
<p>A well-known, much-loved cream bronzer. This isn't my first one and I use it for myself and at work. It's neutral, not too orange, and its trump card is the shade at this price. It's very blendable and doesn't grab straight away, so even beginners can work with it.</p>
<p>There's a rule of thumb: wax-based cream products are tricky over a matte foundation, because the wax can break down the matte base and leave patches. This bronzer has wax as its first ingredient and is still mega user-friendly. You can apply it heavily and take off the excess with a sponge, or keep a stronger contour.</p>'''),
        ('blush-stick', 'Cream blush: Blush Stick Candy Cane', '''<p class="vtag v-sw">Questionable</p>
<p>A lovely tea-rose shade, and there's a lot of product. On one side of my face I applied it straight from the stick, the way most people do at home: it didn't blend easily, probably because it hadn't warmed up, and went patchy. On the other side I warmed it on my hand and applied it with a brush, which works better and needs no pressure.</p>
<p>But it clashed with the bronzer and created a muddy look, even though they're from the same brand. I fixed it with foundation on a brush. That showed how much HD Liquid Coverage oxidises: freshly applied it was clearly lighter.</p>'''),
        ('eyes', 'Eyes: cream shadow, topper, pencils and mascara', '''<h3>Liquid Eyeshadow Golden Treasure</h3><p class="vtag v-sw">Not for me</p>
<p>A warm gold cream shadow; the calendar only had cream shadows. It set instantly, felt slightly cold on application (maybe alcohol evaporating) and feels sticky on the lid. It will probably last a long time, but cream eyeshadows aren't my thing.</p>
<h3>Jelly Eyeshadow Topper Twinkling Crystal</h3><p class="vtag v-yes">Top pick</p>
<p>A fantastic glitter topper. Over the warm gold shadow it gives a cool sparkle and the effect is really pretty. I apply toppers with a finger; they layer more interestingly than with a brush.</p>
<h3>Eyepencil Ruby Noel and Golden Eve</h3><p class="vtag v-sw">Skip · 1/10</p>
<p>The burgundy pencil has a beautiful shade, but it's dry, draws badly over cream shadow and a piece broke off. The liner came out very "approximate", so I smudged it into a smoky line. The light gold pencil for the inner corner broke too and doesn't stay on the waterline. One out of ten for the colour, and that's it.</p>
<aside class="note"><p class="lbl red">The powder puff trick</p><p class="serif fs-20">When you draw liner, rest your hand on a powder puff instead of your face. You won't wipe off your base and your hand stays steady. Draw with your eyes open: first the line, then flick the tail out from it.</p></aside>
<h3>Glam &amp; Doll Volume Mini Mascara</h3><p class="vtag v-dep">7/10</p>
<p>Applies easily and nicely. It promises volume; on me it lengthened more. My lashes are normal, so almost any mascara looks fine on me; wear time needs testing over a day. I give it a seven.</p>'''),
        ('cheeks', 'Baked blush and highlighters', '''<h3>Blush Baked Apple Pink</h3><p class="vtag v-yes">Top pick</p>
<p>A dome compact with a mirror that looks expensive. And the result: a beautiful pink I'd been looking for, with a subtle shimmer. With a very fluffy brush it gives a soft wash; with a denser, even synthetic brush it will be more pigmented. I also added a little to my eyes for depth. It's baked, so you can apply it very thinly, and when I travelled with it, it didn't break. In my experience similar products from Rare Beauty in the same type of packaging break terribly easily.</p>
<h3>Highlighter Holly Jolly Shine</h3><p class="vtag v-yes">Recommended</p>
<p>A gold highlighter. The blush already shimmers, so you don't need much. I know and love Catrice highlighters: budget products with a beautiful glow, and under harder light the highlight will be even prettier.</p>
<h3>Highlighter Glow Stick Glow Ho Ho</h3><p class="vtag v-yes">Good</p>
<p>A waxy highlighter stick, slightly cooler in tone, which I like more. I don't apply it straight to the face, because it would definitely start lifting the powder products. I take it on my fingers, it warms up and works better, and then you can even put it over powders without patches. It's 5.5 g, so it lasts a long time.</p>'''),
        ('lips', 'Lips: liners, lipsticks and tint', '''<h3>Lipliner Snowy Rose and Lipgloss Stick Merry Me?</h3><p class="vtag v-yes">Liner recommended</p>
<p>The warm beige liner is exactly the shade on the pack, soft, retractable, long-wearing and very comfortable to draw with. The glossy lipstick has no flavour, just wax and glycerin, and looks pretty.</p>
<h3>Lipliner Winterberry and Juicy Lip Balm Burgundy Bliss</h3><p class="vtag v-sw">Not my shade</p>
<p>A red-pink combo. The liner feels long-wearing, maybe a little drying, but that's just my impression and needs longer wear. The balm is flavoured and scented, which I like. I just don't wear such bold, aggressive colours, and I rarely like them on anyone.</p>
<h3>Peptide Lip Tint Merry Night Shine</h3><p class="vtag v-yes">Recommended</p>
<p>I generally like lip tints and this one is lovely: not sticky, not bitter, with a beautiful shine that suits soft makeup. My favourite combo was the beige Snowy Rose liner over the whole lip with this tint on top.</p>'''),
        ('overall', 'Overall impression', '''<p>I expected more. At first glance the products promised a really interesting look, but the result was average to me, with no wow effect. This is one of the few videos on my channel where the products didn't excite me much, which is also why it's shorter than usual.</p>
<p>Still, I generally recommend Catrice. It's good makeup for anyone building their first makeup bag or wanting to try something new. With some products you just have to learn how to work. For comparison, see my <a href="/en/blog/full-face-of-nyx-review/">full face of NYX review</a>.</p>'''),
    ],
    lessons_h='Pro tips from this test',
    lessons=[('Warm cream products in your fingers.', 'Waxy blushes and highlighters straight from the stick easily go patchy over matte foundation. Warmed on your fingers or applied with a brush, they melt in cleanly.'),
             ('Matte foundations oxidise.', 'Choose the shade knowing it will deepen after a few minutes. For <a href="/en/wedding/">bridal makeup</a> we check this at the trial.'),
             ('Baked products are perfect for travel.', 'A baked blush and highlighter apply very thinly and won\'t shatter in your bag.')],
    learn_h='New to makeup?',
    cta_note='In a <a href="/en/courses/">one-on-one makeup course</a> we go through your products, I explain which ones work together, and you learn tricks like the powder puff one.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Sparkle for a night out or a ball?',
    cta_text='I use toppers, highlighters and bold lips on clients too. I would love to do evening makeup for you that lasts all night.',
    cta_links=[('Evening makeup', '/en/evening-makeup/'), ('Wedding makeup', '/en/wedding/')],
    faq_h='Frequently asked questions',
    faq=[('Is Catrice HD Liquid Coverage foundation good?', 'It is high coverage, can be applied thin or thick and can double as concealer. But it oxidises noticeably, and for me the niacinamide in the formula causes breakouts. Overall I give it 6 out of 10.'),
         ('Is Catrice HD Liquid Coverage a dupe for Estée Lauder Double Wear?', 'Many people put it on the same level. It layers, but on me it starts to look cakey over time, so it is debatable.'),
         ('Which Catrice products from the test are worth buying?', 'The Baked Apple Pink baked blush, the Jelly Eyeshadow Topper, the Melted Sun 020 cream bronzer, the Holly Jolly Shine highlighter, the Peptide Lip Tint and the Snowy Rose lip liner.'),
         ('How do I apply cream blush over matte foundation without patches?', 'Warm the product on the back of your hand or in your fingers and apply it with a brush without pressing. Straight from the stick onto a matte base it easily goes patchy.'),
         ('Is Catrice good for beginners?', 'Yes. The Melted Sun bronzer is very blendable and forgiving, and the brand is great for building a first makeup bag. With some products you need to learn how to work, which we also cover in my <a href="/en/courses/">makeup course</a>.'),
         ('How do I draw eyeliner without smudging my base?', 'Rest your hand on a powder puff instead of your face. Draw with your eyes open: first the line, then flick the tail out from it.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

EXTRA = dict(products=[], grid=PRODUCTS,
             credit=('Produktové fotografie: Catrice.', 'Product photos: Catrice.'),
             figure=('prod-advent-calendar', 'Obsah adventního kalendáře Catrice Twinkling Treasures 2025. Foto: Catrice.',
                     'Contents of the Catrice Twinkling Treasures 2025 advent calendar. Photo: Catrice.'), brands=BRANDS, about=('Recenze Catrice', 'Catrice makeup review'), video_name='Все обличчя Catrice')
