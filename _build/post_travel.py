"""Article (how-to): travel makeup bag, a full look step by step (video Sb-Sg-GVoVM, filmed in Odesa).

Interactive parts (all readable without JS, see site.js / site.css .tg-*):
- guide: steps with a line-art face whose zones light up per step, plus a Minimum / Day / Evening switch
- packing checklist, dry-vs-damp sponge slider, mascara picker (generic data-finder), brush line-up."""
from post_brushes import DEFS as BRUSH_DEFS, INK, OX, RED, PINK, BLUSH, PAPER, LINE, _S, _T

BRANDS = ['Medi-Peel', 'Image Skincare', 'Round Lab', 'Dior', 'Charlotte Tilbury', 'Note Cosmetique', 'Estée Lauder', 'Eveline Cosmetics',
          'Yves Saint Laurent', 'Hourglass', 'Davydenko Beauty', 'Patricia Ledo', 'Physicians Formula', 'Benefit Cosmetics', 'Fenty Beauty',
          'Essence', 'Pupa', 'Sephora']

PRODUCTS = [
    ('Medi-Peel Hyal Kombucha Tea-Tox Toner', 'https://eva.ua/ua/pr699456/'),
    ('Image Skincare Vital C Hydrating Anti-Aging Serum', 'https://beautydevice.com.ua/kosmetyka-dlya-oblychchya/image-skincare/anti-aging-serum'),
    ('Round Lab Birch Juice Moisturizing Sun Cream SPF 50+', 'https://cosibella.com.ua/uk/products/round-lab-14512'),
    ('Dior Forever Glow Star Filter 2N', 'https://www.brocard.ua/ua/product/tonalna-osnova-dlya-oblichchya-dior-forever-glow-star-filter-30-ml-30-ml-2n-167744'),
    ('Charlotte Tilbury Airbrush Flawless Setting Spray', 'https://glowbeauty.com.ua/fiksuyuchij-ta-zvolozhuyuchij-sprej-dlya-oblichchya-charlotte-tilbury-airbrush-flawless-setting-spra-1'),
    ('Note Cosmetique BB Concealer Advanced Skin Corrector 03', 'https://maudau.com.ua/ru/product/vv-konsyler-note-cosmetique-bb-concealer-advanced-skin-corrector-vidtinok-03-10-ml'),
    ('Estée Lauder Double Wear Sheer SPF 20, 2N1', 'https://www.notino.ua/estee-lauder/multi-protection-anti-oxidant-sheer-tint-release-moisturizer-legkij-matujuchij-tonalnij-zasib-spf-20/p-16093631/'),
    ('Eveline Cosmetics Choco Glamour cream bronzer 02', 'https://www.notino.ua/eveline-cosmetics/choco-glamour-kremovij-bronzer/p-16221155/'),
    ('Dior Forever Glow Maximizer Nude', 'https://www.brocard.ua/ua/product/haylayter-dlya-oblichchya-dior-forever-glow-maximizer-11-ml-11-ml-017-nude-167442'),
    ('YSL Make Me Blush 44', 'https://www.brocard.ua/ru/product/rumyana-yves-saint-laurent-ysl-make-me-blush-15-ml-15-ml-44-177344'),
    ('Hourglass Ambient Lighting Edit Unlocked Leopard', 'https://princess-shop.com.ua/paletka-dlia-oblychchia-ambient-lighting-edit-unlocked-leopard/'),
    ('Eveline Variété Lashes Show Brown', 'https://skladchistoti.com.ua/index.php?route=product/product&product_id=105347'),
    ('Patricia Ledo Absolute Eyebrow 01', 'https://eva.ua/ua/pr635767/#/141705/'),
    ('Physicians Formula Butter Palm Feathered', 'https://www.notino.ua/physicians-formula/butter-palm-feathered-olivec-dlja-ochej/'),
    ('Benefit 24-Hour Brow Setter Clear', 'https://eva.ua/ua/pr141973/'),
    ('Davydenko Beauty lip pencil 05', 'https://prom.ua/p2616999622-davydenko-beauty-olivets.html'),
]

# ---------------------------------------------------------------- line-art face with zones
_Z = f'fill="{RED}" fill-opacity=".16" stroke="{RED}" stroke-width="1.2" stroke-dasharray="3 3" vector-effect="non-scaling-stroke"'
OVAL = 'M120 34C72 34 54 80 56 130c2 58 32 104 64 106 32-2 62-48 64-106 2-50-16-96-64-96z'
ZONES = {
    'face': f'<path d="{OVAL}"/>',
    'neck': '<path d="M96 226h48l4 60H92z"/>',
    'tzone': '<path d="M78 68h84v24h-30l-3 78h-18l-3-78H78z"/>',
    'under': '<path d="M80 129q14 22 30 0-15 11-30 0z"/><path d="M130 129q16 22 30 0-15 11-30 0z"/>',
    'contour': '<path d="M60 116q4 44 32 54-24-18-28-56z"/><path d="M180 116q-4 44-32 54 24-18 28-56z"/><path d="M66 66q-10 18-8 40l10-4q0-20 8-34z"/><path d="M174 66q10 18 8 40l-10-4q0-20-8-34z"/>',
    'cheeks': '<ellipse cx="86" cy="160" rx="15" ry="9"/><ellipse cx="154" cy="160" rx="15" ry="9"/>',
    'lids': '<path d="M78 121q16-24 32 0-16-9-32 0z"/><path d="M130 121q16-24 32 0-16-9-32 0z"/>',
    'outer': '<path d="M80 122q-10-10-18-20l6-3q8 10 16 18z"/><path d="M160 122q10-10 18-20l-6-3q-8 10-16 18z"/>',
    'lashes': '<path d="M79 121q15-14 30 0-15-6-30 0z"/><path d="M131 121q15-14 30 0-15-6-30 0z"/>',
    'brows': '<path d="M74 106q18-15 36-4v5q-18-9-34 2z"/><path d="M166 106q-18-15-36-4v5q18-9 34 2z"/>',
    'lips': '<path d="M100 192q10-8 20-3 10-5 20 3-6 16-20 16t-20-16z"/>',
}


