from django.contrib import admin
from django.urls import path, include
from tienda.views import limpiar_imagenes   # 👈 IMPORTACIÓN NUEVA

urlpatterns = [
    path('', include('TiendaGenesisApp.urls')),   # HOME
    path('admin/', admin.site.urls),

    path('tienda/', include('tienda.urls')),
    path('carrito/', include('carrito.urls')),
    path('contacto/', include('contacto.urls')),
    path('informacion/', include('informacion.urls')),

    # 👇 LOGIN / LOGOUT
    path('accounts/', include('allauth.urls')),

    # 👇 URL TEMPORAL PARA LIMPIAR EL CAMPO IMAGEN
    path('limpiar/', limpiar_imagenes),
]
