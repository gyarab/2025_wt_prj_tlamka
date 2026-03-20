from django.shortcuts import render, get_object_or_404
from .models import Myslitel, Smer, Epocha, Myslenka, Dilo

def index(request):
    """Hlavní rozcestník s počítadly."""
    return render(request, 'index.html', {
        'pocet_myslitelu': Myslitel.objects.count(),
        'pocet_smeru': Smer.objects.count(),
        'pocet_myslenek': Myslenka.objects.count(),
        'pocet_del': Dilo.objects.count(),
    })

def sin_predku(request):
    """Výpis všech myslitelů (Síň předků)."""
    return render(request, 'myslitele.html', {'myslitele': Myslitel.objects.all()})

def myslitel_detail(request, id):
    """Detailní profil konkrétního myslitele."""
    myslitel = get_object_or_404(Myslitel, id=id)
    return render(request, 'myslitel_detail.html', {'myslitel': myslitel})

def dila_seznam(request):
    """Katalog všech děl v systému."""
    dila = Dilo.objects.all().select_related('autor').order_by('nazev')
    return render(request, 'dila.html', {'dila': dila})

def proud_vedomi(request):
    """Proud axiomů s náhodným řazením (order_by('?'))."""
    # Náhodné řazení zajistí, že Proud vědomí bude při každém načtení jiný
    axiomy = Myslenka.objects.all().select_related('autor', 'dilo').order_by('?')
    return render(request, 'proud_vedomi.html', {'axiomy': axiomy})