from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class CategoriaProducto(models.Model):

    nombre = models.CharField(max_length=50, validators=[RegexValidator(
    regex=r"^[A-Za-zÁÉÍÓÚáéíóúÜüÑñ' -]+$",
    message="Solo se permiten letras, espacios, guiones y apóstrofes."
    )])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CategoriaProducto"
        verbose_name_plural = "CategoriasProducto"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):

    TALLAS = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    nombre = models.CharField(max_length=50, validators=[RegexValidator(
    regex=r"^[A-Za-zÁÉÍÓÚáéíóúÜüÑñ' -]+$",
    message="Solo se permiten letras, espacios, guiones y apóstrofes."
    )])
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda")
    precio = models.FloatField()
    talla = models.CharField(max_length=3, choices=TALLAS, default='M')
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
