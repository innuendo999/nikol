"""Article: how I wash makeup brushes (video gc_bq04a_G0).

Editorial line illustrations as inline SVG (brush symbols defined once in DEFS). Motion is SMIL along drawn
guide paths, paused off-screen and under reduced motion by site.js; reveal states (.bc-*) live in site.css.
The bristle finder and technique tabs are enhanced in site.js; everything reads without JS."""

BRANDS = ['Protex', 'Safeguard']

INK, OX, RED, PINK, BLUSH, PAPER, LINE, WATER = '#171213', '#3E1016', '#A8232F', '#F4B9AE', '#F5E4DF', '#FBF7F5', '#D7BDB6', '#6F97B8'
_S = f'stroke="{INK}" stroke-width="1.1" vector-effect="non-scaling-stroke"'
_T = 'stroke-width=".7" vector-effect="non-scaling-stroke" fill="none"'
_FERRULE = lambda x, y, w, h: (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="{PAPER}" {_S}/>'
                               f'<path d="M{x} {y + 7}h{w}M{x} {y + h - 7}h{w}" stroke="{INK}" stroke-opacity=".45" {_T}/>')

# ---------------------------------------------------------------- shared SVG (line art, bristles up, 60 x 220)
DEFS = f'''<svg class="visually-hidden" aria-hidden="true" focusable="false"><defs>
<symbol id="bc-round" viewBox="0 0 60 220"><path d="M14 74C9 46 15 14 30 8c15 6 21 38 16 66z" fill="#E7D2C3" {_S}/><path d="M22 70C20 50 23 28 29 14M30 72V12M38 70c2-20-1-42-7-56" stroke="#8C6E62" stroke-opacity=".7" {_T}/>{_FERRULE(14, 72, 32, 38)}<path d="M16 110h28l-6 104q-8 5-16 0z" fill="{OX}"/></symbol>
<symbol id="bc-flat" viewBox="0 0 60 220"><path d="M14 74l1-46q15-20 30 0l1 46z" fill="#2E2627" {_S}/><path d="M22 70V30M30 70V22M38 70V30" stroke="#8A7B78" stroke-opacity=".8" {_T}/>{_FERRULE(14, 72, 32, 40)}<path d="M17 112h26l-5 102q-8 5-16 0z" fill="{RED}"/></symbol>
<symbol id="bc-fine" viewBox="0 0 60 220"><path d="M26 74q-2-34 4-70 6 36 4 70z" fill="#2E2627" {_S}/>{_FERRULE(25, 72, 10, 50)}<path d="M25.5 122h9l-2.5 92q-2 4-4 0z" fill="{OX}"/></symbol>
<symbol id="bc-duo" viewBox="0 0 60 220"><path d="M12 74c-2-26 2-48 18-52 16 4 20 26 18 52z" fill="#2E2627" {_S}/><path d="M14.5 42c2-12 7-18 15.5-20 8.5 2 13.5 8 15.5 20-9-4-22-4-31 0z" fill="{PAPER}" {_S}/>{_FERRULE(12, 72, 36, 36)}<path d="M15 108h30l-7 106q-8 5-16 0z" fill="#E3A497"/></symbol>
<symbol id="bc-bar" viewBox="0 0 200 62"><rect x="2" y="2" width="196" height="56" rx="20" fill="#fff" {_S}/></symbol>
</defs></svg>'''

PATHS = {'circle': ('M40 0a40 9 0 1 1-80 0a40 9 0 1 1 80 0', '2.8s', 172),
         'pat': ('M-38 0Q-19-18 0 0Q19-18 38 0Q19-18 0 0Q-19-18-38 0', '2.6s', 180),
         'gentle': ('M-12 0L12 0L-12 0', '5s', 166)}


def brush_down(sym, w, tilt=180):
    """A brush pointing down with its tip at (0,0)."""
    h = w * 220 / 60
    tip = 6 * w / 60
    return f'<g transform="rotate({tilt})"><use href="#bc-{sym}" x="{-w / 2}" y="{-tip}" width="{w}" height="{h}"/></g>'


