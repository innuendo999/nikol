"""Article: how I wash makeup brushes (video gc_bq04a_G0).

Illustrations are inline SVG (brush symbols defined once in DEFS); animations live in site.css (.bc-*),
the bristle finder and the technique tabs are enhanced in site.js (both readable without JS)."""

BRANDS = ['Protex', 'Safeguard']

# ---------------------------------------------------------------- shared SVG
DEFS = '''<svg class="visually-hidden" aria-hidden="true" focusable="false"><defs>
<linearGradient id="bc-metal" x1="0" x2="1"><stop offset="0" stop-color="#B9A9A4"/><stop offset=".38" stop-color="#F6EFEC"/><stop offset=".62" stop-color="#D8C9C4"/><stop offset="1" stop-color="#8E7C77"/></linearGradient>
<linearGradient id="bc-ox" x1="0" x2="1"><stop offset="0" stop-color="#2A0A0E"/><stop offset=".42" stop-color="#5A1C24"/><stop offset="1" stop-color="#2A0A0E"/></linearGradient>
<linearGradient id="bc-red" x1="0" x2="1"><stop offset="0" stop-color="#7E1822"/><stop offset=".42" stop-color="#C23A45"/><stop offset="1" stop-color="#7E1822"/></linearGradient>
<linearGradient id="bc-pink" x1="0" x2="1"><stop offset="0" stop-color="#D58F84"/><stop offset=".42" stop-color="#F7CBC2"/><stop offset="1" stop-color="#C47D72"/></linearGradient>
<linearGradient id="bc-nat" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#5E3A28"/><stop offset=".6" stop-color="#B4835C"/><stop offset="1" stop-color="#E9CCAA"/></linearGradient>
<linearGradient id="bc-syn" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#1C1416"/><stop offset=".7" stop-color="#4A3A3D"/><stop offset="1" stop-color="#7C6A6C"/></linearGradient>
<linearGradient id="bc-duog" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#1C1416"/><stop offset=".55" stop-color="#3A2D30"/><stop offset=".72" stop-color="#EDE6E1"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
<linearGradient id="bc-soap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F4B9AE"/></linearGradient>
<symbol id="bc-round" viewBox="0 0 60 220"><path d="M11 72C5 42 13 8 30 5c17 3 25 37 19 67z" fill="url(#bc-nat)"/><path d="M22 60c-2-20 2-42 8-48" stroke="#fff" stroke-opacity=".35" stroke-width="2" fill="none"/><rect x="11" y="70" width="38" height="40" rx="4" fill="url(#bc-metal)"/><path d="M13 108h34l-8 106q-9 6-18 0z" fill="url(#bc-ox)"/></symbol>
<symbol id="bc-flat" viewBox="0 0 60 220"><path d="M12 72l1-48q17-22 34 0l1 48z" fill="url(#bc-syn)"/><path d="M24 66V22" stroke="#fff" stroke-opacity=".25" stroke-width="2"/><rect x="12" y="70" width="36" height="42" rx="3" fill="url(#bc-metal)"/><path d="M15 110h30l-7 104q-8 6-16 0z" fill="url(#bc-red)"/></symbol>
<symbol id="bc-fine" viewBox="0 0 60 220"><path d="M25 72q-2-32 5-68 7 36 5 68z" fill="url(#bc-syn)"/><rect x="24" y="70" width="12" height="52" rx="2" fill="url(#bc-metal)"/><path d="M24.5 120h11L33 214q-3 4-6 0z" fill="url(#bc-ox)"/></symbol>
<symbol id="bc-duo" viewBox="0 0 60 220"><path d="M10 72c-2-26 2-50 20-54 18 4 22 28 20 54z" fill="url(#bc-duog)"/><rect x="10" y="70" width="40" height="38" rx="4" fill="url(#bc-metal)"/><path d="M13 106h34l-8 108q-9 6-18 0z" fill="url(#bc-pink)"/></symbol>
<symbol id="bc-bar" viewBox="0 0 200 70"><rect x="4" y="10" width="192" height="56" rx="22" fill="#D7BDB6" opacity=".45"/><rect width="192" height="58" rx="22" fill="url(#bc-soap)"/><rect x="22" y="12" width="148" height="14" rx="7" fill="#fff" opacity=".6"/></symbol>
</defs></svg>'''


def stage(brush, motion, extra=''):
    """Animated washing demo: a brush (bristles down) moving over a soap bar."""
    return (f'<svg class="bc-stage" viewBox="0 0 400 280" role="img" aria-hidden="true">'
            f'<use href="#bc-bar" x="100" y="200" width="200" height="70"/>'
            f'<g class="bc-mv bc-{motion}"><g transform="translate(200 214) rotate(180)"><use href="#bc-{brush}" x="-24" width="48" height="175"/></g></g>'
            f'<circle class="bc-foam" cx="150" cy="206" r="7"/><circle class="bc-foam d2" cx="252" cy="204" r="9"/><circle class="bc-foam d3" cx="204" cy="198" r="5"/>'
            f'{extra}</svg>')


