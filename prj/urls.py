from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Zde je admin na svém správném místě
    path('admin/', admin.site.urls),
    
    # Připojení tvé aplikace
    path('', include('prj.app.urls')),
]

# Obsluha médií pro vývoj (portréty myslitelů)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)