def stage(brush, kind):
    """Washing demo: the brush tip follows a dashed guide (its real working motion) over a bar of soap."""
    p, dur, tilt = PATHS[kind]
    return (f'<svg class="bc-stage" viewBox="0 0 400 280" data-anim aria-hidden="true">'
            f'<ellipse cx="200" cy="262" rx="110" ry="5" fill="#E9D4CE"/>'
            f'<use href="#bc-bar" x="110" y="198" width="180" height="56"/>'
            f'<g transform="translate(200 206)"><path d="{p}" fill="none" stroke="{RED}" stroke-width="1" stroke-dasharray="2 5" vector-effect="non-scaling-stroke"/>'
            f'<g><animateMotion dur="{dur}" repeatCount="indefinite" path="{p}" calcMode="paced"/>{brush_down(brush, 44, tilt)}</g></g></svg>')


def rule_fig(bad, good):
    return f'''<div class="bc-compare">
<figure class="bc-panel"><svg viewBox="0 0 160 240" data-anim aria-hidden="true"><use href="#bc-round" x="50" y="12" width="60" height="220"/>
<rect x="64" y="84" width="32" height="38" rx="1.5" fill="none" stroke="{RED}" stroke-width="2" vector-effect="non-scaling-stroke" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;.45;.65;.9;1" dur="3.2s" repeatCount="indefinite"/></rect>
<path d="M82 18C93 30 97 56 91 84L88 104" fill="none" stroke="{WATER}" stroke-width="2" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"><animate attributeName="stroke-dashoffset" values="1;0;0;1" keyTimes="0;.55;.9;1" dur="3.2s" repeatCount="indefinite"/></path>
</svg><figcaption><span class="lbl red">01 · {bad[0]}</span><span>{bad[1]}</span></figcaption></figure>
<figure class="bc-panel"><svg viewBox="0 0 160 240" data-anim aria-hidden="true"><g transform="translate(160 240) rotate(180)"><use href="#bc-round" x="50" y="12" width="60" height="220"/></g>
<path d="M88 126C94 158 93 196 80 222" fill="none" stroke="{WATER}" stroke-width="2" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"><animate attributeName="stroke-dashoffset" values="1;0;0;1" keyTimes="0;.5;.9;1" dur="3.2s" repeatCount="indefinite"/></path>
<circle cx="80" cy="226" r="2.6" fill="{WATER}" opacity="0"><animate attributeName="cy" values="226;226;238" keyTimes="0;.5;1" dur="3.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0;1;0" keyTimes="0;.5;.6;1" dur="3.2s" repeatCount="indefinite"/></circle>
</svg><figcaption><span class="lbl">02 · {good[0]}</span><span>{good[1]}</span></figcaption></figure>
</div>'''


def towel(alt, cap):
    types = ['round', 'flat', 'duo', 'fine', 'round', 'duo', 'flat', 'fine', 'round']
    rows = []
    for k, sym in enumerate(types):
        r, c = divmod(k, 3)
        cx, y = 110 + c * 150, 78 + r * 72
        rot = -90 if (r + c) % 2 == 0 else 90
        rows.append((sym, cx - 51 if rot == -90 else cx + 51, y, rot))
    g = ''.join(f'<g class="bc-lay d{min(i, 7)}"><g transform="translate({x} {y}) rotate({r})"><use href="#bc-{s}" x="-14" width="28" height="103"/></g></g>'
                for i, (s, x, y, r) in enumerate(rows))
    return (f'<figure class="bc-towel" data-reveal><svg viewBox="0 0 520 300" role="img" aria-label="{alt}">'
            f'<rect x="1" y="1" width="518" height="298" fill="{PAPER}" {_S}/><path d="M1 26h518M1 32h518M1 268h518M1 274h518" stroke="{LINE}" {_T}/>'
            f'{g}</svg><figcaption class="fine-print">{cap}</figcaption></figure>')