def face():
    zones = ''.join(f'<g class="tg-z" data-z="{k}" {_Z}>{v}</g>' for k, v in ZONES.items())
    return f'''<svg class="tg-face" viewBox="0 0 240 300" aria-hidden="true">
<path d="M70 300q4-40 26-56M170 300q-4-40-26-56" fill="none" {_S}/>
<path d="M96 222v34M144 222v34" fill="none" {_S}/>
<path d="{OVAL}" fill="{PAPER}" {_S}/>
<path d="M56 128c-8-62 26-108 64-108 42 0 74 40 66 108-6-44-30-74-66-76-36 2-60 30-64 76z" fill="{OX}"/>
<path d="M76 104q16-9 32-2M132 102q16-7 32 2" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
<path d="M80 122q14-10 28 0-14 8-28 0zM132 122q14-10 28 0-14 8-28 0z" fill="#fff" {_S}/>
<circle cx="94" cy="122" r="3.6" fill="{INK}"/><circle cx="146" cy="122" r="3.6" fill="{INK}"/>
<path d="M120 132l-6 32q6 5 12 0" fill="none" {_S}/>
<path d="M100 192q10-8 20-3 10-5 20 3-6 16-20 16t-20-16z" fill="#E3A497" {_S}/><path d="M100 192q20 4 40 0" fill="none" {_S}/>
{zones}
</svg>'''


def guide(L, steps):
    """Steps list + sticky face. Each step: (zones, mode, title, products, body). Mode: base / opt / eve."""
    modes = ''.join(f'<button type="button" data-mode="{k}"{" aria-pressed=" + chr(34) + "true" + chr(34) if k == "day" else ""}>{n}</button>' for k, n in L['modes'])
    items = ''
    for i, (zones, mode, title, prods, body) in enumerate(steps):
        tag = {'opt': f'<span class="vtag v-dep">{L["opt"]}</span>', 'eve': f'<span class="vtag v-sw">{L["eve"]}</span>'}.get(mode, '')
        items += (f'<li class="tg-step" id="{L["anchor"]}-{i + 1:02d}" data-zones="{" ".join(zones)}" data-mode="{mode}">'
                  f'<button type="button" class="tg-step-h" aria-expanded="true"><span class="tg-num">{i + 1:02d}</span><span class="tg-title">{title}</span>{tag}</button>'
                  f'<div class="tg-step-b"><p class="tg-prod">{prods}</p>{body}</div></li>')
    return f'''<div class="tg-guide" data-guide>
<div class="tg-modes" role="group" aria-label="{L['modes_label']}" hidden>{modes}</div>
<div class="tg-grid">
<div class="tg-aside"><div class="tg-face-wrap">{face()}<p class="tg-cap lbl" aria-live="polite"></p></div>
<div class="tg-ctrl" hidden><button type="button" data-prev aria-label="{L['prev']}">←</button><span class="tg-count lbl"></span><button type="button" data-next aria-label="{L['next']}">→</button></div></div>
<ol class="tg-steps">{items}</ol>
</div></div>'''


def packing(L, items):
    lis = ''.join(f'<li><label><input type="checkbox"><span class="tg-box" aria-hidden="true"></span><span><b>{a}</b> {b}</span></label></li>' for a, b in items)
    return f'<div class="tg-pack" data-pack><p class="lbl red tg-pack-n" aria-live="polite" data-tpl="{L}" hidden></p><ul>{lis}</ul></div>'


def sponge(L):
    return f'''<figure class="tg-sponge" data-sponge>
<svg viewBox="0 0 320 160" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect x="1" y="1" width="318" height="158" fill="#E9C9B4"/>
<ellipse cx="120" cy="80" rx="46" ry="30" fill="#D9877A"/><ellipse cx="206" cy="92" rx="22" ry="16" fill="#C9786C"/>
<rect class="tg-cover" x="1" y="1" width="318" height="158" fill="#EBCDB9" opacity=".9"/>
<rect x="1" y="1" width="318" height="158" fill="none" {_S}/></svg>
<div class="tg-sponge-ui"><span class="lbl">{L[0]}</span><input type="range" min="0" max="100" value="0" aria-label="{L[2]}"><span class="lbl">{L[1]}</span></div>
<figcaption class="fine-print" data-out data-dry="{L[3]}" data-wet="{L[4]}">{L[3]}</figcaption></figure>'''


# angled brush (bristles cut on a slant) for the brush line-up
ANGLED = (f'<symbol id="tg-angled" viewBox="0 0 60 220"><path d="M14 74l2-50 30-12 0 62z" fill="#2E2627" {_S}/><path d="M22 70V22M30 70V18M38 70V15" stroke="#8A7B78" stroke-opacity=".8" {_T}/>'
          f'<rect x="14" y="72" width="32" height="38" rx="1.5" fill="{PAPER}" {_S}/><path d="M14 79h32M14 103h32" stroke="{INK}" stroke-opacity=".45" {_T}/><path d="M17 110h26l-5 104q-8 5-16 0z" fill="{OX}"/></symbol>')