RULE_FIG = '''<div class="bc-compare">
<figure class="bc-panel bc-bad"><svg viewBox="0 0 120 230" aria-hidden="true"><use href="#bc-round" x="30" y="10" width="60" height="220"/><rect class="bc-glue" x="41" y="80" width="38" height="40" rx="4" fill="#A8232F"/><g fill="#7DB3DA"><path class="bc-in" d="M60 22q-5 7 0 11 5-4 0-11z"/><path class="bc-in d2" d="M50 28q-4 6 0 9 4-3 0-9z"/><path class="bc-in d3" d="M70 28q-4 6 0 9 4-3 0-9z"/></g></svg><figcaption>✕ {bad}</figcaption></figure>
<figure class="bc-panel bc-good"><svg viewBox="0 0 120 230" aria-hidden="true"><g transform="translate(120 222) rotate(180)"><use href="#bc-round" x="30" y="10" width="60" height="220"/></g><g fill="#7DB3DA"><path class="bc-out" d="M60 202q-5 7 0 11 5-4 0-11z"/><path class="bc-out d2" d="M52 196q-4 6 0 9 4-3 0-9z"/><path class="bc-out d3" d="M68 196q-4 6 0 9 4-3 0-9z"/></g></svg><figcaption>✓ {good}</figcaption></figure>
</div>'''

TOWEL = '''<figure class="bc-towel"><svg viewBox="0 0 520 330" role="img" aria-label="{alt}"><rect width="520" height="330" rx="6" fill="#F5E4DF"/><path d="M0 40h520M0 290h520" stroke="#E8CFC8" stroke-width="10"/>
<g class="bc-lay"><g transform="translate(40 85) rotate(-90)"><use href="#bc-round" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay r d1"><g transform="translate(480 130) rotate(90)"><use href="#bc-flat" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay d2"><g transform="translate(40 175) rotate(-90)"><use href="#bc-duo" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay r d3"><g transform="translate(480 220) rotate(90)"><use href="#bc-fine" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay d4"><g transform="translate(40 260) rotate(-90)"><use href="#bc-round" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay r d2"><g transform="translate(330 85) rotate(90)"><use href="#bc-fine" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay d3"><g transform="translate(190 175) rotate(-90)"><use href="#bc-flat" x="-15" width="30" height="110"/></g></g>
<g class="bc-lay r d4"><g transform="translate(330 260) rotate(90)"><use href="#bc-duo" x="-15" width="30" height="110"/></g></g>
</svg><figcaption class="fine-print">{cap}</figcaption></figure>'''

OIL_SVG = [
    '<svg viewBox="0 0 200 150" aria-hidden="true"><path d="M92 6h16v10l8 10v36a5 5 0 0 1-5 5H89a5 5 0 0 1-5-5V26l8-10z" fill="#E7C46A"/><rect x="91" y="2" width="18" height="7" rx="2" fill="#7A4A0B"/><path class="bc-drop" d="M100 76q-6 9 0 13 6-4 0-13z" fill="#D9A93A"/><g transform="translate(100 150) rotate(180)"><use href="#bc-flat" x="-12" width="24" height="66"/></g></svg>',
    '<svg viewBox="0 0 200 150" aria-hidden="true"><ellipse cx="100" cy="122" rx="70" ry="18" fill="#F5E4DF"/><ellipse class="bc-melt" cx="100" cy="122" rx="40" ry="9" fill="#A8232F"/><g class="bc-mv bc-gentle"><g transform="translate(100 120) rotate(180)"><use href="#bc-flat" x="-20" width="40" height="110"/></g></g></svg>',
    '<svg viewBox="0 0 200 150" aria-hidden="true"><use href="#bc-bar" x="40" y="98" width="120" height="44"/><g class="bc-mv bc-circle"><g transform="translate(100 106) rotate(180)"><use href="#bc-round" x="-18" width="36" height="100"/></g></g><circle class="bc-foam" cx="70" cy="102" r="5"/><circle class="bc-foam d2" cx="130" cy="102" r="6"/></svg>',
]


def finder(L):
    """Bristle × quality picker. Without JS every answer is listed; with JS only the selected one shows."""
    pills = lambda name, opts: ''.join(
        f'<label class="bc-pill"><input type="radio" name="{name}" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>'
        for i, (v, t) in enumerate(opts))
    ans = ''.join(f'<div class="bc-ans" data-ans="{k}"><p class="lbl red">{lab}</p><p class="bc-ans-h">{h}</p><p>{b}</p></div>' for k, lab, h, b in L['answers'])
    return f'''<div class="bc-finder" data-finder>
<div class="bc-q"><fieldset><legend class="lbl">{L['q1']}</legend>{pills('bc-fiber', L['fiber'])}</fieldset>
<fieldset><legend class="lbl">{L['q2']}</legend>{pills('bc-quality', L['quality'])}</fieldset></div>
<div class="bc-a" aria-live="polite">{ans}</div>
</div>'''


def tabs(L):
    """Technique by brush shape. Without JS the panes are stacked with their own h3."""
    btns = ''.join(f'<button type="button" role="tab" data-tab="{k}"><svg viewBox="0 0 60 220" aria-hidden="true"><use href="#bc-{k}"/></svg>{name}</button>' for k, name, *_ in L)
    panes = ''.join(f'<div class="bc-pane" data-pane="{k}" role="tabpanel"><div class="bc-stage-wrap">{stage(k, motion)}<span class="bc-motion lbl">{tag}</span></div><div class="bc-pane-text"><h3>{name}</h3>{body}</div></div>'
                    for k, name, motion, tag, body in L)
    return f'<div class="bc-tabs" data-tabs><div class="bc-tablist" role="tablist" hidden>{btns}</div>{panes}</div>'


def oil_steps(items):
    return '<ol class="bc-steps">' + ''.join(f'<li><span class="bc-n" aria-hidden="true">{i + 1}</span>{OIL_SVG[i]}<p><strong>{h}</strong></p><p class="fs-16">{b}</p></li>' for i, (h, b) in enumerate(items)) + '</ol>'


