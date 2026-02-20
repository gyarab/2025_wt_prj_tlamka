# Webová aplikace  
## Projekt – Matouš Tlamka

**Vytvořeno v předmětu Webové technologie**  
Gymnázium Arabská, Praha  
Školní rok **2025/2026**

> „Jednoduchost je vrchol sofistikovanosti.“  
> — Leonardo da Vinci

---

# Obsah

1. [O projektu](#o-projektu)  
2. [Rychlý start (lokální vývoj)](#rychlý-start-lokální-vývoj)  
3. [Spuštění aplikace](#spuštění-aplikace)  
4. [Licence](#licence)  
5. [Autor](#autor)  

---

## O projektu

Tato webová aplikace vznikla jako školní projekt a slouží jako interaktivní databáze pro všechny, které zajímá filosofie a vývoj lidského myšlení. Cílem je přehledně propojit významné myslitele s jejich hlavními myšlenkami, historickým obdobím a zemí, ze které pocházejí.

Uživatelé tu mohou jednoduše vyhledávat a procházet různé kategorie – od konkrétních filosofů přes historické epochy až po hlavní filosofické směry a disciplíny, jako je třeba metafyzika nebo gnoseologie.

---

# Rychlý start (lokální vývoj)

## 1. Vytvoření virtuálního prostředí

```bash
python3 -m venv .venv
```

Na Windows můžeš případně použít:

```bash
python -m venv .venv
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

### Flask

```bash
flask run
```

### FastAPI

```bash
uvicorn main:app --reload
```

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

Projekt byl vytvořen pro studijní účely v rámci výuky.  

---

## Autor

Matouš Tlamka  
Gymnázium Arabská, Praha  
Školní rok 2025/2026
