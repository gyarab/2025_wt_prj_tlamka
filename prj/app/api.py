from ninja import NinjaAPI, Schema
from typing import Optional, List
from .models import Myslitel

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