def spots(items):
    return '<div class="bc-spots">' + ''.join(f'<details class="bc-spot {cls}"><summary><span class="bc-e" aria-hidden="true">{e}</span>{q}<span class="pm" aria-hidden="true">+</span></summary><p>{a}</p></details>' for e, q, cls, a in items) + '</div>'


def myths(items):
    return '<div class="bc-myths">' + ''.join(f'<details class="bc-myth"><summary><span class="serif">{q}</span><span class="lbl muted2">{hint}</span></summary><p><span class="vtag {cls}">{lab}</span> {a}</p></details>' for q, hint, cls, lab, a in items) + '</div>'


def temp(lbls):
    return '<div class="bc-temp" aria-hidden="true"><div class="bc-temp-bar"><span class="bc-temp-dot"></span></div><div class="bc-temp-lbl">' + ''.join(f'<span>{x}</span>' for x in lbls) + '</div></div>'


# ================================================================= CZECH
C = {}
_FINDER_CS = dict(
    q1='Štětiny', q2='Kvalita',
    fiber=[('natural', 'Přírodní'), ('synth', 'Syntetické')],
    quality=[('premium', 'Kvalitní'), ('budget', 'Levný')],
    answers=[
        ('natural-premium', 'Přírodní · kvalitní', 'Tuhé mýdlo', 'Klidně obyčejné tuhé mýdlo. Kdyby štětiny po čase začaly tvrdnout, ošetřete je kondicionérem nebo maskou na vlasy, které uzavřou kutikulu chloupků. Jen krátce, žádné hodiny.'),
        ('natural-budget', 'Přírodní · levný', 'Šampon a kondicionér', 'Místo mýdla šampon a potom krátce kondicionér nebo maska na vlasy. V masce je nenechávejte dlouho: stačí, než domyjete ostatní štětce.'),
        ('synth-premium', 'Syntetické · kvalitní', 'Tuhé mýdlo bez obav', 'Kvalitní syntetika mýdlo snese bez problémů. Na krémové textury, jako je make-up nebo korektor, nejdřív kapka oleje, potom mýdlo.'),
        ('synth-budget', 'Syntetické · levný', 'Něco šetrnějšího', 'Levné štětce se po mýdle rychle rozčepýří. Sáhněte po jemném šamponu nebo speciálním čističi na štětce. Je to v pořádku, jen to vyjde dráž.'),
    ])
_TABS_CS = [
    ('round', 'Kulaté štětce', 'circle', 'Krouživě',
     '<p>Navlhčete štětec a krouživými pohyby přejíždějte po kostce mýdla. Štětec je kulatý, tak i pohyb je kulatý. Netlačte, není to potřeba. Stačí lehce, ale pořádně, aby se mýdlo dostalo dovnitř a napěnilo.</p>'
     '<p class="bc-batch"><span>🧼 ×10</span>→<span>💧 ×10</span>→<span>ručník</span></p>'
     '<p class="fs-16">Štětce třídím do skupin: namydlím deset středních nebo malých kulatých za sebou, pak všech deset opláchnu a odložím na ručník.</p>'),
    ('flat', 'Ploché štětce', 'stroke', 'Tahy a „kočičí tlapka“',
     '<p>Plochým štětcem nikdy nekružte. Štětinám to nedělá dobře, protože s ním krouživě ani nepracujeme, jen tahy. Stejnými tahy ho tedy i myjte. Klepejte jím do mýdla jako kočičí tlapkou, hlaďte tam a zpátky, odložte a nechte chvilku odležet. Make-up se mezitím uvolní.</p>'),
    ('fine', 'Tenké štětce na linky', 'gentle', 'Velmi jemně',
     '<p>Jejich hodnota je v tenkých štětinách, které kreslí přesné linky. Když je při mytí moc mačkáte, rozčepýří se a těžko se vracejí do tvaru.</p>'
     '<aside class="note"><p class="lbl red">Trik na vlastní riziko</p><p>Na okamžik ponořte do vroucí vody jen štětiny, ne plast, a stáhnou se zpět. Některé štětce se ale můžou roztavit.</p></aside>'),
    ('duo', 'Duo fiber', 'circle', 'Krouživě',
     '<p>I když je trochu zploštělý, můžete ho mýt krouživě. Odpovídá to jeho tvaru a tomu, jak s ním pracujete.</p>'),
]

