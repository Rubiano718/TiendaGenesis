from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ("nombre", "created", "updated")
    search_fields = ("nombre",)
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "created", "updated")
    list_filter = ("categorias", "created")
    search_fields = ("titulo", "contenido", "autor__username")
    filter_horizontal = ("categorias",)
    readonly_fields = ("created", "updated")

    exclude = ("autor",)

    readonly_fields = ("created", "updated")

    def save_model(self, request, obj, form, change):
     
        if not change or obj.autor_id is None:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        if not request.user.is_superuser:

            return qs.filter(autor=request.user)
    
        return qs
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
