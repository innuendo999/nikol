"""Google reviews (copied from the Google Business Profile, emoji removed, long ones shortened with …)."""
R = {
    'erika': dict(name='Erika Bartaková', ini='EB', lang='cs', extra=' · Local Guide',
                  text='„V minulosti jsem si nechávala dělat profesionální make-up, ale nic z toho se nedá ani srovnat s tím, co Nikol vykouzlila. Fakt neskutečný. Jednoznačně doporučuji. Přesně odhadla, co mi bude slušet. … Make-up přežil velké horko až do večera.“'),
    'erika_w': dict(name='Erika Bartaková', ini='EB', lang='cs', extra=' · Local Guide',
                    text='„Naprosto to předčilo moje očekávání. Přesně odhadla, co mi bude slušet. Make-up přežil velké horko až do večera. … Díky téhle zkušenosti jsem našla make-up artistku na svou svatbu.“'),
    'darya': dict(name='Дар’я Собакіна', ini='ДС', lang='uk',
                  text='„Побачивши роботу Ніколь у своєї подруги я відразу захотіла також, і не прогадала. Ніколь чудова людина і шикарний майстер, макіяж і зачіска. Макіяж підкреслив всі мої виграшні сторони, а зачіска завершила цей образ. Рекомендую від серця.“'),
    'shirley': dict(name='Shirley Ficler', ini='SF', lang='en',
                    text='“Nikol did my hair &amp; makeup for my wedding. She did exactly what I asked her for, and it turned out amazing. Highly recommend!”'),
    'zoe': dict(name='Zoe Chan', ini='ZC', lang='en', extra=' · Local Guide',
                text='“Getting a makeover isn’t something I do often, but Nikol’s cozy home studio and her warm, welcoming approach put me at ease immediately. … The final result was a flawless look that held up perfectly for over 15 hours.”'),
    'zoe_c': dict(name='Zoe Chan', ini='ZC', lang='en', extra=' · Local Guide',
                  text='“She took the time to truly understand my preferences, carefully considering my skin tone and hair texture to craft the exact look I had in mind. … I can’t recommend her highly enough for anyone needing makeup and hairstyling for special occasions or modeling.”'),
    'karin': dict(name='Karin Gulíková', ini='KG', lang='sk', extra=' · Local Guide',
                  text='„Už som tu bola viac krát a vždy výborná skúsenosť. Mám problematickú pleť s jazvami po akne, s čím sa ale pani maskérka vždy hravo vysporiada, makeup vydrží veľmi dlho a je vždy podľa mojich predstáv.“'),
    'nelli': dict(name='Gabbiasova Nelli', ini='GN', lang='cs',
                  text='„Make-up předčil moje očekávání! Pleť vypadala svěže, sjednoceně a přirozeně, oči krásně vynikly a celý look mi perfektně seděl. Oceňuju i to, že všechno probíhalo v klidu, bez spěchu a s důrazem na detaily. Líčení vydrželo až do večera a slyšela jsem spoustu komplimentů.“'),
    'beata': dict(name='Beáta Mechurová', ini='BM', lang='en', extra=' · Local Guide',
                  text='“Nikol is a very professional, kind and works with high quality products. She also speaks english perfectly.”'),
    'stepanka': dict(name='Štěpánka Šedivá', ini='ŠŠ', lang='cs',
                     text='„Chtěla bych moc poděkovat úžasné Nikol za naprosto dokonalý letní make-up. Celé líčení probíhalo v super přátelské a uvolněné atmosféře. Výsledek byl ještě lepší, než jsem si představovala – krásný, svěží a rozzářený look. Make-up držel jako přibitý celý den a večer!“'),
    'glenn': dict(name='Glenn Sousa', ini='GS', lang='en',
                  text='“Nikol was amazing!! She is super sweet, easy to work with and understood the brief completely. I’m so happy with the finished look and got so many compliments. I highly recommend Nikol and hope to work with her again in the future.”'),
    'marie': dict(name='Marie Slováčková', ini='MS', lang='cs',
                  text='„Nikol je úžasná vizážistka, která vždy zjišťuje, co si klient opravdu přeje, vcítí se do jeho pocitu ohledně make-upu a komunikuje jeho potřeby. Líčila mě již třikrát a pokaždé byl výsledek skvělý. Vřele doporučuji!“'),
    'lena': dict(name='Lenaaa', ini='L', lang='en',
                 text='“Every look from Nikol was beautiful, she knows what she’s doing very well and she is a professional. I’m glad I got to know her.”'),
    'polina': dict(name='Polina', ini='P', lang='en',
                   text='“Nikol is an amazing makeup artist! She’s talented, creative and super considerate of all the client’s wishes. She did my makeup for a recent pregnancy photoshoot of mine and I couldn’t be more content with the end results.”'),
    'polinashu': dict(name='Polina Shu', ini='PS', lang='cs',
                      text='„Nikol je nejlepší vizážistka v Praze. Miluju její kreativní styl a kvalitu líčení. Líčila mě na svatební focení a výsledek byl úžasný. Vřele doporučuji!“'),
}


def pick(*keys):
    return [R[k] for k in keys]
