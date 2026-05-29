from ninja import NinjaAPI, Schema
from typing import Optional, List
from .models import Myslitel, Dilo, Myslenka

api = NinjaAPI()


# ── Schémata: Myslitel ─────────────────────────────────────

class MyslitelOut(Schema):
    id: int
    jmeno: str
    roky_zivota: Optional[str] = None
    zivotopis: str
    epocha_id: Optional[int] = None


class MyslitelIn(Schema):
    jmeno: str
    roky_zivota: Optional[str] = None
    zivotopis: str
    epocha_id: Optional[int] = None


# Speciální schéma pro potřeby asynchronního frontendu Panteonu
class MyslitelFrontendOut(Schema):
    id: int
    jmeno: str
    epocha: str
    citat: str
    inicialy: str


# ── Schémata: Dilo ─────────────────────────────────────────

class DiloOut(Schema):
    id: int
    nazev: str
    rok_vydani: Optional[str] = None
    popis: Optional[str] = None
    autor_id: int


class DiloIn(Schema):
    nazev: str
    rok_vydani: Optional[str] = None
    popis: Optional[str] = None
    autor_id: int


# ── Schémata: Myslenka ─────────────────────────────────────

class MyslenkOut(Schema):
    id: int
    text: str
    autor_id: int
    dilo_id: Optional[int] = None


class MyslenkIn(Schema):
    text: str
    autor_id: int
    dilo_id: Optional[int] = None


# ── Endpointy: Speciální uzel pro Vue Frontend ─────────────

@api.get("/myslitele", response=List[MyslitelFrontendOut])
def seznam_myslitelu_frontend(request):
    """Vrací optimalizovaná data pro monolitické karty frontendu."""
    myslitele = Myslitel.objects.all()
    vysledek = []
    
    for m in myslitele:
        # Získání první myšlenky autora
        prvni_myslenka = m.myslenka_set.first()
        myslenka_text = prvni_myslenka.text if prvni_myslenka else "Zatím žádná myšlenka v síti..."
        
        # Ošetření vazby na epochu
        epocha_nazev = m.epocha.nazev if m.epocha else "Neznámá epocha"
        
        # Generování iniciál (pokud model nemá metodu ziskej_inicialy)
        if hasattr(m, 'ziskej_inicialy'):
            inicialy = m.ziskej_inicialy()
        else:
            inicialy = "".join([cast[0].upper() for cast in m.jmeno.split() if cast])[:2]
            
        vysledek.append({
            "id": m.id,
            "jmeno": m.jmeno,
            "epocha": epocha_nazev,
            "citat": myslenka_text,
            "inicialy": inicialy
        })
        
    return vysledek


# ── Endpointy: Myslitel (Původní CRUD) ────────────────────

@api.get("/myslitel", response=List[MyslitelOut])
def seznam_myslitelu(request):
    return Myslitel.objects.all()


@api.get("/myslitel/{myslitel_id}", response=MyslitelOut)
def detail_myslitele(request, myslitel_id: int):
    return Myslitel.objects.get(id=myslitel_id)


@api.post("/myslitel", response=MyslitelOut)
def vytvor_myslitele(request, data: MyslitelIn):
    myslitel = Myslitel.objects.create(**data.dict())
    return myslitel


@api.put("/myslitel/{myslitel_id}", response=MyslitelOut)
def uprav_myslitele(request, myslitel_id: int, data: MyslitelIn):
    myslitel = Myslitel.objects.get(id=myslitel_id)
    for attr, value in data.dict().items():
        setattr(myslitel, attr, value)
    myslitel.save()
    return myslitel


# ── Endpointy: Dilo (Původní CRUD) ────────────────────────

@api.get("/dilo", response=List[DiloOut])
def seznam_del(request):
    return Dilo.objects.all()


@api.get("/dilo/{dilo_id}", response=DiloOut)
def detail_dila(request, dilo_id: int):
    return Dilo.objects.get(id=dilo_id)


@api.post("/dilo", response=DiloOut)
def vytvor_dilo(request, data: DiloIn):
    dilo = Dilo.objects.create(**data.dict())
    return dilo


@api.put("/dilo/{dilo_id}", response=DiloOut)
def uprav_dilo(request, dilo_id: int, data: DiloIn):
    dilo = Dilo.objects.get(id=dilo_id)
    for attr, value in data.dict().items():
        setattr(dilo, attr, value)
    dilo.save()
    return dilo


# ── Endpointy: Myslenka (Původní CRUD) ────────────────────

@api.get("/myslenka", response=List[MyslenkOut])
def seznam_myslenek(request):
    return Myslenka.objects.all()


@api.get("/myslenka/{myslenka_id}", response=MyslenkOut)
def detail_myslenky(request, myslenka_id: int):
    return Myslenka.objects.get(id=myslenka_id)


@api.post("/myslenka", response=MyslenkOut)
def vytvor_myslenku(request, data: MyslenkIn):
    myslenka = Myslenka.objects.create(**data.dict())
    return myslenka


@api.put("/myslenka/{myslenka_id}", response=MyslenkOut)
def uprav_myslenku(request, myslenka_id: int, data: MyslenkIn):
    myslenka = Myslenka.objects.get(id=myslenka_id)
    for attr, value in data.dict().items():
        setattr(myslenka, attr, value)
    myslenka.save()
    return myslenka