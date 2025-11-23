from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tienda.models import Producto, CategoriaProducto


# -----------------------------
# 🔹 Vista principal de tienda
# -----------------------------
def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()
    return render(request, "tienda/tienda.html", {
        "productos": productos,
        "categorias": categorias
    })


# -----------------------------
# 🔹 Vista de productos por categoría
# -----------------------------
def categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaProducto, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = CategoriaProducto.objects.all()

    return render(request, "tienda/categorias.html", {
        "categoria": categoria,
        "productos": productos,
        "categorias": categorias
    })


# ---------------------------------------------------------
# 🔥 Vista temporal para limpiar rutas antiguas del campo imagen
# ---------------------------------------------------------
def limpiar_imagenes(request):
    """
    Esta vista elimina rutas viejas como 'tienda/archivo.png'
    que quedaron de Cloudinary o del FileField anterior.
    Después podrás poner rutas de /static/productos/ sin errores.
    """
    productos = Producto.objects.all()
    count = 0

    for p in productos:
        # Detectar rutas viejas provenientes del FileField
        if p.imagen and ("tienda/" in p.imagen or "media/" in p.imagen):
            p.imagen = ""   # limpiar
            p.save()
            count += 1

    return HttpResponse(f"Rutas antiguas eliminadas del campo imagen: {count}")




