# I.D.E.A. 
## Interaktivní Databáze Epistemologie a Axiomů

**Vytvořeno v rámci předmětu Webové technologie**  
Gymnázium Arabská, Praha  
Školní rok **2025/2026**

> „Jednoduchost je vrchol sofistikovanosti.“  
> — Leonardo da Vinci

---

# Obsah

1. [O projektu](#o-projektu)  
2. [Rychlý start](#rychlý-start)   
3. [Licence](#licence)  
4. [Autor](#autor)  

---

## O projektu

**I.D.E.A.**
Interaktivní Databáze Epistemologie a Axiomů

Cílem tohoto projektu je vytvořit komplexní relační <u>databázi</u>, která systematicky mapuje vývoj lidského <u>myšlení</u>. V dnešní době přehlcené povrchními informacemi chci nabídnout strukturovaný <u>nástroj</u> pro skutečně hluboké <u>studium</u>.

Základními stavebními kameny celé <u>aplikace</u> jsou jednotliví <u>myslitelé</u>. Každý <u>autor</u> je v <u>systému</u> pevně ukotven a provázán se svými klíčovými <u>díly</u>, historickou <u>epochou</u> a geografickým <u>původem</u>. Nejde však o pouhý strohý <u>seznam</u> jmen. Hlavní přidanou hodnotou je úzké propojení na konkrétní <u>koncepty</u> a myšlenkové <u>směry</u> (jako je například <u>stoicismus</u> či <u>existencialismus</u>). Celá <u>architektura</u> je dále kategorizována podle fundamentálních <u>disciplín</u>, s primárním důrazem na <u>metafyziku</u> a <u>gnoseologii</u>. To umožňuje přesně sledovat evoluci určitého <u>problému</u> napříč staletími a pochopit tak skryté <u>souvislosti</u>.

Z hlediska uživatelského <u>přístupu</u> je web rozdělen do tří úrovní. Běžný nepřihlášený <u>návštěvník</u> může volně procházet veřejný <u>katalog</u>, filtrovat <u>záznamy</u> podle zadaných <u>kritérií</u> a číst si základní <u>definice</u> či <u>životopisy</u>.

Aby se však z pasivního čtenáře stal aktivní účastník, je vyžadována <u>registrace</u>. Přihlášený <u>uživatel</u> získává prostor pro hlubší <u>interakci</u>. Může k jednotlivým <u>tezím</u> přidávat vlastní <u>komentáře</u>, reflektovat přečtené <u>texty</u> a především si ukládat stěžejní <u>citáty</u> do osobního <u>výběru</u>. Vzniká tak izolovaný <u>prostor</u> pro racionální utřídění vlastního <u>světonázoru</u>.

Nejvyšší <u>oprávnění</u> drží <u>administrátor</u>, který ručí za faktickou správnost celého <u>lexikonu</u>. Přes zabezpečené redakční <u>rozhraní</u> přidává nové <u>entity</u>, spravuje relační <u>vazby</u> a moderuje uživatelský <u>obsah</u>. Po technologické <u>stránce</u> projekt plně využívá <u>framework</u> k zajištění stabilního chodu a pokročilé práce s <u>daty</u>.

---
### Návrh User Flow

![UserFlow](dokumentace/userFlow_idea.png)


![Původní návrh User Flow](dokumentace/userFlow.jpg)


### Ukázka rozhraní (Wireframes)

![WebWireframe](dokumentace/wifeframe1.jpg)

![MobileWireframe](dokumentace/wifeframe2.jpg)

---

# Rychlý start

## 1. Vytvoření virtuálního prostředí

```bash
python3 -m venv .venv
```

---

## 2. Aktivace prostředí

### macOS / Linux / Git Bash / WSL

```bash
source .venv/bin/activate
```

### Windows – PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### Windows – Příkazový řádek (cmd)

```bash
.venv\Scripts\activate.bat
```

Pokud PowerShell hlásí chybu o spouštění skriptů, spusť jednorázově:

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## 3. Instalace závislostí

Aktualizace pip (doporučeno):

```bash
python -m pip install --upgrade pip setuptools wheel
```

Instalace projektu:

```bash
pip install -r requirements.txt
```

---

## 4. Spuštění aplikace

### Django

```bash
python manage.py runserver
```

Aplikace bude dostupná typicky na:

```
http://127.0.0.1:8000
```

nebo

```
http://127.0.0.1:5000
```

---

## Licence

Tento projekt podléhá přísné proprietární licenci. **Všechna práva jsou vyhrazena.**

Plné znění licenčního ujednání, které definuje přesné hranice užití, naleznete v přiloženém souboru [`LICENSE`](LICENSE).

---

## Autor

Matouš Tlamka  
Gymnázium Arabská, Praha  
Školní rok 2025/2026
