import os
import django

# Inicializace spojení
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from prj.app.models import Epocha, Smer, Myslitel, Dilo, Myslenka

print("Zahajuji Protokol M.O.I.R.A. - Fáze 2: Expanze Panteonu...")

# 1. Epochy a Směry
antika, _ = Epocha.objects.get_or_create(nazev="Antická filosofie", defaults={'obdobi': '6. stol. př. n. l. – 6. stol. n. l.', 'charakteristika': 'Zrod západního myšlení, hledání arché a ideálního státu.'})
epocha_19, _ = Epocha.objects.get_or_create(nazev="Filosofie 19. století")

idealismus, _ = Smer.objects.get_or_create(nazev="Idealismus", defaults={'definice': 'Směr upřednostňující ideu, ducha či vědomí před materiální realitou.'})
pesimismus, _ = Smer.objects.get_or_create(nazev="Filosofický pesimismus", defaults={'definice': 'Postoj zdůrazňující utrpení a marnost existence, často spojený s popřením vůle.'})

# 2. Platón
platon, _ = Myslitel.objects.get_or_create(jmeno="Platón", defaults={
    'roky_zivota': '427–347 př. n. l.', 
    'zivotopis': 'Žák Sókratův a učitel Aristotelův. Zakladatel Akademie a autor teorie ideí. Jeho myšlení tvoří páteř západní metafyziky, kterou se pozdější filosofové pokoušeli buď upevnit, nebo vyvrátit.'
})
platon.epocha = antika
platon.smery.add(idealismus)
platon.save()

dilo_republika, _ = Dilo.objects.get_or_create(nazev="Ústava (Politeia)", autor=platon, defaults={'rok_vydani': 'cca 375 př. n. l.', 'popis': 'Dialog o spravedlnosti a ideálním uspořádání obce.'})

Myslenka.objects.get_or_create(text="Tělo je žalářem duše.", autor=platon)
Myslenka.objects.get_or_create(text="Poznání je pouze rozpomínání se na to, co duše viděla v říši ideí.", autor=platon, dilo=dilo_republika)

# 3. Arthur Schopenhauer
schopenhauer, _ = Myslitel.objects.get_or_create(jmeno="Arthur Schopenhauer", defaults={
    'roky_zivota': '1788–1860', 
    'zivotopis': 'Německý filosof, známý svou analýzou světa jako projevu slepé a nenasytné Vůle. Jeho pesimistická vize hluboce ovlivnila mladého Nietzscheho i celou moderní psychologii.'
})
schopenhauer.epocha = epocha_19
schopenhauer.smery.add(pesimismus)
schopenhauer.save()

dilo_vule, _ = Dilo.objects.get_or_create(nazev="Svět jako vůle a představa", autor=schopenhauer, defaults={'rok_vydani': '1818', 'popis': 'Základní Schopenhauerovo dílo definující podstatu reality jako slepý pud.'})

Myslenka.objects.get_or_create(text="Svět je má představa.", autor=schopenhauer, dilo=dilo_vule)
Myslenka.objects.get_or_create(text="Život osciluje jako kyvadlo mezi utrpením a nudou.", autor=schopenhauer)
Myslenka.objects.get_or_create(text="Člověk může dělat, co chce, ale nemůže chtít, co chce.", autor=schopenhauer, dilo=dilo_vule)

print("Mise splněna. Platón i Schopenhauer jsou nyní součástí ontologie.")