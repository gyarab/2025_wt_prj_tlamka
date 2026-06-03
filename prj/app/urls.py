from django.urls import path
from . import views
from .api import api

urlpatterns = [
    # Domovská stránka (Agora)
    path('', views.index, name='index'),
    
    # Síň předků
    path('myslitele/', views.sin_predku, name='sin_predku'),
    
    # Detail myslitele
    path('myslitele/<int:id>/', views.myslitel_detail, name='myslitel_detail'),
    
    # Katalog děl
    path('dila/', views.dila_seznam, name='dila_seznam'),
    
    # Proud vědomí (Axiomy)
    path('axiomy/', views.proud_vedomi, name='proud_vedomi'),
    
    # API rozhraní (Ninjutsu tvého systému)
    path("api/", api.urls),

    path('playground/', views.playground, name='playground'),

    path('vue/', views.vue_app, name='vue_app'),
]