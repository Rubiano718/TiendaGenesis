from django.contrib import admin
from .models import CategoriaProducto, Producto
from .forms import ProductoForm  # ← IMPORTANTE

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm  # ← ESTE FORM HACE QUE CLOUDINARY FUNCIONE
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "categoria", "precio", "talla", "disponibilidad", "created")

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
