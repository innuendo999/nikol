"""Article (how-to): transition blush explained, its history and how to do it with what you already own (video qIsRGQgTsOk).

Interactive parts (readable without JS; site.js / site.css .tb-* plus the shared .tg-* guide):
- step guide on a real portfolio photo with zones; Kevyn Aucoin / + Paint By Ester / + evening top-up switch
- concealer + blush mixer that builds the transition gradient, brush softness slider, face-shape picker, history timeline."""
from post_travel import guide, ZONES as TRAVEL_ZONES, DEFS

BRANDS = ['Kevyn Aucoin', 'Patrick Ta', 'Fenty Beauty', 'Dior']

# zones on the portfolio photo (coordinates of the original 800x800 nude-1 photo, see post_travel)
ZONES = {k: TRAVEL_ZONES[k] for k in ('face', 'under', 'outer', 'lids', 'lips', 'cheeks')}
ZONES.update({
    'inner': '<path d="M350 314q14 2 22 10l-10 48q-14-6-24-20z"/><path d="M496 318q-14 2-22 10l10 48q14-6 24-20z"/>',
    'cheekbone': '<ellipse cx="275" cy="386" rx="64" ry="26" transform="rotate(-18 275 386)"/><ellipse cx="566" cy="396" rx="60" ry="25" transform="rotate(18 566 396)"/>',
    'nose': '<path d="M398 300h40l8 160h-56z"/>',
})

CONCEALER = '#EFD5C3'
BLUSHES = [('#C98BB0', 'lila'), ('#D8577E', 'pink'), ('#E07A5F', 'coral')]


def _mix(a, b, t):
    a, b = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x + (y - x) * t):02X}' for x, y in zip(a, b))


def _ratio(i, n, L):
    from math import gcd
    if i == 0:
        return L['con']
    if i == n - 1:
        return L['blush']
    c, b = n - 1 - i, i
    g = gcd(c, b)
    return f'{c // g} : {b // g}'


def strip(color, n, L):
    w = 600 / n
    out = ''
    for i in range(n):
        t = i / (n - 1)
        out += (f'<rect x="{i * w + 3:.1f}" y="4" width="{w - 6:.1f}" height="84" rx="2" fill="{_mix(CONCEALER, color, t)}"/>'
                f'<text x="{i * w + w / 2:.1f}" y="114" text-anchor="middle">{_ratio(i, n, L)}</text>')
    return out


def mixer(L):
    sw = ''.join(f'<label class="bc-pill tb-sw"><input type="radio" name="tb-blush" value="{c}"{" checked" if i == 0 else ""}><span><svg viewBox="0 0 10 10" aria-hidden="true"><circle cx="5" cy="5" r="5" fill="{c}"/></svg>{L["names"][k]}</span></label>'
                 for i, (c, k) in enumerate(BLUSHES))
    return f'''<figure class="tb-mix" data-mix data-con="{CONCEALER}" data-l-con="{L['con']}" data-l-blush="{L['blush']}">
<div class="tb-mix-ui"><fieldset><legend class="lbl">{L['q1']}</legend>{sw}</fieldset>
<label class="tb-steps-n"><span class="lbl">{L['q2']}</span><input type="range" min="3" max="7" value="5" aria-label="{L['q2']}"><output class="lbl red">5</output></label></div>
<svg class="tb-strip" viewBox="0 0 600 122" role="img" aria-label="{L['aria']}">{strip(BLUSHES[0][0], 5, L)}</svg>
<figcaption class="fine-print">{L['cap']}</figcaption></figure>'''


def brush_demo(L):
    return f'''<figure class="tb-brush" data-blur>
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><filter id="tb-soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter></defs>
<rect width="320" height="150" fill="#EFD5C3"/><ellipse cx="160" cy="75" rx="80" ry="36" fill="#D8577E" fill-opacity=".75" filter="url(#tb-soft)" transform="rotate(-12 160 75)"/></svg>
<div class="tg-sponge-ui"><span class="lbl">{L[0]}</span><input type="range" min="0" max="100" value="0" aria-label="{L[2]}"><span class="lbl">{L[1]}</span></div>
<figcaption class="fine-print" data-out data-a="{L[3]}" data-b="{L[4]}">{L[3]}</figcaption></figure>'''


