from django.contrib import admin
from django.urls import path
from prj.app import views  # Změněno z 'from app import views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]