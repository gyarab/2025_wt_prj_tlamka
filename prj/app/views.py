from django.shortcuts import render
from .models import Myslitel, Smer, Epocha, Dilo, Myslenka

def index(request):
    kontext = {
        'pocet_myslitelu': Myslitel.objects.count(),
        'pocet_myslenek': Myslenka.objects.count(),
        'pocet_smeru': Smer.objects.count(),
    }
    
    return render(request, 'index.html', kontext)