from django.shortcuts import render
from tienda.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos})