OIL_SVG = [
    f'<svg viewBox="0 0 200 150" data-anim aria-hidden="true"><path d="M92 8h16v10l8 10v32a4 4 0 0 1-4 4H88a4 4 0 0 1-4-4V28l8-10z" fill="{PAPER}" {_S}/><path d="M85 40h30v20a3 3 0 0 1-3 3H88a3 3 0 0 1-3-3z" fill="#E8C97A"/><rect x="90" y="3" width="20" height="7" rx="1" fill="{OX}"/>'
    f'<circle cx="100" cy="70" r="3" fill="#D9AE4E"><animate attributeName="cy" values="68;68;112" keyTimes="0;.3;1" dur="2.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.3;.92;1" dur="2.6s" repeatCount="indefinite"/></circle>'
    f'<use href="#bc-flat" x="86" y="112" width="28" height="103"/></svg>',
    f'<svg viewBox="0 0 200 150" data-anim aria-hidden="true"><ellipse cx="100" cy="128" rx="62" ry="10" fill="#fff" {_S}/><ellipse cx="100" cy="128" rx="34" ry="5" fill="{RED}"><animate attributeName="opacity" values="1;.15;1" dur="4s" repeatCount="indefinite"/></ellipse>'
    f'<g transform="translate(100 124)"><g><animateMotion dur="2.6s" repeatCount="indefinite" path="{PATHS["pat"][0]}" calcMode="paced"/>{brush_down("flat", 30)}</g></g></svg>',
    f'<svg viewBox="0 0 200 150" data-anim aria-hidden="true"><use href="#bc-bar" x="45" y="104" width="110" height="34"/>'
    f'<g transform="translate(100 110)"><path d="M26 0a26 6 0 1 1-52 0a26 6 0 1 1 52 0" fill="none" stroke="{RED}" stroke-width="1" stroke-dasharray="2 5" vector-effect="non-scaling-stroke"/><g><animateMotion dur="2.6s" repeatCount="indefinite" path="M26 0a26 6 0 1 1-52 0a26 6 0 1 1 52 0" calcMode="paced"/>{brush_down("round", 30, 172)}</g></g></svg>',
]


def finder(L):
    """Bristle × quality picker. Without JS every answer is listed; with JS only the selected one shows."""
    pills = lambda name, opts: ''.join(
        f'<label class="bc-pill"><input type="radio" name="{name}" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>'
        for i, (v, t) in enumerate(opts))
    ans = ''.join(f'<div class="bc-ans" data-ans="{k}"><p class="lbl">{lab}</p><p class="bc-ans-h">{h}</p><p>{b}</p></div>' for k, lab, h, b in L['answers'])
    return f'''<div class="bc-finder" data-finder>
<div class="bc-q"><fieldset><legend class="lbl">{L['q1']}</legend>{pills('bc-fiber', L['fiber'])}</fieldset>
<fieldset><legend class="lbl">{L['q2']}</legend>{pills('bc-quality', L['quality'])}</fieldset></div>
<div class="bc-a" aria-live="polite">{ans}</div>
</div>'''


def tabs(L):
    """Technique by brush shape. Without JS the panes are stacked with their own h3."""
    btns = ''.join(f'<button type="button" role="tab" data-tab="{k}">{name}</button>' for k, name, *_ in L)
    panes = ''.join(f'<div class="bc-pane" data-pane="{k}" role="tabpanel"><div class="bc-stage-wrap">{stage(k, motion)}<span class="bc-motion lbl red">{tag}</span></div><div class="bc-pane-text"><h3>{name}</h3>{body}</div></div>'
                    for k, name, motion, tag, body in L)
    return f'<div class="bc-tabs" data-tabs><div class="bc-tablist" role="tablist" hidden>{btns}</div>{panes}</div>'


def flow(items):
    return '<ol class="bc-flow">' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'


