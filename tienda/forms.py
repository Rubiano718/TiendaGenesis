from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Producto

class ProductoForm(forms.ModelForm):
    imagen = CloudinaryFileField(
        options={
            'folder': "productos"
        },
        required=False
    )

    class Meta:
        model = Producto
        fields = "__all__"
