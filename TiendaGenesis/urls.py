from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('TiendaGenesisApp.urls')),   # HOME
    path('admin/', admin.site.urls),

    path('tienda/', include('tienda.urls')),
    path('carrito/', include('carrito.urls')),
    path('contacto/', include('contacto.urls')),
    path('informacion/', include('informacion.urls')),

    # 👇 ESTO ES OBLIGATORIO PARA LOGIN/LOGOUT
    path('accounts/', include('allauth.urls')),
]