C['cs'] = dict(
    toc=[('kratce', 'Postup v kostce'), ('pomucky', 'Co budete potřebovat'), ('stetiny', 'Přírodní, nebo syntetické?'), ('pravidla', 'Tři zlatá pravidla'),
         ('technika', 'Technika podle tvaru'), ('olej', 'Make-up a rtěnka, které nejdou vymýt'), ('suseni', 'Sušení'), ('praxe', 'Tipy z praxe'),
         ('myty', 'Mýtus, nebo fakt?'), ('verdikt', 'Co dělat a co ne'), ('faq', 'Časté dotazy')],
    opener='Mytí štětců nemiluje skoro nikdo, a vizážistky už vůbec ne. Já jich ale někdy myju padesát nebo i sto za den, takže jsem si vypracovala postup, který je rychlý, levný a štětcům neublíží. Žádné zázračné přípravky a žádná dvacetiminutová procedura: kostka mýdla, pár pravidel a správná technika.',
    pre=DEFS,
    summary_h='Postup v kostce',
    steps=['Tuhé antibakteriální mýdlo, silikonová podložka, rukavice a ručník', 'Mokrý štětec vždy špičkou dolů a nikdy ho nenamáčejte', 'Vlažná voda: ne horká, ne studená', 'Kulaté štětce krouživě, ploché jen tahy', 'Make-up a rtěnku nejdřív rozpusťte kapkou oleje', 'Myjte po dávkách, třeba po deseti', 'Sušte naplocho na ručníku, s rozestupy', 'Mimo vlhkou koupelnu, horké topení a přímé slunce'],
    tested_h='Pro koho to je',
    tested='<p>Tenhle postup používám na celý pracovní kufr: u mě to není jeden štětec, ale někdy padesát nebo sto najednou. Hodí se pro každého, kdo má doma pár štětců a chce, aby vydržely roky, i pro začínající vizážistky. Na mytí štětců žádná věda není, jen pár pravidel, která se vyplatí dodržet.</p>',
    sections=[
        ('pomucky', 'Co budete potřebovat', '''<dl class="rows">
<div><dt class="k">Tuhé mýdlo</dt><dd class="v">antibakteriální, s hloubkovým čištěním</dd></div>
<div><dt class="k">Silikonová podložka</dt><dd class="v">nejlépe s vroubkovanou částí</dd></div>
<div><dt class="k">Rukavice</dt><dd class="v">stejné, jako na barvení vlasů</dd></div>
<div><dt class="k">Rovný ručník</dt><dd class="v">na sušení, klidně dvakrát větší</dd></div>
<div><dt class="k">Olej</dt><dd class="v">olivový nebo slunečnicový, na krémové textury</dd></div>
<div><dt class="k">Kondicionér na vlasy</dt><dd class="v">jen pro přírodní štětiny, které tvrdnou</dd></div>
</dl>
<p>Mýdlo musí být <b>tuhé, ne tekuté</b>, a pořádně čisticí. Jemné krémové mýdlo nestačí. Mýdlo na praní by možná fungovalo, ale je silně zásadité a vysušuje, takže ho nedoporučuji. V Česku používám <b>Protex</b>, na Ukrajině hledejte <b>Safeguard</b> s nápisem Deep Clean.</p>
<p>Silikonovou podložku mám z AliExpressu a slouží mi už třetím rokem. Nejvíc miluju vroubkovanou část, která vymyje i prach a usazený pigment. A rukavice, ve kterých si barvím vlasy, šetří ruce, když jde o desítky štětců.</p>'''),
        ('stetiny', 'Přírodní, nebo syntetické štětiny?', '''<p>Štětce jsou jen dvou druhů: přírodní a syntetické. Třetí druh neexistuje, nanejvýš mix, jako u duo fiber. Dřív jsem přírodní štětce myla šamponem, protože z obyčejného mýdla tvrdnou, a to je pravda. Zkušenost mě ale naučila jedno: <b>kvalitní, dražší štětec mýdlo prostě vydrží.</b></p>
<p>Prémiové štětce od ukrajinských značek jsem za rok ani jednou nemusela ošetřit maskou, nikdy nezatvrdly, ať jsem je myla čímkoli. Naopak některé levné štětce z AliExpressu, se kterými jsem začínala, se rozčepýří během půl vteřiny, po mýdle i po šamponu. Pár z nich používám dodnes, ostatní sedí na lavičce náhradníků.</p>
<p class="lbl red">Vyberte svůj štětec</p>
''' + finder(_FINDER_CS) + '''
<aside class="note"><p class="lbl red">Proč ne speciální čističe?</p><p>Speciální mýdla a šampony na štětce fungují, jen nejsou tak úsporné jako obyčejná kostka mýdla. A expresní čističe štětiny vysušují, takže s nimi nešetřím jen na nejnutnější případy. Investice do dobrého štětce se vrátí na sto procent.</p></aside>'''),
        ('pravidla', 'Tři zlatá pravidla', '''<p>Technika je jednoduchá, ale tahle pravidla jsou zásadní. Všechno ve štětci drží lepidlo, a právě to chceme chránit.</p>
''' + RULE_FIG.format(bad='Štětinami nahoru', good='Štětinami dolů') + '''
<ol class="lessons">
<li><span class="n" aria-hidden="true">1</span><div><p><strong>Mokrý štětec nikdy nedržte štětinami nahoru.</strong></p><p class="fs-16">Voda steče do lepidla v objímce a to se časem rozmočí. Štětiny začnou vypadávat nebo se štětec rozpadne.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><p><strong>Štětce nenamáčejte.</strong></p><p class="fs-16">Nedávejte je všechny do umyvadla a nenechávejte je ležet ve vodě. Důvod je stejný: lepidlo.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><p><strong>Jen vlažná voda.</strong></p><p class="fs-16">Ve studené se kosmetika nevymyje, horká škodí lepidlu.</p></div></li>
</ol>
''' + temp(['Studená', 'Vlažná ✓', 'Horká'])),
        ('technika', 'Technika podle tvaru štětce', '<p>Pohyb při mytí kopíruje pohyb, kterým štětcem pracujete. Vyberte tvar:</p>\n' + tabs(_TABS_CS)),
        ('olej', 'Make-up nebo rtěnka, které nejdou vymýt', '''<p>Hustý syntetický štětec na krémové textury, ve kterém se make-up usadí hluboko uvnitř? Nebo červená rtěnka? Hydrofilní olej nebo micelárka fungují taky, ale nejověřenější je u mě obyčejný olej z kuchyně.</p>
''' + oil_steps([('Kapka oleje', 'Olivový nebo slunečnicový. Opravdu jen kapička a ne hluboko do štětce.'),
                 ('Rozpusťte kosmetiku', 'Olejem z štětce vymyjte make-up nebo rtěnku.'),
                 ('Domyjte mýdlem', 'Mýdlo odstraní olej i zbytky. Opláchnout, otisknout, hotovo.')]) + '''
<aside class="note"><p class="lbl red">Jak jsem na to přišla</p><p>Úplnou náhodou. Jednou mi došlo mýdlo, zjistila jsem to až pozdě večer a ráno jsem se štětci musela do práce. Vymyla jsem je olejem a domyla prostředkem na nádobí. Od té doby mám kostku mýdla vždycky v záloze.</p></aside>'''),
        ('suseni', 'Sušení: naplocho a s rozestupy', '''<p>Po každé dávce štětce položte na <b>rovný ručník</b>. Nestavte je do stojánku a nevěšte je, není to potřeba. Plochý štětec můžete ještě lehce otisknout do ručníku, ale nemačkejte ho. Rozložte je s rozestupy, klidně střídavě hlavou k patě, aby se štětiny nedotýkaly. Přes noc uschnou.</p>
''' + TOWEL.format(alt='Štětce rozložené na ručníku střídavě hlavou k patě', cap='Střídavě hlavou k patě, aby se štětiny nedotýkaly.') + '''
<p class="lbl red">Kam ručník se štětci odnést? Klikněte:</p>
''' + spots([('🛁', 'Koupelna', 'bc-no', 'Raději ne, v koupelně bývá vlhko. Ručník opatrně složím a odnesu do pokoje.'),
             ('🔥', 'Parapet nad topením', 'bc-warn', 'Pozor: horký radiátor pod oknem může štětiny přesušit. Raději je dejte na stůl.'),
             ('🪴', 'Stůl v pokoji', 'bc-ok', 'Ideální. Suchý pokoj bez přímého tepla, do rána všechno uschne.'),
             ('☀️', 'Okno na slunci', 'bc-no', 'Ne. V létě se rukojeť na přímém slunci zahřeje a lepidlo může povolit.')])),
        ('praxe', 'Tipy z praxe', '''<h3>Expresní čistič jen na suché textury</h3>
<p>Když mám klientky za sebou, používám expresní čistič, ale jen na štětce na stíny. Krémové textury jím nikdy nečistím: je to moc práce a vysušuje štětiny. Jednodušší je mít prostě víc štětců.</p>
<h3>Gelové linky smyjte hned</h3>
<p>Nenechávejte gelovou linku zaschnout na štětci. Vysuší ho a štětiny se zkroutí.</p>
<h3>Ze zkušenosti: s jakými štětci začít</h3>
<p>Pokud si teprve skládáte kufr, víc se vyplatí pár kvalitních štětců než krabice levných. Jak vybrat ty, které vám opravdu sednou, procházíme na <a href="/kurzy-liceni/">individuálním kurzu líčení</a>.</p>'''),
        ('myty', 'Mýtus, nebo fakt?', '<p>Tipněte si a rozklikněte.</p>\n' + myths([
            ('Štětce je dobré nechat odmočit ve vodě.', 'Mýtus, nebo fakt?', 'v-sw', 'Mýtus', 'Voda se dostane do lepidla v objímce a štětec se časem rozpadne.'),
            ('Kvalitní přírodní štětec můžete mýt obyčejným mýdlem.', 'Mýtus, nebo fakt?', 'v-yes', 'Fakt', 'Dobré štětce to snesou. Kdyby přece jen ztvrdly, pomůže krátce kondicionér.'),
            ('Čím teplejší voda, tím čistší štětec.', 'Mýtus, nebo fakt?', 'v-sw', 'Mýtus', 'Horká voda škodí lepidlu. Ideální je vlažná.'),
            ('Štětce nejlépe uschnou zavěšené.', 'Mýtus, nebo fakt?', 'v-sw', 'Mýtus', 'Není to potřeba. Naplocho na ručníku s rozestupy přes noc úplně stačí.')])),
    ],
    verdict_h='Co dělat a co ne',
    verdict=[('Dělejte', 'vtag v-yes', ['Tuhé antibakteriální mýdlo', 'Kulaté krouživě, ploché tahy', 'Olej na make-up a rtěnku', 'Sušení naplocho na ručníku', 'Gelové linky smýt hned']),
             ('Opatrně', 'vtag v-dep', ['Šampon a kondicionér na levné přírodní štětce', 'Expresní čistič jen na suché textury', 'Vroucí voda na tenké štětce', 'Mýdlo na praní (vysušuje)']),
             ('Nikdy', 'vtag v-sw', ['Mokrý štětec štětinami nahoru', 'Namáčení v umyvadle', 'Horká voda', 'Sušení na topení nebo na slunci', 'Kroužit plochým štětcem'])],
    verdict_foot='',
    lessons_h='Tři věci, které si z toho vzít',
    lessons=[('Všechno drží lepidlo.', 'Štětinami dolů, žádné namáčení, žádná horká voda ani topení. Tak štětec vydrží roky.'),
             ('Myjte stejně, jako líčíte.', 'Kulatým štětcem pracujete krouživě, tak ho tak i myjte. Plochým jen tahy, ne kroužením.'),
             ('Kvalitní štětec je investice.', 'Dobrý štětec snese obyčejné mýdlo a nepotřebuje drahou péči. Levný se rozčepýří po čemkoli.')],
    learn_h='Chcete vědět, které štětce se vyplatí?',
    cta_note='Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> projdeme vaše štětce i kosmetiku a řekneme si, co se vyplatí a jak se o to starat.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Profesionální líčení v Praze',
    cta_text='Na každou klientku používám čisté štětce umyté přesně tímhle postupem: na svatby, focení i večerní akce.',
    cta_links=[('Svatební líčení', '/svatebni-liceni/'), ('Večerní líčení', '/vecerni-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Čím umýt štětce na make-up?', 'Tuhým antibakteriálním mýdlem s hloubkovým čištěním, například Protex nebo Safeguard Deep Clean. Jemné krémové mýdlo nestačí a mýdlo na praní vysušuje. Levné štětce, které se po mýdle rozčepýří, myjte šetrnějším šamponem.'),
         ('Můžu mýt přírodní štětce mýdlem?', 'Kvalitní ano, z mojí zkušenosti to snesou bez problémů. Kdyby začaly tvrdnout, ošetřete je krátce kondicionérem nebo maskou na vlasy. Levné přírodní štětce myjte šamponem a po něm vždy krátce kondicionér.'),
         ('Jak vymýt make-up nebo rtěnku z hustého štětce?', 'Kapkou olivového nebo slunečnicového oleje kosmetiku nejdřív rozpusťte a vymyjte, potom štětec domyjte mýdlem. Olej dávejte jen trochu a ne hluboko do štětce.'),
         ('Proč štětcům vypadávají štětiny?', 'Nejčastěji kvůli vodě v lepidle: mokrý štětec držený štětinami nahoru, namáčení, horká voda nebo sušení na slunci a na topení. Všechno ve štětci drží lepidlo.'),
         ('Jak štětce správně sušit?', 'Naplocho na rovném ručníku, s rozestupy a klidně střídavě hlavou k patě. Ne ve vlhké koupelně, ne nad horkým topením a ne na přímém slunci. Přes noc uschnou.'),
         ('Jak zachránit rozčepýřený tenký štětec?', 'Na okamžik ponořte do vroucí vody jen štětiny, ne plastovou část, a stáhnou se zpět. Některé štětce se ale můžou roztavit, takže je to na vlastní riziko.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

# ================================================================= ENGLISH
_FINDER_EN = dict(
    q1='Bristles', q2='Quality',
    fiber=[('natural', 'Natural'), ('synth', 'Synthetic')],
    quality=[('premium', 'Premium'), ('budget', 'Budget')],
    answers=[
        ('natural-premium', 'Natural · premium', 'Bar soap', "Plain bar soap is fine. If the bristles ever start to stiffen, treat them with hair conditioner or a mask to close the hair cuticle. Briefly, not for hours."),
        ('natural-budget', 'Natural · budget', 'Shampoo and conditioner', "Shampoo instead of soap, then a quick conditioner or hair mask. Don't leave them in it long: just while you finish washing the rest."),
        ('synth-premium', 'Synthetic · premium', 'Bar soap, no worries', 'Good synthetics handle soap with no trouble. For cream textures such as foundation or concealer, use a drop of oil first, then soap.'),
        ('synth-budget', 'Synthetic · budget', 'Something gentler', "Cheap brushes fluff out quickly with soap. Reach for a gentle shampoo or a dedicated brush cleanser. That's fine; it just costs more."),
    ])
_TABS_EN = [
    ('round', 'Round brushes', 'circle', 'Circles',
     "<p>Wet the brush and move it over the soap bar in circles. Round brush, round motion. Don't press hard, there's no need. Go gently but properly, so the soap works its way inside and lathers.</p>"
     '<p class="bc-batch"><span>🧼 ×10</span>→<span>💧 ×10</span>→<span>towel</span></p>'
     '<p class="fs-16">I sort brushes into groups: I lather ten medium or small round ones in a row, rinse all ten, then lay them on the towel.</p>'),
    ('flat', 'Flat brushes', 'stroke', 'Strokes and "cat paw"',
     "<p>Never swirl a flat brush. It's bad for the bristles, because you never work with it in circles, only in strokes. So wash it in strokes too. Tap it into the soap like a cat's paw, stroke back and forth, set it down and let it sit for a moment. The makeup loosens while it rests.</p>"),
    ('fine', 'Fine liner brushes', 'gentle', 'Very gently',
     '<p>Their whole value is in the fine bristles that draw precise lines. Squash them while washing and they fluff out and are hard to get back into shape.</p>'
     '<aside class="note"><p class="lbl red">A trick at your own risk</p><p>Dip just the bristles, not the plastic, into boiling water for a moment and they pull back together. Some brushes can melt, though.</p></aside>'),
    ('duo', 'Duo fibre', 'circle', 'Circles',
     "<p>Even though it's a little flattened, you can wash it in circles. That matches its shape and the way you work with it.</p>"),
]

C['en'] = dict(
    toc=[('summary', 'The routine in short'), ('kit', "What you'll need"), ('bristles', 'Natural or synthetic?'), ('rules', 'Three golden rules'),
         ('technique', 'Technique by shape'), ('oil', "Foundation and lipstick that won't wash out"), ('drying', 'Drying'), ('pro-tips', 'Pro tips'),
         ('myths', 'Myth or fact?'), ('verdict', "Dos and don'ts"), ('faq', 'FAQ')],
    opener="Almost nobody loves washing brushes, and makeup artists least of all. But some days I wash fifty or even a hundred of them, so I've built a routine that's fast, cheap and gentle on the bristles. No miracle products and no twenty-minute ritual: a bar of soap, a few rules and the right technique.",
    pre=DEFS,
    summary_h='The routine in short',
    steps=['Antibacterial bar soap, a silicone mat, gloves and a towel', 'Always hold a wet brush tip-down, and never soak it', 'Warm water: not hot, not cold', 'Round brushes in circles, flat ones in strokes only', 'Melt foundation and lipstick with a drop of oil first', 'Wash in batches, say ten at a time', 'Dry flat on a towel, spaced apart', 'Away from a humid bathroom, a hot radiator and direct sun'],
    tested_h='Who it is for',
    tested="<p>I use this routine on my whole kit: for me it isn't one brush but sometimes fifty or a hundred at once. It works for anyone with a few brushes at home who wants them to last for years, and for new makeup artists too. There's no science to washing brushes, just a few rules worth keeping.</p>",
    sections=[
        ('kit', "What you'll need", '''<dl class="rows">
<div><dt class="k">Bar soap</dt><dd class="v">antibacterial and deep-cleansing</dd></div>
<div><dt class="k">Silicone mat</dt><dd class="v">ideally with a ribbed section</dd></div>
<div><dt class="k">Gloves</dt><dd class="v">the same ones you dye your hair in</dd></div>
<div><dt class="k">A flat towel</dt><dd class="v">for drying, even twice as big</dd></div>
<div><dt class="k">Oil</dt><dd class="v">olive or sunflower, for cream textures</dd></div>
<div><dt class="k">Hair conditioner</dt><dd class="v">only for natural bristles that stiffen</dd></div>
</dl>
<p>The soap has to be <b>a bar, not liquid</b>, and properly cleansing. A gentle creamy soap isn't enough. Laundry soap might work, but it's very alkaline and drying, so I don't recommend it. In the Czech Republic I use <b>Protex</b>; in Ukraine, look for <b>Safeguard</b> labelled Deep Clean.</p>
<p>My silicone mat is from AliExpress and it's on its third year. My favourite part is the ribbed section, which gets out dust and built-up pigment. And the gloves I dye my hair in save my hands when it's dozens of brushes.</p>'''),
        ('bristles', 'Natural or synthetic bristles?', '''<p>There are only two kinds of brushes: natural and synthetic. There's no third kind, at most a mix, like duo fibre. I used to wash natural brushes with shampoo, because plain soap makes them stiff, and that's true. But experience taught me one thing: <b>a good, pricier brush handles soap just fine.</b></p>
<p>In a year of using premium brushes from Ukrainian brands I never once needed a mask on them; they never went stiff, whatever I washed them with. Some of the cheap AliExpress brushes I started with, on the other hand, fluff out in half a second, with soap or shampoo. I still use a few of them; the rest sit on the bench.</p>
<p class="lbl red">Pick your brush</p>
''' + finder(_FINDER_EN) + '''
<aside class="note"><p class="lbl red">Why not special cleansers?</p><p>Brush soaps and shampoos work; they just aren't as economical as a plain bar. And express cleansers dry the bristles out, so I keep them for when I really need them. Investing in a good brush pays you back one hundred percent.</p></aside>'''),
        ('rules', 'Three golden rules', '''<p>The technique is simple, but these rules are non-negotiable. Everything in a brush is held together by glue, and that's what we're protecting.</p>
''' + RULE_FIG.format(bad='Bristles up', good='Bristles down') + '''
<ol class="lessons">
<li><span class="n" aria-hidden="true">1</span><div><p><strong>Never hold a wet brush bristles-up.</strong></p><p class="fs-16">Water runs into the glue in the ferrule and softens it over time. The bristles start shedding or the brush falls apart.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><p><strong>Never soak your brushes.</strong></p><p class="fs-16">Don't pile them in the sink or leave them sitting in water. Same reason: the glue.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><p><strong>Warm water only.</strong></p><p class="fs-16">Cold water won't wash the product out; hot water damages the glue.</p></div></li>
</ol>
''' + temp(['Cold', 'Warm ✓', 'Hot'])),
        ('technique', 'Technique by brush shape', '<p>Your washing motion should mirror how you use the brush. Pick a shape:</p>\n' + tabs(_TABS_EN)),
        ('oil', "Foundation or lipstick that won't wash out", '''<p>A dense synthetic brush for cream textures with foundation packed deep inside? Or red lipstick? Cleansing oil or micellar water work too, but my most tried-and-tested method is plain kitchen oil.</p>
''' + oil_steps([('A drop of oil', 'Olive or sunflower. Really just a tiny drop, and not deep into the brush.'),
                 ('Dissolve the product', 'Work the foundation or lipstick out of the brush with the oil.'),
                 ('Finish with soap', 'Soap removes the oil and any leftovers. Rinse, press, done.')]) + '''
<aside class="note"><p class="lbl red">How I found out</p><p>By pure accident. I once ran out of soap, only noticed late at night, and had to leave for work with those brushes in the morning. I washed them out with oil and finished with dish soap. Ever since, I always keep a spare bar on hand.</p></aside>'''),
        ('drying', 'Drying: flat and spaced out', '''<p>After each batch, lay the brushes on a <b>flat towel</b>. Don't stand them up and don't hang them; there's no need. You can press a flat brush lightly into the towel, but don't squeeze it. Space them out, alternating head-to-toe so the bristles don't touch. They dry overnight.</p>
''' + TOWEL.format(alt='Brushes laid head-to-toe on a towel', cap="Head-to-toe, so the bristles don't touch.") + '''
<p class="lbl red">Where should the towel go? Tap to check:</p>
''' + spots([('🛁', 'The bathroom', 'bc-no', 'Better not: bathrooms are usually humid. I fold the towel carefully and carry it to my room.'),
             ('🔥', 'A sill above the radiator', 'bc-warn', 'Careful: a hot radiator under the window can overdry the bristles. Put them on a table instead.'),
             ('🪴', 'A table in a room', 'bc-ok', 'Perfect. A dry room with no direct heat, and everything is dry by morning.'),
             ('☀️', 'A sunny window', 'bc-no', 'No. In summer the handle heats up in direct sun and the glue can come loose.')])),
        ('pro-tips', 'Pro tips from the job', '''<h3>Express cleanser for dry textures only</h3>
<p>When I have clients back to back, I use an express cleanser, but only on eyeshadow brushes. I never clean cream textures with it: it's too much hassle and it dries the bristles. It's easier to simply own more brushes.</p>
<h3>Clean gel liner off straight away</h3>
<p>Don't let gel liner dry on the brush. It dries the brush out and twists the bristles.</p>
<h3>From experience: which brushes to start with</h3>
<p>If you're only building your kit, a few good brushes are worth more than a box of cheap ones. We go through choosing the ones that really suit you in my <a href="/en/courses/">one-on-one makeup courses</a>.</p>'''),
        ('myths', 'Myth or fact?', '<p>Make your guess, then tap.</p>\n' + myths([
            ('Soaking brushes in water helps loosen makeup.', 'Myth or fact?', 'v-sw', 'Myth', 'Water gets into the ferrule glue and the brush falls apart over time.'),
            ('A good natural brush can be washed with plain bar soap.', 'Myth or fact?', 'v-yes', 'Fact', 'Good brushes cope fine. If they ever stiffen, a short conditioner treatment helps.'),
            ('The hotter the water, the cleaner the brush.', 'Myth or fact?', 'v-sw', 'Myth', 'Hot water damages the glue. Warm is ideal.'),
            ('Brushes dry best hanging up.', 'Myth or fact?', 'v-sw', 'Myth', 'No need. Flat on a towel, spaced out, overnight is all it takes.')])),
    ],
    verdict_h="Dos and don'ts",
    verdict=[('Do', 'vtag v-yes', ['Antibacterial bar soap', 'Round in circles, flat in strokes', 'Oil for foundation and lipstick', 'Dry flat on a towel', 'Clean gel liner off straight away']),
             ('With care', 'vtag v-dep', ['Shampoo and conditioner for budget natural brushes', 'Express cleanser on dry textures only', 'Boiling water for fine brushes', 'Laundry soap (drying)']),
             ('Never', 'vtag v-sw', ['A wet brush bristles-up', 'Soaking in the sink', 'Hot water', 'Drying on a radiator or in the sun', 'Swirling a flat brush'])],
    verdict_foot='',
    lessons_h='Three things to take away',
    lessons=[('Glue holds everything together.', 'Bristles down, no soaking, no hot water and no radiator. That way a brush lasts for years.'),
             ('Wash the way you apply.', 'You use a round brush in circles, so wash it in circles. A flat one only in strokes, never swirled.'),
             ('A good brush is an investment.', 'A quality brush copes with plain soap and needs no pricey care. A cheap one fluffs out whatever you use.')],
    learn_h='Want to know which brushes are worth it?',
    cta_note="In a <a href=\"/en/courses/\">one-on-one makeup course</a> we go through your brushes and products and work out what's worth keeping and how to look after it.",
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Professional makeup in Prague',
    cta_text='Every client gets clean brushes washed exactly this way: for weddings, shoots and evening events.',
    cta_links=[('Wedding makeup', '/en/wedding/'), ('Evening makeup', '/en/evening-makeup/')],
    faq_h='Frequently asked questions',
    faq=[('What should I wash makeup brushes with?', 'An antibacterial, deep-cleansing bar soap, such as Protex or Safeguard Deep Clean. A gentle creamy soap isn\'t enough and laundry soap is drying. Wash cheap brushes that fluff out with soap in a gentler shampoo instead.'),
         ('Can I wash natural-hair brushes with soap?', 'Good ones, yes: in my experience they cope fine. If they start to stiffen, give them a short conditioner or hair mask treatment. Wash budget natural brushes with shampoo, always followed by a quick conditioner.'),
         ('How do I get foundation or lipstick out of a dense brush?', 'Dissolve and work out the product with a drop of olive or sunflower oil first, then finish with soap. Use only a little oil and keep it out of the base of the brush.'),
         ('Why are my brushes shedding?', 'Usually because water got into the glue: a wet brush held bristles-up, soaking, hot water, or drying in the sun or on a radiator. Everything in a brush is held together by glue.'),
         ('How should I dry makeup brushes?', 'Flat on a towel, spaced out and alternating head-to-toe. Not in a humid bathroom, not above a hot radiator and not in direct sun. They dry overnight.'),
         ('How do I fix a fluffed-out liner brush?', 'Dip just the bristles, not the plastic part, into boiling water for a moment and they pull back together. Some brushes can melt, though, so it\'s at your own risk.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

EXTRA = dict(products=[], brands=BRANDS, about=('Mytí štětců na make-up', 'Washing makeup brushes'),
             video_name='Як правильно мити пензлики')
