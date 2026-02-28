from django.contrib import admin
from .models import Producto  # <--- Debe tener la misma "P" mayúscula

admin.site.register(Producto)