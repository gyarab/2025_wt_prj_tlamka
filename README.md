# Webová aplikace  
## Projekt – Matouš Tlamka

**Vytvořeno v předmětu Webové technologie**  
Gymnázium Arabská, Praha  
Školní rok **2025/2026**

> „Jednoduchost je vrchol sofistikovanosti.“  
> — Leonardo da Vinci

---

## O projektu

Tato webová aplikace vznikla jako projekt v předmětu **Webové technologie**.

---

## Použité technologie

### Backend
- Python 3.11+
- Flask / FastAPI / Django *(doplň používaný framework)*

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Šablony
- Jinja2

### Databáze
- SQLite (vývoj)
- PostgreSQL (volitelně)

### Správa závislostí
- pip  
- requirements.txt  

---

# Rychlý start (lokální vývoj)

## 1️. Vytvoření virtuálního prostředí

```bash
python3 -m venv .venv
```

---

## 2️. Aktivace prostředí

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

## 3️. Instalace závislostí

Aktualizace pip (doporučeno):

```bash
python -m pip install --upgrade pip setuptools wheel
```

Instalace projektu:

```bash
pip install -r requirements.txt
```

---

## 4️. Spuštění aplikace

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


## 📄 Licence

Projekt byl vytvořen pro studijní účely v rámci výuky.  
Není určen pro komerční využití.

---

## 👨‍🎓 Autor

Matouš Tlamka  
Gymnázium Arabská, Praha  
Školní rok 2025/2026
