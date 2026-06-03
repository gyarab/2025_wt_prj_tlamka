from ninja import NinjaAPI, Schema
from typing import Optional, List
from .models import Myslitel, Dilo, Myslenka

api = NinjaAPI()


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


class MyslenkOut(Schema):
    id: int
    text: str
    autor_id: int
    dilo_id: Optional[int] = None


class MyslenkIn(Schema):
    text: str
    autor_id: int
    dilo_id: Optional[int] = None


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