def timeline(items):
    lis = ''.join(f'<li class="d{i}"><span class="tb-dot" aria-hidden="true"></span><p class="lbl red">{a}</p><p class="tb-t-h">{b}</p><p class="fs-16">{c}</p></li>' for i, (a, b, c) in enumerate(items))
    return f'<ol class="tb-time" data-reveal>{lis}</ol>'


def picker(L):
    pills = ''.join(f'<label class="bc-pill"><input type="radio" name="tb-face" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(L['opts']))
    ans = ''.join(f'<div class="bc-ans" data-ans="{k}"><p class="lbl">{lab}</p><p class="bc-ans-h">{h}</p><p>{b}</p></div>' for k, lab, h, b in L['answers'])
    return f'<div class="bc-finder" data-finder><div class="bc-q"><fieldset><legend class="lbl">{L["q"]}</legend>{pills}</fieldset></div><div class="bc-a" aria-live="polite">{ans}</div></div>'


# ================================================================= CZECH
_P = lambda *n: ' · '.join(n)
STEPS_CS = [
    (['cheekbone'], 'base', 'Namíchejte odstíny', _P('Dvě tvářenky', 'nejsvětlejší korektor'),
     '<p>Nejdřív smíchám nejsvětlejší tvářenky, aby vznikl jemný přechodový odstín, u mě krásně lila. Pak zvlášť namíchám ty nejtmavší: to budou hlavní tvářenky. Celé to jde udělat i s jedinou tvářenkou. Na obličeji mám zatím jen make-up a trochu bronzeru, žádný korektor.</p>'),
    (['inner'], 'base', 'Světlý odstín k vnitřnímu koutku', _P('Světlý lila-růžový mix'),
     '<p>Světlejší lila-růžový odstín dám do úplně vnitřního koutku oka a lehce ho rozmažu směrem dolů. Pod záhyb ho nedávám, není to potřeba. Snažím se ho nanést rovnou rozmazaný, abych nemusela nic dotírat.</p>'),
    (['cheekbone'], 'base', 'Tmavší odstín na lícní kost', _P('Tmavší tvářenka', 'štětec'),
     '<p>Na štětec naberu tmavší odstín a nanesu ho na vystouplou část lícní kosti, ne na „jablíčko“. Jdu až těsně pod oko, ale oblast pod okem vynechám, a kousek ven do strany. Čím výš ho vytáhnu, tím víc vizuálně rozšiřuji obličej; ze strany to dává lehký liftingový efekt.</p>'),
    (['nose'], 'base', 'Zbytek na nos', _P('Zbytek tmavší tvářenky'),
     '<p>Se zbytkem produktu můžete přejet nos a zbytek rozmazat do stran. Je to volitelné.</p>'),
    (['cheekbone'], 'base', 'Světlým odstínem přes okraje', _P('Světlý mix'),
     '<p>Vrátím se ke světlejšímu odstínu a přejedu jím okraje, aby se tmavší a světlejší odstín propojily. Podle techniky Kevyna Aucoina můžete tady skončit; on by do oblasti pod okem použil méně jasný korektor.</p><aside class="note"><p class="lbl red">Tip vizážistky</p><p>Okraje vždycky rozmažte, aby tvářenka nevypadala jako skvrna. Když je to moc, vraťte se ke světlejšímu odstínu a rozmažte ho.</p></aside>'),
    (['cheekbone', 'cheeks'], 'opt', 'Velký nadýchaný štětec', _P('Velký nadýchaný štětec', 'tvářenka'),
     '<p>Paint By Ester bere velmi velký, nadýchaný štětec a produkt nabírá opatrně. Nejdřív jím rozprostře tvářenku co nejšířeji, takže první vrstva je méně sytá a rovnou rozmazaná. Když jsem to zkusila, říkala jsem si: geniální. Velký štětec roztírá měkčeji. S hodně hustým štětcem to tak hezky nevypadá.</p>'),
    (['under'], 'opt', 'Korektor s tvářenkou na kruhy', _P('Korektor smíchaný s tvářenkou'),
     '<p>Korektorem smíchaným s tvářenkou překryji kruhy pod očima. Do celého trojúhelníku pod okem jít nemusíte. Mám spíš oválný obličej a ne moc plné tváře, takže mi víc sluší, když tam nemám rozjasnění navíc, jen tam, kde je stín.</p>'),
    (['outer'], 'opt', 'Začistit linky', _P('Zbytek korektoru'),
     '<p>Stejně tak zbytkem produktu začistím linky, opatrně, ať nic nerozmažu. Vizuálně je to ještě víc protáhne. Když máte pocit, že jste to přehnali, přejeďte okraje trochou světlého korektoru.</p>'),
    (['face', 'nose'], 'opt', 'Zafixovat pudrem', _P('Fenty Beauty pudr, světlý lila'),
     '<p>Paint By Ester všechno zafixuje pudrem. Já mám od Fenty lila, světlý, protože dnes používám tenhle odstín. Baking můžete udělat, ale s dnešním make-upem ho nepotřebuji. Ráda přejedu i hřbet nosu, abych ho trochu zvýraznila.</p>'),
    (['cheekbone'], 'eve', 'Top-up výraznou tvářenkou', _P('Výrazná tvářenka', 'velký štětec'),
     '<p>Když vám to nestačí, naberte velkým štětcem výraznou tvářenku a zvýrazněte místa, kam chcete přitáhnout pozornost: jako masku, nebo jako já na lícní kosti, abych protáhla obličej. Ostrý přechod nevznikne, protože pod tím už je podklad od barvy pleti přes nejsvětlejší růžovou až po hodně sytou.</p>'),
    (['lips', 'lids'], 'eve', 'Barva na rty a oči', _P('Nejtmavší tvářenka'),
     '<p>Nejtmavší tvářenku dám i na rty a trochu na oči, aby všechno ladilo dohromady.</p>'),
    (['cheekbone', 'cheeks'], 'eve', 'Když je to moc', _P('Čistá houbička', 'váš make-up'),
     '<p>Když vám večerní verze pro Instagram nebo TikTok nesedí, naberte čistou houbičkou stejný make-up, jaký máte na obličeji, a jemně to přejeďte. Ne hustě, ne úplně do krytí. Výsledek je hned nositelnější.</p>'),
]
_GUIDE_CS = dict(modes=[('min', 'Kevyn Aucoin'), ('day', '+ Paint By Ester'), ('eve', '+ Večerní top-up')], modes_label='Varianta techniky',
                 opt='Paint By Ester', eve='Na večer', anchor='krok', prev='Předchozí krok', next='Další krok',
                 alt='Přirozený make-up, foto z mého portfolia', credit='Foto z mého portfolia')

C = {}
C['cs'] = dict(
    toc=[('kratce', 'Postup v kostce'), ('historie', 'Kdo to vymyslel'), ('princip', 'Jak transition blush funguje'), ('michani', 'Namíchejte si přechod'),
         ('navod', 'Návod krok za krokem'), ('stetec', 'Proč velký štětec'), ('tvar', 'Sedí každému obličeji?'), ('verdikt', 'Potřebujete novou kolekci?'), ('faq', 'Časté dotazy')],
    opener='Patrick Ta představil kolekci „transition blurring blushes“ a můj TikTok je jich plný. Je to génius, nebo prodává techniku, která existuje dvacet let? Musíme si teď všichni běžet něco koupit? A sedí opravdu každému obličeji? Ukážu, jak transition blush funguje, odkud se vzal a jak ho udělat z toho, co už máte doma.',
    pre=DEFS,
    summary_h='Postup v kostce',
    steps=['Smíchejte světlé a zvlášť tmavé odstíny tvářenky', 'Světlý odstín k vnitřnímu koutku, rozmazat dolů', 'Tmavší na vystouplou část lícní kosti, ne na jablíčko', 'Světlým odstínem propojit okraje', 'Korektor smíchaný s tvářenkou na kruhy pod očima', 'Zafixovat pudrem', 'Na večer přidat výraznou tvářenku velkým štětcem'],
    tested_h='Pro koho to je',
    tested='<p>Pro každého, kdo chce rozmazanou tvářenku bez ostrého okraje a nechce kvůli tomu kupovat novou kolekci. Stačí korektor, jedna nebo dvě tvářenky a velký štětec. Techniku používám i na klientkách.</p>',
    sections=[
        ('historie', 'Kdo to vymyslel', '<p>Transition blush není novinka. Krátká historie, ať víte, komu dát kredit:</p>\n' + timeline([
            ('Původ', 'Kevyn Aucoin', 'Legendární vizážista techniku popsal jako „transition blush“, píše o ní i ve své knize. Jeho looky jsou supermodelky 80., 90. a nultých let, žádné výrazné barvy. Jeho značka má na to suché produkty s texturou, kterou mám moc ráda.'),
            ('Loni', 'Paint By Ester', 'Vizážistka techniku trochu upravila a udělala výraznější. Otevřeně, veřejně ukázala na masterclassu, jak to dělá. Hlavní trendsetterka posledního roku.'),
            ('Před pár týdny', 'Patrick Ta', 'Americký vizážista celebrit vydal celou řadu produktů „přímo na transition blush“: paletu suchých textur, korektor-tvářenku v tyčince a k tomu paletu suchých a krémových tvářenek. Ani jednoho z předchůdců nezmiňuje a kolekce schytala hodně kritiky.')])),
        ('princip', 'Jak transition blush funguje', '''<p>Princip je jednoduchý: mezi tvářenkou a pletí vytvoříte mezivrstvu produktu, která má jemný nádech tvářenky a dokonale ladí s vaší pletí. Barva pak nepřechází z pleti rovnou do syté skvrny, ale postupně. Potřebujete jen korektor a tvářenku, jednu nebo víc odstínů, a klidně jen suché produkty.</p>
<p>Patrick Ta jako profesionál ví, jak to udělat úplně bez těch produktů. A nemusíte být vizážistka, abyste to zvládly s tím, co máte doma. Spousta z vás to už dělá, jen nevěděla, že se tomu tak říká.</p>'''),
        ('michani', 'Namíchejte si přechod', '''<p>Celé tajemství: smíchejte korektor s tvářenkou v několika poměrech. Nejsvětlejší, trochu tmavší, ještě tmavší, až dojdete k barvě samotné tvářenky. Přechodů může být tolik, kolik chcete, a nemusíte kupovat milion produktů navíc. Vyzkoušejte si to:</p>
''' + mixer(dict(q1='Tvářenka', q2='Počet přechodů', con='korektor', blush='tvářenka', aria='Přechod od korektoru k tvářence', names=dict(lila='Lila-růžová', pink='Sytě růžová', coral='Korálová'),
                 cap='Poměr korektor : tvářenka. Barvy jsou ilustrační.'))),
        ('navod', 'Návod krok za krokem', '''<p>Vyberte variantu: <b>Kevyn Aucoin</b> je jemná denní verze, <b>Paint By Ester</b> přidává velký štětec, korektor s tvářenkou a pudr, <b>večerní top-up</b> barvu navíc. Klikněte na krok a na fotce uvidíte, kam produkt patří.</p>
''' + guide(_GUIDE_CS, STEPS_CS, ZONES)),
        ('stetec', 'Proč velký nadýchaný štětec', '''<p>Je to vlastně jen trochu jiné pořadí kroků, ale rozhoduje štětec. Velký nadýchaný štětec nanese produkt na velkou plochu, slaběji a rovnou rozmazaně. Hustý štětec udělá sytou skvrnu s okrajem, kterou pak musíte rozmazávat. Posuňte jezdec:</p>
''' + brush_demo(('Hustý', 'Nadýchaný', 'Typ štětce', 'Hustý štětec: sytá skvrna s viditelným okrajem.', 'Velký nadýchaný štětec: měkký přechod bez okraje.'))),
        ('tvar', 'Sedí transition blush každému obličeji?', '''<p>Technika sedí každému. Umístění tvářenky se ale liší podle tvaru obličeje. Jak to vypadá u mě a u kulatého obličeje:</p>
''' + picker(dict(q='Tvar obličeje', opts=[('round', 'Kulatý'), ('oval', 'Oválný, ne moc plné tváře')],
                  answers=[('round', 'Kulatý obličej', 'Rozjasnění v trojúhelníku', 'Tvářenka nanesená vysoko a rozjasnění v trojúhelníku pod okem obličej opticky zvednou a působí veseleji. Ten trojúhelník funguje: kde je tmavší odstín, obličej se zužuje, a světlá část dodá jas a definici.'),
                           ('oval', 'Oválný obličej', 'Rozjasnění jen do stínu', 'Do celého trojúhelníku nechoďte. Rozjasnění dejte jen tam, kde je tma. Rozjasnění navíc by u oválného obličeje bez plných tváří působilo nafoukle.')])) + '''
<p>Pokud vás zajímá, kam dávat tvářenku podle tvaru obličeje, napište mi do komentářů pod videem. A jestli si to chcete vyzkoušet na vlastním obličeji, přesně tohle procházíme na <a href="/kurzy-liceni/">individuálním kurzu líčení</a>.</p>'''),
    ],
    verdict_h='Potřebujete kolekci Patricka Ta?',
    verdict=[('Stačí vám', 'vtag v-yes', ['Nejsvětlejší korektor', 'Jedna nebo dvě tvářenky', 'Velký nadýchaný štětec', 'Pudr na fixaci']),
             ('Jen když chcete', 'vtag v-dep', ['Kolekce Patricka Ta (dobré produkty, cca 120 dolarů)', 'Suché produkty Kevyn Aucoin']),
             ('Na co pozor', 'vtag v-sw', ['Jedna sytá skvrna bez přechodu', 'Hustý štětec na první vrstvu', 'Nerozmazané okraje'])],
    verdict_foot='',
    lessons_h='Tři věci, které si z toho vzít',
    lessons=[('Přechod si namícháte sami.', 'Korektor a tvářenka v několika poměrech nahradí celou kolekci. Ušetřila jsem vám zhruba 120 dolarů.'),
             ('Velký štětec dělá polovinu práce.', 'Nadýchaný štětec nanáší slaběji a rovnou rozmazaně, takže nevznikne skvrna.'),
             ('Technika sedí všem, umístění ne.', 'Kulatému obličeji pomůže rozjasnění v trojúhelníku, oválnému spíš jen tam, kde je stín.')],
    learn_h='Chcete si to vyzkoušet na sobě?',
    cta_note='Na <a href="/kurzy-liceni/">individuálním kurzu líčení</a> najdeme umístění tvářenky přesně pro tvar vašeho obličeje a namícháme přechody z vaší kosmetiky.',
    cta_btn=('Kurzy líčení →', '/kurzy-liceni/'),
    cta_title='Výrazná tvářenka, která drží',
    cta_text='Transition blush používám i na klientkách: jemně na focení a nude look, výrazněji na večer a plesy.',
    cta_links=[('Večerní líčení', '/vecerni-liceni/'), ('Nude líčení', '/nude-liceni/')],
    faq_h='Časté dotazy',
    faq=[('Co je transition blush?', 'Technika, při které mezi pletí a tvářenkou vytvoříte mezivrstvu: korektor smíchaný s trochou tvářenky. Barva pak přechází z pleti do tvářenky postupně, bez ostrého okraje.'),
         ('Kdo vymyslel transition blush?', 'Techniku jako „transition blush“ představil vizážista Kevyn Aucoin a psal o ní ve své knize. Výraznější verzi loni zpopularizovala Paint By Ester. Patrick Ta k ní nedávno vydal kolekci produktů.'),
         ('Potřebuji na transition blush speciální produkty?', 'Ne. Stačí nejsvětlejší korektor, jedna nebo dvě tvářenky a velký nadýchaný štětec. Korektor smíchejte s tvářenkou v několika poměrech a máte přechody.'),
         ('Kam nanést tvářenku při transition blush?', 'Tmavší odstín na vystouplou část lícní kosti, ne na jablíčko, až těsně pod oko a kousek do strany. Světlejším odstínem pak propojte okraje.'),
         ('Sedí transition blush každému?', 'Technika ano, umístění tvářenky se ale liší podle tvaru obličeje. Kulatému obličeji pomůže rozjasnění v trojúhelníku pod okem, oválnému bez plných tváří spíš jen do stínu.'),
         ('Co když je tvářenky moc?', 'Čistou houbičkou naberte stejný make-up, jaký máte na obličeji, a jemně ji přejeďte, ne do plného krytí. Nebo okraje rozmažte světlejším odstínem.')],
    bio='Vizážistka v Praze, kde žiji od roku 2021. Věnuji se svatebnímu, večernímu a komerčnímu líčení a učím individuální kurzy. Na YouTube každý týden ukazuji, jak líčím a které produkty opravdu používám.',
)

# ================================================================= ENGLISH
STEPS_EN = [
    (['cheekbone'], 'base', 'Mix your shades', _P('Two blushes', 'the lightest concealer'),
     "<p>First I mix the lightest blushes into a soft transition shade, a lovely lilac on me. Then, separately, I mix the darkest ones: those are the main blushes. You can easily do all of this with a single blush. So far I only have foundation and a little bronzer on, no concealer.</p>"),
    (['inner'], 'base', 'Light shade by the inner corner', _P('Light lilac-pink mix'),
     "<p>The lighter lilac-pink shade goes to the very inner corner of the eye, blended slightly downward. I don't take it under the crease; there's no need. I try to apply it already blended, so I don't have to fix anything afterwards.</p>"),
    (['cheekbone'], 'base', 'Deeper shade on the cheekbone', _P('Deeper blush', 'a brush'),
     "<p>I pick up the deeper shade and apply it to the prominent part of the cheekbone, not the apple. I go right up under the eye while still avoiding the under-eye area, and a little out to the side. The higher you take it, the wider the face looks; from the side it gives a slight lifting effect.</p>"),
    (['nose'], 'base', 'Leftovers on the nose', _P('What is left of the deeper blush'),
     '<p>With the leftovers you can sweep over the nose and blend the rest out to the sides. Optional.</p>'),
    (['cheekbone'], 'base', 'Blend the edges with the light shade', _P('Light mix'),
     "<p>I go back to the lighter shade and run it over the edges so the deeper and lighter shades melt together. With Kevyn Aucoin's technique you could stop here; he would use a less bright concealer under the eyes.</p><aside class=\"note\"><p class=\"lbl red\">Pro tip</p><p>Always blend the edges so the blush doesn't look like a stain. If it's too much, go back to the lighter shade and blend it out.</p></aside>"),
    (['cheekbone', 'cheeks'], 'opt', 'A big fluffy brush', _P('Large fluffy brush', 'blush'),
     "<p>Paint By Ester uses a very large, fluffy brush and picks up the product carefully. She first spreads the blush as widely as possible, so the first layer is less intense and already blended. When I tried it I thought: genius. A large brush blends more softly. With a very dense brush it won't look as nice.</p>"),
    (['under'], 'opt', 'Concealer mixed with blush on dark circles', _P('Concealer mixed with blush'),
     "<p>I cover the dark circles with concealer mixed with blush. You don't have to go all the way down into the under-eye triangle. My face is more oval and my cheeks aren't very full, so it suits me better without extra brightness there, only where there's shadow.</p>"),
    (['outer'], 'opt', 'Clean up the liner', _P('Leftover concealer'),
     "<p>In the same way I clean up the liner with the leftover product, carefully, so nothing smudges. It elongates it visually even more. If you feel you went overboard, run a little light concealer over the edges.</p>"),
    (['face', 'nose'], 'opt', 'Set with powder', _P('Fenty Beauty powder, light lilac'),
     "<p>Paint By Ester sets everything with powder. Mine is a light lilac from Fenty, because that's the shade I'm using today. You can bake if you like, but with today's makeup I don't need to. I love running it down the bridge of the nose to highlight it a little.</p>"),
    (['cheekbone'], 'eve', 'Top up with a bright blush', _P('Bright blush', 'large brush'),
     "<p>If that's not enough, pick up a bright blush with a large brush and emphasise the features you want to draw attention to: like a mask, or, as I do, on the cheekbones to elongate the face. There's no harsh edge, because underneath you've already built a base from skin tone through the lightest pink to a very deep pink.</p>"),
    (['lips', 'lids'], 'eve', 'Colour on lips and eyes', _P('Darkest blush'),
     '<p>I put the darkest blush on the lips and a little on the eyes, so everything comes together.</p>'),
    (['cheekbone', 'cheeks'], 'eve', "If it's too much", _P('A clean sponge', 'your foundation'),
     "<p>If the evening Instagram or TikTok version isn't for you, pick up the same foundation you're wearing with a clean sponge and press it over gently. Not thick, not fully opaque. The result is instantly more wearable.</p>"),
]
_GUIDE_EN = dict(modes=[('min', 'Kevyn Aucoin'), ('day', '+ Paint By Ester'), ('eve', '+ Evening top-up')], modes_label='Technique version',
                 opt='Paint By Ester', eve='Evening', anchor='step', prev='Previous step', next='Next step',
                 alt='Natural makeup, photo from my portfolio', credit='Photo from my portfolio')

C['en'] = dict(
    toc=[('summary', 'The routine in short'), ('history', 'Who came up with it'), ('how-it-works', 'How transition blush works'), ('mixing', 'Mix your own transition'),
         ('how-to', 'Step-by-step guide'), ('brush', 'Why a big brush'), ('face-shape', 'Does it suit every face?'), ('verdict', 'Do you need a new kit?'), ('faq', 'FAQ')],
    opener="Patrick Ta launched his \"transition blurring blushes\" and my TikTok is flooded with them. Is he a genius, or is he selling a technique that has been around for twenty years? Do we all have to rush out and buy something? And does it really suit every face? I'll show you how transition blush works, where it came from and how to do it with what you already own.",
    pre=DEFS,
    summary_h='The routine in short',
    steps=['Mix the light and, separately, the deep blush shades', 'Light shade by the inner corner, blended down', 'Deeper shade on the prominent cheekbone, not the apple', 'Blend the edges with the light shade', 'Concealer mixed with blush on dark circles', 'Set with powder', 'For evening, top up with a bright blush and a big brush'],
    tested_h='Who it is for',
    tested="<p>For anyone who wants a blurred blush without a hard edge and doesn't want to buy a new collection for it. A concealer, one or two blushes and a big brush are enough. I use the technique on clients too.</p>",
    sections=[
        ('history', 'Who came up with it', "<p>Transition blush isn't new. A short history, so you know who to credit:</p>\n" + timeline([
            ('The origin', 'Kevyn Aucoin', 'The legendary makeup artist introduced the technique as "transition blush" and wrote about it in his book. His looks are supermodels of the 80s, 90s and 2000s, no bright colours. His brand makes dry products for it with a texture I really like.'),
            ('Last year', 'Paint By Ester', 'The makeup artist adapted the technique and made it more vibrant. She openly showed how she does it in a public masterclass. The main trendsetter of the past year.'),
            ('A few weeks ago', 'Patrick Ta', 'The American celebrity makeup artist launched a whole line "designed for transition blush": a palette of dry textures, a blush-corrector stick, plus a palette of dry and cream blushes. He mentions neither of his predecessors, and the collection got a lot of hate.')])),
        ('how-it-works', 'How transition blush works', '''<p>The principle is simple: between the blush and the skin you create an intermediate layer of product that has a subtle blush tint and matches your skin perfectly. The colour then doesn't jump from skin straight into a saturated patch, it moves gradually. All you need is concealer and blush, in one or several shades, and dry products work fine.</p>
<p>As a professional, Patrick Ta knows how to do this without those products. And you don't have to be a makeup artist to do it with what you have at home. Many of you already do it; you just didn't know it had a name.</p>'''),
        ('mixing', 'Mix your own transition', '''<p>The whole secret: mix concealer with blush in several proportions. The lightest, a bit deeper, deeper still, until you reach the colour of the blush itself. You can have as many transitions as you like, and you don't need to buy a million extra products. Try it:</p>
''' + mixer(dict(q1='Blush', q2='Number of transitions', con='concealer', blush='blush', aria='Transition from concealer to blush', names=dict(lila='Lilac pink', pink='Bright pink', coral='Coral'),
                 cap='Concealer : blush ratio. Colours are illustrative.'))),
        ('how-to', 'Step-by-step guide', '''<p>Pick a version: <b>Kevyn Aucoin</b> is the soft day version, <b>Paint By Ester</b> adds a big brush, concealer mixed with blush and powder, and the <b>evening top-up</b> adds extra colour. Tap a step to see on the photo where the product goes.</p>
''' + guide(_GUIDE_EN, STEPS_EN, ZONES)),
        ('brush', 'Why a big fluffy brush', '''<p>It's really just a slightly different order of steps, but the brush makes the difference. A big fluffy brush lays the product over a large area, lighter and already blended. A dense brush leaves a saturated patch with an edge you then have to blend out. Move the slider:</p>
''' + brush_demo(('Dense', 'Fluffy', 'Brush type', 'Dense brush: a saturated patch with a visible edge.', 'Big fluffy brush: a soft transition with no edge.'))),
        ('face-shape', 'Does transition blush suit every face?', '''<p>The technique suits everyone. Where you place the blush, though, depends on your face shape. Here's how it works on me and on a round face:</p>
''' + picker(dict(q='Face shape', opts=[('round', 'Round'), ('oval', 'Oval, cheeks not very full')],
                  answers=[('round', 'Round face', 'Brighten the triangle', 'Blush placed high and brightness in the triangle under the eye lift the face and make it look more cheerful. The triangle works: the face narrows where the deeper shade sits, and the light part adds brightness and definition.'),
                           ('oval', 'Oval face', 'Brighten only the shadow', "Don't go into the whole triangle. Add brightness only where there's darkness. Extra brightness on an oval face without full cheeks can look puffy.")])) + '''
<p>If you'd like to know where blush goes for each face shape, tell me in the comments under the video. And if you want to try it on your own face, that's exactly what we cover in a <a href="/en/courses/">one-on-one makeup course</a>.</p>'''),
    ],
    verdict_h="Do you need Patrick Ta's collection?",
    verdict=[('All you need', 'vtag v-yes', ['The lightest concealer', 'One or two blushes', 'A big fluffy brush', 'Setting powder']),
             ('Only if you want to', 'vtag v-dep', ["Patrick Ta's collection (good products, about $120)", 'Kevyn Aucoin dry products']),
             ('Watch out for', 'vtag v-sw', ['One saturated patch with no transition', 'A dense brush for the first layer', 'Unblended edges'])],
    verdict_foot='',
    lessons_h='Three things to take away',
    lessons=[('You can mix the transition yourself.', 'Concealer and blush in a few proportions replace a whole collection. I just saved you about 120 dollars.'),
             ('A big brush does half the work.', 'A fluffy brush applies lighter and already blended, so you never get a stain.'),
             ("The technique suits everyone; placement doesn't.", 'A round face benefits from brightness in the triangle, an oval one rather only where there is shadow.')],
    learn_h='Want to try it on your own face?',
    cta_note='In a <a href="/en/courses/">one-on-one makeup course</a> we find the blush placement for your face shape and mix transitions from your own products.',
    cta_btn=('View courses →', '/en/courses/'),
    cta_title='Bold blush that lasts',
    cta_text='I use transition blush on clients too: softly for shoots and nude looks, bolder for evening events.',
    cta_links=[('Evening makeup', '/en/evening-makeup/'), ('Nude makeup', '/en/nude-makeup/')],
    faq_h='Frequently asked questions',
    faq=[('What is transition blush?', 'A technique where you build an intermediate layer between skin and blush: concealer mixed with a little blush. The colour then moves from skin to blush gradually, without a hard edge.'),
         ('Who invented transition blush?', 'The makeup artist Kevyn Aucoin introduced it as "transition blush" and wrote about it in his book. Paint By Ester popularised a more vibrant version last year. Patrick Ta recently launched a product collection for it.'),
         ('Do I need special products for transition blush?', 'No. The lightest concealer, one or two blushes and a big fluffy brush are enough. Mix the concealer with the blush in a few proportions and you have your transitions.'),
         ('Where do I apply blush for transition blush?', 'The deeper shade goes on the prominent part of the cheekbone, not the apple, right up under the eye and a little out to the side. Then blend the edges with the lighter shade.'),
         ('Does transition blush suit everyone?', 'The technique does, but blush placement depends on face shape. A round face benefits from brightness in the under-eye triangle; an oval face without full cheeks rather only where there is shadow.'),
         ("What if there's too much blush?", 'Pick up the same foundation you are wearing with a clean sponge and press it over gently, not to full coverage. Or blend the edges out with the lighter shade.')],
    bio='Makeup artist based in Prague since 2021. I do bridal, evening and commercial makeup and teach one-on-one courses. Every week on YouTube I show how I do makeup and which products I genuinely use.',
)

import re as _re
HOWTO = {lang: [(t, ' '.join(_re.sub(r'<aside.*?</aside>|<[^>]+>', ' ', b).split())) for _z, _m, t, _p, b in (STEPS_CS if lang == 'cs' else STEPS_EN)] for lang in ('cs', 'en')}
TOOLS = {'cs': ['Velký nadýchaný štětec', 'Štětec na tvářenku', 'Houbička na make-up'], 'en': ['Large fluffy brush', 'Blush brush', 'Makeup sponge']}
SUPPLY = ['Concealer (lightest shade)', 'Blush (one or more shades)', 'Setting powder', 'Foundation']

EXTRA = dict(products=[], brands=BRANDS, about=('Transition blush', 'Transition blush'),
             video_name='Хто в кого вкрав? Transition blush техніка пояснена', howto=dict(steps=HOWTO, supply=SUPPLY, tools=TOOLS))
