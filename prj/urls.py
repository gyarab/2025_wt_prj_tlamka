from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Cesta do kontrolního centra
    path('admin/', admin.site.urls),
    
    # 2. Cesta k tvé aplikaci (ZDE BYLA PRAVDĚPODOBNĚ CHYBA REKURZE)
    # Všimni si přesného zápisu 'prj.app.urls' 
    path('', include('prj.app.urls')),
]

# 3. Architektonický bypass pro lokální vývoj
if settings.DEBUG:
    # Podpora pro statické soubory (CSS, JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Podpora pro uživatelsky nahraná média (Obrázky)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)