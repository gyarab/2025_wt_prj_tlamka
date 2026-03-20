from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myslitele/', views.sin_predku, name='sin_predku'),
    path('myslitele/<int:id>/', views.myslitel_detail, name='myslitel_detail'),
    path('dila/', views.dila_seznam, name='dila_seznam'),
    path('axiomy/', views.proud_vedomi, name='proud_vedomi'),
]