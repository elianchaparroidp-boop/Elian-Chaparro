from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all() # Trae todos los dulces de la DB
    return render(request, 'menu/index.html', {'productos': productos})