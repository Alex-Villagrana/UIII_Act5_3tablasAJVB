# Contenido CORRECTO de backend_Skateshop/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- ¡Importa include!
from django.conf import settings
from django.conf.urls.static import static

# NOTA: NO DEBES tener una línea como 'from . import views' o 'from backend_Skateshop import views' aquí.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea delega todas las rutas vacías ('') a las URLs de tu app.
    path('', include('app_Skateshop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
