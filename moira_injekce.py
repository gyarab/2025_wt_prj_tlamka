import os
import django

# 1. Inicializace spojení s databází I.D.E.A.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from prj.app.models import Epocha, Smer, Myslitel, Dilo, Myslenka

print("Zahajuji Protokol M.O.I.R.A. - Materializace dat...")

# 2. Definice abstraktních konceptů
epocha, _ = Epocha.objects.get_or_create(nazev="Filosofie 19. století", defaults={'obdobi': '1801–1900', 'charakteristika': 'Doba radikálního přehodnocování tradičních hodnot a nástupu moderních věd.'})
smer_nihilismus, _ = Smer.objects.get_or_create(nazev="Nihilismus", defaults={'definice': 'Filosofický postoj popírající objektivní smysl, pravdu nebo hodnotu lidské existence.'})
smer_existencialismus, _ = Smer.objects.get_or_create(nazev="Existencialismus", defaults={'definice': 'Směr zaměřený na individuální existenci, svobodu a hledání smyslu v absurdním světě.'})

# 3. Stvoření samotného myslitele
nietzsche, _ = Myslitel.objects.get_or_create(jmeno="Friedrich Nietzsche", defaults={
    'roky_zivota': '1844–1900', 
    'zivotopis': 'Německý filosof, klasický filolog, básník a kulturní kritik. Jeho dílo radikálně zpochybnilo základy západního náboženství, morálky a filosofie. Otevřel cestu k překonání člověka a vzniku nadčlověka (Übermensch).'
})
nietzsche.epocha = epocha
nietzsche.smery.add(smer_nihilismus, smer_existencialismus)
nietzsche.save()

# 4. Záznam děl
dilo_zarathustra, _ = Dilo.objects.get_or_create(nazev="Tak pravil Zarathustra", autor=nietzsche, defaults={'rok_vydani': '1883', 'popis': 'Filosofický román představující koncepty nadčlověka, věčného návratu a vůle k moci.'})
dilo_dobro_zlo, _ = Dilo.objects.get_or_create(nazev="Mimo dobro a zlo", autor=nietzsche, defaults={'rok_vydani': '1886', 'popis': 'Kritika dosavadní filosofie a nástin filosofie budoucnosti.'})

# 5. Extrakce fundamentálních axiomů
Myslenka.objects.get_or_create(text="Neexistují žádná fakta, pouze interpretace.", autor=nietzsche, dilo=dilo_dobro_zlo)
Myslenka.objects.get_or_create(text="Bůh je mrtev! Bůh zůstane mrtev! A my jsme ho zabili!", autor=nietzsche)
Myslenka.objects.get_or_create(text="Kdo bojuje s nestvůrami, ať se má na pozoru, aby se sám nestal nestvůrou. A když dlouho hledíš do propasti, propast pohlédne do tebe.", autor=nietzsche, dilo=dilo_dobro_zlo)
Myslenka.objects.get_or_create(text="Člověk je něco, co má být překonáno.", autor=nietzsche, dilo=dilo_zarathustra)

print("Data úspěšně zapsána do ontologické sítě!")