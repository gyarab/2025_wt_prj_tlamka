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
    """Výpis myslitelů s možností filtrace podle epochy."""
    epocha_id = request.GET.get('epocha')
    epochy = Epocha.objects.all()
    
    if epocha_id:
        myslitele = Myslitel.objects.filter(epocha_id=epocha_id)
        zvolena_epocha = get_object_or_404(Epocha, id=epocha_id)
    else:
        myslitele = Myslitel.objects.all()
        zvolena_epocha = None
        
    return render(request, 'myslitele.html', {
        'myslitele': myslitele,
        'epochy': epochy,
        'zvolena_epocha': zvolena_epocha
    })

def myslitel_detail(request, id):
    """Detailní profil myslitele."""
    myslitel = get_object_or_404(Myslitel, id=id)
    return render(request, 'myslitel_detail.html', {'myslitel': myslitel})

def dila_seznam(request):
    """Katalog děl."""
    dila = Dilo.objects.all().select_related('autor').order_by('nazev')
    return render(request, 'dila.html', {'dila': dila})

def proud_vedomi(request):
    """Proud axiomů s integrovaným vyhledáváním."""
    dotaz = request.GET.get('q')
    
    if dotaz:
        # Vyhledává v textu myšlenky i ve jméně autora (case-insensitive)
        axiomy = Myslenka.objects.filter(
            text__icontains=dotaz
        ).select_related('autor', 'dilo').order_by('?')
    else:
        axiomy = Myslenka.objects.all().select_related('autor', 'dilo').order_by('?')
        
    return render(request, 'proud_vedomi.html', {
        'axiomy': axiomy,
        'dotaz': dotaz
    })