def oil_steps(items):
    return '<ol class="bc-steps">' + ''.join(f'<li>{OIL_SVG[i]}<p class="bc-n">0{i + 1}</p><p><strong>{h}</strong></p><p class="fs-16">{b}</p></li>' for i, (h, b) in enumerate(items)) + '</ol>'


def rows(items, title_cls=''):
    """Expandable rows (like the FAQ): spots to dry and myth/fact statements."""
    return '<div class="bc-rows">' + ''.join(f'<details><summary><span class="{title_cls}">{q}</span><span class="pm" aria-hidden="true">+</span></summary><p><span class="vtag {cls}">{lab}</span>{a}</p></details>' for q, cls, lab, a in items) + '</div>'


def temp(lbls):
    return '<div class="bc-temp" data-reveal aria-hidden="true"><div class="bc-temp-bar"><span class="bc-temp-mark"></span></div><div class="bc-temp-lbl">' + ''.join(f'<span>{x}</span>' for x in lbls) + '</div></div>'


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
     '<p>Navlhčete štětec a krouživými pohyby přejíždějte po kostce mýdla. Štětec je kulatý, tak i pohyb je kulatý. Netlačte, není to potřeba. Stačí lehce, ale pořádně, aby se mýdlo dostalo dovnitř a napěnilo.</p>' +
     flow(['10 × namydlit', '10 × opláchnout', 'na ručník']) +
     '<p class="fs-16">Štětce třídím do skupin: namydlím deset středních nebo malých kulatých za sebou, pak všech deset opláchnu a odložím na ručník.</p>'),
    ('flat', 'Ploché štětce', 'pat', 'Tahy a „kočičí tlapka“',
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
''' + rule_fig(('Špatně', 'Voda steče do lepidla v objímce.'), ('Správně', 'Voda odteče špičkou ven.')) + '''
<ol class="lessons">
<li><span class="n" aria-hidden="true">1</span><div><p><strong>Mokrý štětec nikdy nedržte štětinami nahoru.</strong></p><p class="fs-16">Voda steče do lepidla v objímce a to se časem rozmočí. Štětiny začnou vypadávat nebo se štětec rozpadne.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><p><strong>Štětce nenamáčejte.</strong></p><p class="fs-16">Nedávejte je všechny do umyvadla a nenechávejte je ležet ve vodě. Důvod je stejný: lepidlo.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><p><strong>Jen vlažná voda.</strong></p><p class="fs-16">Ve studené se kosmetika nevymyje, horká škodí lepidlu.</p></div></li>
</ol>
''' + temp(['Studená', 'Vlažná', 'Horká'])),
        ('technika', 'Technika podle tvaru štětce', '<p>Pohyb při mytí kopíruje pohyb, kterým štětcem pracujete. Vyberte tvar:</p>\n' + tabs(_TABS_CS)),
        ('olej', 'Make-up nebo rtěnka, které nejdou vymýt', '''<p>Hustý syntetický štětec na krémové textury, ve kterém se make-up usadí hluboko uvnitř? Nebo červená rtěnka? Hydrofilní olej nebo micelárka fungují taky, ale nejověřenější je u mě obyčejný olej z kuchyně.</p>
''' + oil_steps([('Kapka oleje', 'Olivový nebo slunečnicový. Opravdu jen kapička a ne hluboko do štětce.'),
                 ('Rozpusťte kosmetiku', 'Olejem z štětce vymyjte make-up nebo rtěnku.'),
                 ('Domyjte mýdlem', 'Mýdlo odstraní olej i zbytky. Opláchnout, otisknout, hotovo.')]) + '''
<aside class="note"><p class="lbl red">Jak jsem na to přišla</p><p>Úplnou náhodou. Jednou mi došlo mýdlo, zjistila jsem to až pozdě večer a ráno jsem se štětci musela do práce. Vymyla jsem je olejem a domyla prostředkem na nádobí. Od té doby mám kostku mýdla vždycky v záloze.</p></aside>'''),
        ('suseni', 'Sušení: naplocho a s rozestupy', '''<p>Po každé dávce štětce položte na <b>rovný ručník</b>. Nestavte je do stojánku a nevěšte je, není to potřeba. Plochý štětec můžete ještě lehce otisknout do ručníku, ale nemačkejte ho. Rozložte je s rozestupy, klidně střídavě hlavou k patě, aby se štětiny nedotýkaly. Přes noc uschnou.</p>
''' + towel(alt='Štětce rozložené na ručníku střídavě hlavou k patě', cap='Střídavě hlavou k patě, aby se štětiny nedotýkaly.') + '''
<p class="lbl red">Kam ručník se štětci odnést?</p>
''' + rows([('Koupelna', 'v-sw', 'Ne', 'V koupelně bývá vlhko. Ručník opatrně složím a odnesu do pokoje.'),
             ('Parapet nad topením', 'v-dep', 'Pozor', 'Horký radiátor pod oknem může štětiny přesušit. Raději je dejte na stůl.'),
             ('Stůl v pokoji', 'v-yes', 'Ano', 'Suchý pokoj bez přímého tepla, do rána všechno uschne.'),
             ('Okno na slunci', 'v-sw', 'Ne', 'V létě se rukojeť na přímém slunci zahřeje a lepidlo může povolit.')])),
        ('praxe', 'Tipy z praxe', '''<h3>Expresní čistič jen na suché textury</h3>
<p>Když mám klientky za sebou, používám expresní čistič, ale jen na štětce na stíny. Krémové textury jím nikdy nečistím: je to moc práce a vysušuje štětiny. Jednodušší je mít prostě víc štětců.</p>
<h3>Gelové linky smyjte hned</h3>
<p>Nenechávejte gelovou linku zaschnout na štětci. Vysuší ho a štětiny se zkroutí.</p>
<h3>Ze zkušenosti: s jakými štětci začít</h3>
<p>Pokud si teprve skládáte kufr, víc se vyplatí pár kvalitních štětců než krabice levných. Jak vybrat ty, které vám opravdu sednou, procházíme na <a href="/kurzy-liceni/">individuálním kurzu líčení</a>.</p>'''),
        ('myty', 'Mýtus, nebo fakt?', '<p>Tipněte si a rozklikněte.</p>\n' + rows([
            ('Štětce je dobré nechat odmočit ve vodě.', 'v-sw', 'Mýtus', 'Voda se dostane do lepidla v objímce a štětec se časem rozpadne.'),
            ('Kvalitní přírodní štětec můžete mýt obyčejným mýdlem.', 'v-yes', 'Fakt', 'Dobré štětce to snesou. Kdyby přece jen ztvrdly, pomůže krátce kondicionér.'),
            ('Čím teplejší voda, tím čistší štětec.', 'v-sw', 'Mýtus', 'Horká voda škodí lepidlu. Ideální je vlažná.'),
            ('Štětce nejlépe uschnou zavěšené.', 'v-sw', 'Mýtus', 'Není to potřeba. Naplocho na ručníku s rozestupy přes noc úplně stačí.')], 'serif')),
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
     "<p>Wet the brush and move it over the soap bar in circles. Round brush, round motion. Don't press hard, there's no need. Go gently but properly, so the soap works its way inside and lathers.</p>" +
     flow(['Lather 10', 'Rinse 10', 'Onto the towel']) +
     '<p class="fs-16">I sort brushes into groups: I lather ten medium or small round ones in a row, rinse all ten, then lay them on the towel.</p>'),
    ('flat', 'Flat brushes', 'pat', 'Strokes and "cat paw"',
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
''' + rule_fig(('Wrong', 'Water runs into the ferrule glue.'), ('Right', 'Water runs off the tip.')) + '''
<ol class="lessons">
<li><span class="n" aria-hidden="true">1</span><div><p><strong>Never hold a wet brush bristles-up.</strong></p><p class="fs-16">Water runs into the glue in the ferrule and softens it over time. The bristles start shedding or the brush falls apart.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><p><strong>Never soak your brushes.</strong></p><p class="fs-16">Don't pile them in the sink or leave them sitting in water. Same reason: the glue.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><p><strong>Warm water only.</strong></p><p class="fs-16">Cold water won't wash the product out; hot water damages the glue.</p></div></li>
</ol>
''' + temp(['Cold', 'Warm', 'Hot'])),
        ('technique', 'Technique by brush shape', '<p>Your washing motion should mirror how you use the brush. Pick a shape:</p>\n' + tabs(_TABS_EN)),
        ('oil', "Foundation or lipstick that won't wash out", '''<p>A dense synthetic brush for cream textures with foundation packed deep inside? Or red lipstick? Cleansing oil or micellar water work too, but my most tried-and-tested method is plain kitchen oil.</p>
''' + oil_steps([('A drop of oil', 'Olive or sunflower. Really just a tiny drop, and not deep into the brush.'),
                 ('Dissolve the product', 'Work the foundation or lipstick out of the brush with the oil.'),
                 ('Finish with soap', 'Soap removes the oil and any leftovers. Rinse, press, done.')]) + '''
<aside class="note"><p class="lbl red">How I found out</p><p>By pure accident. I once ran out of soap, only noticed late at night, and had to leave for work with those brushes in the morning. I washed them out with oil and finished with dish soap. Ever since, I always keep a spare bar on hand.</p></aside>'''),
        ('drying', 'Drying: flat and spaced out', '''<p>After each batch, lay the brushes on a <b>flat towel</b>. Don't stand them up and don't hang them; there's no need. You can press a flat brush lightly into the towel, but don't squeeze it. Space them out, alternating head-to-toe so the bristles don't touch. They dry overnight.</p>
''' + towel(alt='Brushes laid head-to-toe on a towel', cap="Head-to-toe, so the bristles don't touch.") + '''
<p class="lbl red">Where should the towel go?</p>
''' + rows([('The bathroom', 'v-sw', 'No', 'Bathrooms are usually humid. I fold the towel carefully and carry it to my room.'),
             ('A sill above the radiator', 'v-dep', 'Careful', 'A hot radiator under the window can overdry the bristles. Put them on a table instead.'),
             ('A table in a room', 'v-yes', 'Yes', 'A dry room with no direct heat, and everything is dry by morning.'),
             ('A sunny window', 'v-sw', 'No', 'In summer the handle heats up in direct sun and the glue can come loose.')])),
        ('pro-tips', 'Pro tips from the job', '''<h3>Express cleanser for dry textures only</h3>
<p>When I have clients back to back, I use an express cleanser, but only on eyeshadow brushes. I never clean cream textures with it: it's too much hassle and it dries the bristles. It's easier to simply own more brushes.</p>
<h3>Clean gel liner off straight away</h3>
<p>Don't let gel liner dry on the brush. It dries the brush out and twists the bristles.</p>
<h3>From experience: which brushes to start with</h3>
<p>If you're only building your kit, a few good brushes are worth more than a box of cheap ones. We go through choosing the ones that really suit you in my <a href="/en/courses/">one-on-one makeup courses</a>.</p>'''),
        ('myths', 'Myth or fact?', '<p>Make your guess, then tap.</p>\n' + rows([
            ('Soaking brushes in water helps loosen makeup.', 'v-sw', 'Myth', 'Water gets into the ferrule glue and the brush falls apart over time.'),
            ('A good natural brush can be washed with plain bar soap.', 'v-yes', 'Fact', 'Good brushes cope fine. If they ever stiffen, a short conditioner treatment helps.'),
            ('The hotter the water, the cleaner the brush.', 'v-sw', 'Myth', 'Hot water damages the glue. Warm is ideal.'),
            ('Brushes dry best hanging up.', 'v-sw', 'Myth', 'No need. Flat on a towel, spaced out, overnight is all it takes.')], 'serif')),
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
