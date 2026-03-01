from django.contrib import admin
from django.urls import path
from menu.views import lista_productos
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_productos, name='home'),
]

# Esto asegura que las fotos se vean en Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)