DEFS = BRUSH_DEFS.replace('</defs></svg>', ANGLED + '</defs></svg>')


def brushes(labels):
    syms = ['tg-angled', 'tg-angled', 'tg-angled', 'tg-angled', 'bc-flat']
    cells = ''.join(f'<li class="tg-b d{i}"><svg viewBox="0 0 60 220" aria-hidden="true"><use href="#{s}"/></svg><span class="lbl">{labels[i]}</span></li>' for i, s in enumerate(syms))
    return f'<ul class="tg-brushes" data-reveal>{cells}</ul>'


def finder(L):
    pills = lambda name, opts: ''.join(f'<label class="bc-pill"><input type="radio" name="{name}" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(opts))
    ans = ''.join(f'<div class="bc-ans" data-ans="{k}"><p class="lbl">{lab}</p><p class="bc-ans-h">{h}</p><p>{b}</p></div>' for k, lab, h, b in L['answers'])
    return f'''<div class="bc-finder" data-finder><div class="bc-q"><fieldset><legend class="lbl">{L['q']}</legend>{pills('tg-look', L['opts'])}</fieldset></div><div class="bc-a" aria-live="polite">{ans}</div></div>'''


# ================================================================= CZECH
_P = lambda *names: ' · '.join(names)
STEPS_CS = [
    (['face', 'neck'], 'base', 'Tonikum', _P('Medi-Peel Hyal Kombucha Tea-Tox Toner'),
     '<p>Obličej už mám umytý, ale tonikum používám jako další hydrataci, dočištění a jemnou exfoliaci: stačí, že vatový tamponek po pleti trochu tře. Projedu celý obličej a vždy přejdu i na krk. Tamponek si odložím, později s ním budu otírat ruku od dalších produktů.</p>'),
    (['face', 'neck'], 'base', 'Sérum s vitaminem C', _P('Image Skincare Vital C'),
     '<p>Můj vitamin C už mnoho let. Hydratuje, nezatěžuje pleť, hezky voní a má obal, ve kterém produkt neoxiduje. Je dražší, ale stojí za to.</p>'),
    (['face', 'neck'], 'base', 'SPF', _P('Round Lab Birch Juice SPF 50+'),
     '<p>Klasika, bez které na slunci nikam. Ideálně nechte péči chvilku vsáknout. Na cestách na to ale moc času nebývá.</p>'),
    (['face', 'under'], 'base', 'Glow filtr', _P('Dior Forever Glow Star Filter, odstín 2'),
     '<p>V létě beru o odstín tmavší, abych ladila s opálením. Jedno zmáčknutí stačí na efekt rozzářené pleti a zbytek dám pod oči. Je hydratační: v létě se mi T-zóna může mastit a výdrž bývá kratší než v chladném období. Mně to nevadí.</p>'),
    (['face'], 'base', 'Fixace první vrstvy', _P('Charlotte Tilbury Airbrush Flawless Setting Spray'),
     '<p>Zafixuji vrstvu, kterou mám na pleti, aby make-up lépe sedl a vydržel déle, když jdu ven do horka. Nechte zaschnout.</p>'),
    (['under'], 'base', 'Korektor jen pod oči', _P('Note Cosmetique BB Concealer 03'),
     '<p>Moje nová láska: kruhy pod očima kryje skvěle. Je na mě dost tmavý, proto ho dávám výhradně pod oči. Stačí opravdu málo a vtisknout houbičkou.</p><aside class="note"><p class="lbl red">Tip vizážistky</p><p>V denním make-upu, hlavně v létě, kruhy nepřekrývejte úplně. Vypadalo by to nepřirozeně.</p></aside>'),
    (['face'], 'base', 'Lehký make-up', _P('Estée Lauder Double Wear Sheer, 2N1'),
     '<p>Odlehčená verze Double Wear: méně odolná, trochu hydratační, sedne asi všem typům pleti kromě velmi suché. Dává lehké krytí a drží. Pigmentu má méně: tón sjednotí, ale zázračné krytí nečekejte. Dnes nechci perfektní pleť, jen vypadat svěže, a ne jako po dvou nocích ve vlaku.</p>'),
    (['contour'], 'base', 'Krémový bronzer', _P('Eveline Choco Glamour 02'),
     '<p>Chladnější odstín. Naberu ho na ruku a zahřeji: dřív na hřbetu ruky, ale ten mám od práce vysušený, tak teď používám vnitřní stranu dlaně. Je i teplejší, produkt se rozpustí rychleji. Snadno se roztírá a míchá s jinými produkty, a když ho naberete moc, jde lehce setřít. Pak si ruku otřu odloženým tamponkem.</p>'),
    (['cheeks'], 'base', 'Tváře: mix 1 : 1', _P('Dior Forever Glow Maximizer Nude', 'YSL Make Me Blush 44'),
     '<p>Moje nové kombo. Glow Maximizer je napůl tvářenka, napůl rozjasňovač, a umí se zafixovat. Smíchám ho s tvářenkou YSL zhruba jedna ku jedné, takže zafixuje i ji a nic dalšího už tváře nepotřebují: je tam barva i lesk.</p>'),
    (['lids', 'outer'], 'opt', 'Oči', _P('Krémové stíny v tyčince', 'Hourglass Ambient Lighting Edit', 'plochý štětec Davydenko č. 7'),
     '<p>Krémové stíny v teplém zlatorůžovém odstínu rozetřu prstem: tenká vrstva, nesrolují se a je to rychlé. Tmavým pudrem z palety a plochým štětcem zafixuji nepohyblivou část víčka, protože každý krémový produkt během dne mizí. Tmavším odstínem bronzeru přidám vnější koutek s výběhem ke spánku a kousek pod spodní víčko.</p><p>Když se ruka zachvěje, projedu místo štětcem se zbytkem korektoru a doťuknu houbičkou.</p>'),
    (['lashes'], 'base', 'Řasy', _P('Eveline Variété Lashes Show Brown'),
     '<p>Tmavě hnědá řasenka, kterou si vozím z Ukrajiny, protože v Česku stojí několikrát víc. Moje už vysychala, tak jsem do ní kápla silikonové ředidlo na kosmetiku a dá se s ní zase malovat, jen se trochu otiskuje.</p><aside class="note"><p class="lbl red">Poznámka</p><p>Řasenka má krátkou dobu použitelnosti po otevření. Ředění je nouzové řešení na cestu, ne náhrada nové řasenky.</p></aside>'),
    (['brows'], 'base', 'Obočí', _P('Patricia Ledo Absolute Eyebrow 01', 'Physicians Formula liner', 'Benefit 24-Hour Brow Setter'),
     '<p>Tužkou doplním tvar. Liner Physicians Formula jsem si koupila na kreslení pih podle triku, který jsem viděla. Pihy se mi nelíbily, ale liner teď používám na pár chloupků navíc, žádné extra obočí. Gel Benefit: nejdřív vyčesat nahoru, pak do strany. Mám středně tuhé obočí, nelepím ho, jen podtrhnu přirozený tvar.</p>'),
    (['face'], 'base', 'Druhá fixace', _P('Fixační sprej'),
     '<p>Ještě jednou projedu fixačním sprejem. Charlotte Tilbury je dost vlhký a rozprašovač spíš prská. Nově jsem si koupila sprej Fenty Beauty a jeho jemná mlha je úplně jiný příběh.</p>'),
    (['lips'], 'opt', 'Rty', _P('Davydenko Beauty, tužka na rty 05'),
     '<p>K takovému make-upu nechci výrazné rty. Pro mnohé bude tahle tužka tmavá, ale moje rty mají vlastní pigment dost výrazný a tmavý, takže je pro mě nude.</p>'),
    (['contour'], 'base', 'Suchá korekce', _P('Pudr z palety Hourglass', 'štětec na suché textury'),
     '<p>Na štětec naberu pudr z palety, trochu ho smíchám s bronzerem a vtisknu přesně tam, kde jsem korigovala krémovým bronzerem. Zafixuje to a krém vydrží déle.</p>'),
    (['under', 'tzone'], 'eve', 'Rozjasnění', _P('Rozjasňující korektor Sephora'),
     '<p>Velmi světlý hydratační korektor, kterým na večer rozjasním vybraná místa. Přes den ho nepotřebuji.</p>'),
    (['lips'], 'eve', 'Studenější rty', _P('Pupa, tužka na rty 004'),
     '<p>Hodně známá studená růžová tužka. Mám ji v kosmetičce pro případ, že večer chci jiné rty.</p>'),
]
_GUIDE_CS = dict(modes=[('min', 'Minimum'), ('day', 'Den'), ('eve', 'Večer')], modes_label='Varianta make-upu', opt='Volitelné ve dne', eve='Na večer',
                 anchor='krok', prev='Předchozí krok', next='Další krok')
_PACK_CS = [('Tonikum', 'přelité do malé lahvičky: je lehčí a zabere méně místa než sklo'), ('Sérum s vitaminem C', ''), ('SPF 50+', ''), ('Glow filtr', ''),
            ('Fixační sprej', ''), ('Korektor', 'pod oči, plus světlý na večer'), ('Lehký make-up', ''), ('Krémový bronzer', 'zároveň kontura i stíny'),
            ('Glow Maximizer a tvářenka', ''), ('Paleta na obličej', 'pudr, tvářenky, rozjasňovač i stíny v jednom'), ('Krémové stíny v tyčince', ''),
            ('Řasenka', ''), ('Tužka, liner a gel na obočí', ''), ('Dvě tužky na rty', 'nude na den, studená růžová na večer'),
            ('Pět štětců a houbička', ''), ('Tamponky, tyčinky, kartáčky', 'v sáčku z IKEA, ať zaberou co nejméně místa')]

C = {}
C['cs'] = dict(
    toc=[('kratce', 'Postup v kostce'), ('balime', 'Co si zabalit'), ('stetce', 'Pět štětců stačí'), ('navod', 'Návod krok za krokem'),
         ('houbicka', 'Suchá, nebo vlhká houbička?'), ('rasenka', 'Jakou hnědou řasenku'), ('paleta', 'Proč jedna paleta'), ('verdikt', 'Co do kosmetičky'), ('produkty', 'Produkty z videa'), ('faq', 'Časté dotazy')],
    opener='Tentokrát vybaluji svoji cestovní kosmetičku a dělám z ní celý make-up, rovnou v malém hotelovém pokoji v Oděse po noci ve vlaku. Produkty jsou vybrané úsporně a s rozmyslem, aby z nich šel udělat denní i večerní look. Tady je návod krok za krokem, i s tím, proč make-up nanáším suchou houbičkou.',
    pre=DEFS,
    summary_h='Postup v kostce',
    steps=['Tonikum, sérum s vitaminem C a SPF', 'Glow filtr a první fixace sprejem', 'Korektor jen pod oči, nepřekrývat úplně', 'Lehký make-up suchou houbičkou', 'Krémový bronzer zahřátý na dlani', 'Tváře: rozjasňovač a tvářenka 1 : 1', 'Oči, řasy a obočí', 'Druhá fixace, rty a suchá korekce pudrem'],
    tested_h='Pro koho je tenhle návod',
    tested='<p>Pro každého, kdo chce na cesty jednu malou kosmetičku a přesto zvládnout denní i večerní make-up. Žádný produkt navíc: polovina z nich umí dvě věci najednou.</p>',
    sections=[
        ('balime', 'Co si zabalit', '<p>Všechno, co je v kosmetičce. Odškrtejte si, co už máte sbalené:</p>\n' + packing('Sbaleno {n} z {t}', _PACK_CS)),
        ('stetce', 'Pět štětců stačí', '''<p>Na cesty mi stačí pět štětců: čtyři zkosené a jeden plochý. Zkosené používám na konturu, tvářenku, korektor a suché textury, plochý na oči. Víc toho opravdu nepotřebuji.</p>
''' + brushes(['Kontura', 'Tvářenka', 'Korektor', 'Suché textury', 'Oči · č. 7'])),
        ('navod', 'Návod krok za krokem', '''<p>Vyberte variantu: <b>Minimum</b> je make-up bez stínů a rtů, <b>Den</b> je přesně to, co dělám ve videu, a <b>Večer</b> přidává dva kroky navíc. Klikněte na krok a na obličeji uvidíte, kam produkt patří.</p>
''' + guide(_GUIDE_CS, STEPS_CS)),
        ('houbicka', 'Suchá, nebo vlhká houbička?', '''<p>Teď po mně možná poletí kameny, ale make-up nanáším <b>suchou houbičkou</b>. Líbí se mi, jak hustě kryje. Vlhkou houbičkou bude krytí průsvitnější. Moje houbička je sama o sobě dost měkká, takže se s ní suchá na suchou pracuje dobře. U hustšího make-upu ji ale navlhčím.</p>
''' + sponge(('Suchá', 'Vlhká', 'Vlhkost houbičky', 'Suchá houbička: hustší krytí, zarudnutí zmizí.', 'Vlhká houbička: průsvitnější krytí, pleť prosvítá.'))),
        ('rasenka', 'Jakou hnědou řasenku vybrat', '''<p>Eveline Variété je tmavě hnědá, ne světle hnědá. Na mně s kontrastním typem vypadá skvěle. Světlejší, víc do rezava, je hnědá řasenka od Essence, ta na mně dobře nevypadá.</p>
''' + finder(dict(q='Váš typ', opts=[('dark', 'Kontrastní, tmavé vlasy'), ('fair', 'Světlé vlasy'), ('red', 'Zrzavé vlasy')],
                    answers=[('dark', 'Kontrastní typ', 'Tmavě hnědá', 'Eveline Variété Lashes Show Brown: dost tmavá na kontrastní vzhled, a přitom měkčí než černá.'),
                             ('fair', 'Světlé vlasy', 'Rezavě hnědá', 'Hnědá řasenka Essence: světlejší, víc do rezava. Na světlých holkách vypadá moc hezky.'),
                             ('red', 'Zrzavé vlasy', 'Rezavě hnědá', 'Hnědá řasenka Essence: teplý rezavý tón ladí se zrzavými vlasy.')]))),
        ('paleta', 'Proč jedna paleta stačí', '''<p>Paleta Hourglass Ambient Lighting Edit je skvělá investice. Nemusíte kupovat všechny, ale jednu limitku v barvách, které máte rádi, doporučuji: textury jsou pečené, jemné, napůl průsvitné, dají se nanést tence i vrstvit a všechny se spolu míchají. Výrazné tvářenky moc nenosím, ale používám je jako „míchač“ barvy na tváře nebo do make-upu očí. Zlatý rozjasňovač smíchaný s tvářenkou má na opálené pleti krásnou barvu.</p>'''),
    ],
    verdict_h='Co do cestovní kosmetičky',
    verdict=[('Základ', 'vtag v-yes', ['Tonikum v malé lahvičce', 'Sérum s vitaminem C a SPF', 'Lehký make-up a korektor', 'Krémový bronzer', 'Tmavě hnědá řasenka', 'Gel na obočí', 'Fixační sprej']),
             ('Dvě role v jednom', 'vtag v-dep', ['Paleta: pudr, tvářenka, stíny, rozjasňovač', 'Glow Maximizer: tvářenka i rozjasňovač', 'Bronzer: kontura i stíny', 'Liner na obočí']),
             ('Jen na večer', 'vtag v-sw', ['Rozjasňující korektor Sephora', 'Studená růžová tužka Pupa 004'])],
    verdict_foot='',
    lessons_h='Tři věci, které si z toho vzít',
    lessons=[('Méně produktů, víc funkcí.', 'Bronzer jako kontura i stíny, paleta místo pěti krabiček. Kosmetička je pak malá a zvládne den i večer.'),
             ('Fixujte po vrstvách.', 'Sprej po podkladu, pudr na krémové stíny a bronzer. V horku vydrží krémové produkty jen tak, jak je zafixujete.'),
             ('Přes den nepřekrývejte všechno.', 'Korektor jen tam, kde je potřeba, lehký make-up a svěžest místo dokonalé pleti.')],
    learn_h='Chcete si sestavit vlastní kosmetičku?',
    cta_note='Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> projdeme vaši kosmetiku a sestavíme z ní kompaktní sadu na cesty i na každý den.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Profesionální líčení v Praze',
    cta_text='Make-up, který vydrží horko i dlouhý den: na svatby, focení i večerní akce.',
    cta_links=[('Nude líčení', '/nude-liceni/'), ('Svatební líčení', '/svatebni-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Co si zabalit do cestovní kosmetičky na make-up?', 'Péči (tonikum, sérum, SPF), lehký make-up, korektor, krémový bronzer, tvářenku, paletu na obličej, řasenku, tužku a gel na obočí, tužku na rty, fixační sprej, pár štětců a houbičku. Vybírejte produkty, které umí víc věcí najednou.'),
         ('Kolik štětců potřebuji na cesty?', 'Mně stačí pět: čtyři zkosené na konturu, tvářenku, korektor a suché textury a jeden plochý na oči. Krémové stíny se dají rozetřít i prstem.'),
         ('Nanášet make-up suchou, nebo vlhkou houbičkou?', 'Suchá houbička dává hustší krytí, vlhká průsvitnější. Lehký make-up nanáším suchou, protože je houbička dost měkká. Hustší make-up nanáším navlhčenou.'),
         ('Jak zajistit, aby make-up vydržel v horku?', 'Fixovat po vrstvách: sprej po podkladu, pudr na krémové stíny a přes místa s krémovým bronzerem a na konci znovu sprej. Hydratační produkty v létě vydrží o něco kratší dobu.'),
         ('Proč zahřívat krémový bronzer na dlani?', 'Na dlani se produkt rychleji rozpustí a lépe se roztírá. Vnitřní strana dlaně je teplejší než hřbet ruky a nevysušuje se tolik.'),
         ('Jakou hnědou řasenku vybrat?', 'Na kontrastní typ tmavě hnědou, třeba Eveline Variété Lashes Show Brown. Na světlé a zrzavé vlasy rezavě hnědou, třeba od Essence.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

# ================================================================= ENGLISH
STEPS_EN = [
    (['face', 'neck'], 'base', 'Toner', _P('Medi-Peel Hyal Kombucha Tea-Tox Toner'),
     "<p>My face is already washed, but I use toner for extra hydration, a final cleanse and gentle exfoliation: the cotton pad rubbing over the skin is enough. I go over the whole face and always down the neck. I keep the pad, because later I'll wipe my hand on it between products.</p>"),
    (['face', 'neck'], 'base', 'Vitamin C serum', _P('Image Skincare Vital C'),
     "<p>My vitamin C for many years. It hydrates, doesn't weigh the skin down, smells lovely and comes in packaging that keeps it from oxidising. Pricier, but worth it.</p>"),
    (['face', 'neck'], 'base', 'SPF', _P('Round Lab Birch Juice SPF 50+'),
     "<p>A classic I never go without in the sun. Ideally let the skincare sink in for a moment. When you're travelling, there's rarely time.</p>"),
    (['face', 'under'], 'base', 'Glow filter', _P('Dior Forever Glow Star Filter, shade 2'),
     "<p>In summer I go one shade deeper to match my tan. One pump is enough for a glowing effect, and the rest goes under the eyes. It's hydrating: in summer my T-zone can get oily and wear is shorter than in the colder months. That doesn't bother me.</p>"),
    (['face'], 'base', 'Set the first layer', _P('Charlotte Tilbury Airbrush Flawless Setting Spray'),
     "<p>I set what's on my skin so the base sits better and lasts longer once I'm out in the heat. Let it dry.</p>"),
    (['under'], 'base', 'Concealer under the eyes only', _P('Note Cosmetique BB Concealer 03'),
     "<p>My new love: it covers my under-eye circles beautifully. It's quite dark on me, so I use it under the eyes only. You need very little; press it in with a sponge.</p><aside class=\"note\"><p class=\"lbl red\">Pro tip</p><p>In day makeup, especially in summer, don't cover the circles completely. It looks unnatural.</p></aside>"),
    (['face'], 'base', 'A light foundation', _P('Estée Lauder Double Wear Sheer, 2N1'),
     "<p>The lighter version of Double Wear: less long-wearing, slightly hydrating, and it suits probably every skin type except very dry. Light coverage that stays. It has less pigment: it evens out the tone, but don't expect miracle coverage. Today I don't want perfect skin, just to look fresh, not like I spent two nights on a train.</p>"),
    (['contour'], 'base', 'Cream bronzer', _P('Eveline Choco Glamour 02'),
     "<p>A cooler shade. I pick it up on my hand and warm it: I used to use the back of my hand, but it's dry from work, so now I use the inside of my palm. It's warmer too, so the product melts faster. It blends easily, mixes with other products, and if you take too much it wipes off easily. Then I wipe my hand on the saved cotton pad.</p>"),
    (['cheeks'], 'base', 'Cheeks: a 1 : 1 mix', _P('Dior Forever Glow Maximizer Nude', 'YSL Make Me Blush 44'),
     "<p>My new combo. Glow Maximizer is half blush, half highlighter, and it sets. I mix it with the YSL blush roughly one to one, so it sets the blush too and the cheeks need nothing else: colour and glow in one.</p>"),
    (['lids', 'outer'], 'opt', 'Eyes', _P('Cream eyeshadow stick', 'Hourglass Ambient Lighting Edit', 'Davydenko flat brush no. 7'),
     "<p>I blend a warm golden-rose cream shadow with a finger: a thin layer, it doesn't crease, and it's fast. With the dark powder from the palette and a flat brush I set the fixed part of the lid, because any cream product fades during the day. A deeper shade of bronzer goes on the outer corner, swept towards the temple, and a little under the lower lash line.</p><p>If your hand slips, go over it with a brush that still has some concealer on it and pat with the sponge.</p>"),
    (['lashes'], 'base', 'Lashes', _P('Eveline Variété Lashes Show Brown'),
     "<p>A dark brown mascara I stock up on in Ukraine, because in the Czech Republic it costs several times more. Mine was drying out, so I added a drop of silicone makeup thinner and it works again, it just transfers a little.</p><aside class=\"note\"><p class=\"lbl red\">Note</p><p>Mascara has a short period after opening. Thinning it is an emergency fix for a trip, not a replacement for a new tube.</p></aside>"),
    (['brows'], 'base', 'Brows', _P('Patricia Ledo Absolute Eyebrow 01', 'Physicians Formula liner', 'Benefit 24-Hour Brow Setter'),
     "<p>I fill the shape with the pencil. I bought the Physicians Formula liner to draw freckles after seeing the hack somewhere. I didn't like the freckles, but now I use the liner for a few extra hair strokes, no statement brows. Benefit gel: brush up first, then sideways. My brows are medium-coarse, so I don't glue them; I just bring out their natural shape.</p>"),
    (['face'], 'base', 'Set again', _P('Setting spray'),
     "<p>One more pass of setting spray. The Charlotte Tilbury one is quite wet and the nozzle spits rather than mists. I've just bought the Fenty Beauty spray, and its fine mist is a different story.</p>"),
    (['lips'], 'opt', 'Lips', _P('Davydenko Beauty lip pencil 05'),
     "<p>With this kind of makeup I don't want bold lips. For many people this pencil will look dark, but my natural lip pigment is quite strong and dark, so for me it's a nude.</p>"),
    (['contour'], 'base', 'Dry correction', _P('Powder from the Hourglass palette', 'brush for dry textures'),
     "<p>I pick up powder from the palette, mix in a little bronzer and press it exactly where I used the cream bronzer. It sets the cream so it lasts longer.</p>"),
    (['under', 'tzone'], 'eve', 'Brightening', _P('Sephora brightening concealer'),
     "<p>A very light, hydrating concealer I use in the evening to brighten selected areas. I don't need it during the day.</p>"),
    (['lips'], 'eve', 'Cooler lips', _P('Pupa lip pencil 004'),
     '<p>A well-known cool pink pencil. It lives in my bag in case I want different lips in the evening.</p>'),
]
_GUIDE_EN = dict(modes=[('min', 'Minimal'), ('day', 'Day'), ('eve', 'Evening')], modes_label='Makeup version', opt='Optional by day', eve='Evening',
                 anchor='step', prev='Previous step', next='Next step')
_PACK_EN = [('Toner', 'decanted into a small bottle: lighter and smaller than glass'), ('Vitamin C serum', ''), ('SPF 50+', ''), ('Glow filter', ''),
            ('Setting spray', ''), ('Concealer', 'for under the eyes, plus a light one for evenings'), ('Light foundation', ''), ('Cream bronzer', 'contour and eyeshadow in one'),
            ('Glow Maximizer and blush', ''), ('Face palette', 'powder, blushes, highlighter and eyeshadow in one'), ('Cream eyeshadow stick', ''),
            ('Mascara', ''), ('Brow pencil, liner and gel', ''), ('Two lip pencils', 'a nude for day, a cool pink for evening'),
            ('Five brushes and a sponge', ''), ('Cotton pads, swabs, spoolies', 'in an IKEA bag so they take up as little room as possible')]

C['en'] = dict(
    toc=[('summary', 'The routine in short'), ('packing', 'What to pack'), ('brushes', 'Five brushes are enough'), ('how-to', 'Step-by-step guide'),
         ('sponge', 'Dry or damp sponge?'), ('mascara', 'Which brown mascara'), ('palette', 'Why one palette'), ('verdict', 'What goes in the bag'), ('products', 'Products in the video'), ('faq', 'FAQ')],
    opener="This time I unpack my travel makeup bag and do a full look with it, right in a tiny hotel room in Odesa after a night on the train. The products are chosen sparingly and with purpose, so they work for both a day and an evening look. Here is the step-by-step guide, including why I apply foundation with a dry sponge.",
    pre=DEFS,
    summary_h='The routine in short',
    steps=['Toner, vitamin C serum and SPF', 'Glow filter and a first pass of setting spray', "Concealer under the eyes only, don't cover everything", 'Light foundation with a dry sponge', 'Cream bronzer warmed on the palm', 'Cheeks: highlighter and blush 1 : 1', 'Eyes, lashes and brows', 'Set again, lips and a dry powder correction'],
    tested_h='Who this guide is for',
    tested="<p>For anyone who wants one small bag for a trip and still a day and an evening look. No extras: half of these products do two jobs at once.</p>",
    sections=[
        ('packing', 'What to pack', '<p>Everything in my bag. Tick off what you have packed:</p>\n' + packing('{n} of {t} packed', _PACK_EN)),
        ('brushes', 'Five brushes are enough', '''<p>Five brushes are all I need for a trip: four angled and one flat. The angled ones are for contour, blush, concealer and dry textures; the flat one is for eyes. I really don't need more.</p>
''' + brushes(['Contour', 'Blush', 'Concealer', 'Dry textures', 'Eyes · no. 7'])),
        ('how-to', 'Step-by-step guide', '''<p>Pick a version: <b>Minimal</b> is the look without eyeshadow and lips, <b>Day</b> is exactly what I do in the video, and <b>Evening</b> adds two extra steps. Tap a step to see on the face where the product goes.</p>
''' + guide(_GUIDE_EN, STEPS_EN)),
        ('sponge', 'Dry or damp sponge?', '''<p>People may throw stones at me for this, but I apply foundation with a <b>dry sponge</b>. I like how densely it covers. With a damp sponge the coverage is sheerer. My sponge is soft enough that working dry-on-dry is fine. For a heavier foundation, though, I do dampen it.</p>
''' + sponge(('Dry', 'Damp', 'Sponge dampness', 'Dry sponge: denser coverage, the redness disappears.', 'Damp sponge: sheerer coverage, the skin shows through.'))),
        ('mascara', 'Which brown mascara to choose', '''<p>Eveline Variété is dark brown, not light brown. On me, with my high-contrast colouring, it looks great. A lighter, more reddish brown is the Essence brown mascara, which doesn't look good on me.</p>
''' + finder(dict(q='Your colouring', opts=[('dark', 'High contrast, dark hair'), ('fair', 'Fair hair'), ('red', 'Red hair')],
                    answers=[('dark', 'High contrast', 'Dark brown', 'Eveline Variété Lashes Show Brown: dark enough for high-contrast colouring, yet softer than black.'),
                             ('fair', 'Fair hair', 'Reddish brown', 'Essence brown mascara: lighter and more reddish. It looks lovely on blondes.'),
                             ('red', 'Red hair', 'Reddish brown', 'Essence brown mascara: the warm reddish tone suits red hair.')]))),
        ('palette', 'Why one palette is enough', '''<p>The Hourglass Ambient Lighting Edit palette was a great buy. You don't need them all, but I recommend one limited edition in colours you love: the textures are baked, soft and semi-sheer, they can be applied thinly or built up, and they all mix together. I rarely wear bright blush, but I use it as a colour mixer for the cheeks or eye makeup. The golden highlighter mixed with blush looks beautiful on tanned skin.</p>'''),
    ],
    verdict_h='What goes in a travel makeup bag',
    verdict=[('The basics', 'vtag v-yes', ['Toner in a small bottle', 'Vitamin C serum and SPF', 'Light foundation and concealer', 'Cream bronzer', 'Dark brown mascara', 'Brow gel', 'Setting spray']),
             ('Two jobs in one', 'vtag v-dep', ['Palette: powder, blush, eyeshadow, highlighter', 'Glow Maximizer: blush and highlighter', 'Bronzer: contour and eyeshadow', 'Brow liner']),
             ('Evening only', 'vtag v-sw', ['Sephora brightening concealer', 'Pupa 004 cool pink lip pencil'])],
    verdict_foot='',
    lessons_h='Three things to take away',
    lessons=[('Fewer products, more jobs.', 'Bronzer as contour and eyeshadow, one palette instead of five compacts. The bag stays small and still covers day and evening.'),
             ('Set in layers.', 'Spray after the base, powder over cream eyeshadow and bronzer. In the heat, cream products last only as long as you set them.'),
             ("Don't cover everything by day.", 'Concealer only where needed, a light foundation, and freshness instead of perfect skin.')],
    learn_h='Want to build your own kit?',
    cta_note='In a <a href="/en/courses/">one-on-one makeup course</a> we go through your products and put together a compact kit for travel and every day.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Professional makeup in Prague',
    cta_text='Makeup that survives heat and a long day: for weddings, shoots and evening events.',
    cta_links=[('Nude makeup', '/en/nude-makeup/'), ('Wedding makeup', '/en/wedding/')],
    faq_h='Frequently asked questions',
    faq=[('What should I pack in a travel makeup bag?', 'Skincare (toner, serum, SPF), a light foundation, concealer, cream bronzer, blush, a face palette, mascara, brow pencil and gel, a lip pencil, setting spray, a few brushes and a sponge. Choose products that do more than one job.'),
         ('How many brushes do I need for travel?', 'Five are enough for me: four angled ones for contour, blush, concealer and dry textures, and one flat brush for eyes. Cream eyeshadow can be blended with a finger.'),
         ('Should I apply foundation with a dry or damp sponge?', 'A dry sponge gives denser coverage, a damp one a sheerer finish. I apply a light foundation with a dry sponge because mine is soft enough. A heavier foundation goes on with a damp sponge.'),
         ('How do I make makeup last in the heat?', 'Set it in layers: spray after the base, powder over cream eyeshadow and over the cream bronzer, and spray again at the end. Hydrating products wear a little shorter in summer.'),
         ('Why warm cream bronzer on the palm?', 'The product melts faster on the palm and blends more easily. The inside of the palm is warmer than the back of the hand and doesn\'t dry out as much.'),
         ('Which brown mascara should I choose?', 'Dark brown for high-contrast colouring, such as Eveline Variété Lashes Show Brown. Reddish brown for fair or red hair, such as the Essence brown mascara.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

HOWTO = {lang: [(t, ' '.join(__import__('re').sub(r'<aside.*?</aside>|<[^>]+>', ' ', b).split())) for _z, _m, t, _p, b in (STEPS_CS if lang == 'cs' else STEPS_EN)] for lang in ('cs', 'en')}
SUPPLY = [n for n, _ in PRODUCTS]
TOOLS = {'cs': ['Pět štětců (čtyři zkosené, jeden plochý)', 'Houbička na make-up', 'Vatové tamponky'], 'en': ['Five brushes (four angled, one flat)', 'Makeup sponge', 'Cotton pads']}

EXTRA = dict(products=PRODUCTS, brands=BRANDS, about=('Cestovní kosmetička', 'Travel makeup bag'),
             video_name='Моя косметичка в подорож', howto=dict(steps=HOWTO, supply=SUPPLY, tools=TOOLS))
