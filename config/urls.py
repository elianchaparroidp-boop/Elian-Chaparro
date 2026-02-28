from django.contrib import admin
from django.urls import path
from menu.views import lista_productos
from django.conf import settings # Agrega esto
from django.conf.urls.static import static # Agrega esto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_productos, name='home'),
]

# Esto permite que Django muestre las fotos que subiste
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)