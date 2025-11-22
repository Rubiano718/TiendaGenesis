from django import forms
from django.core.validators import RegexValidator, EmailValidator


class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre", required=True, validators=[ RegexValidator(
    regex=r"^[A-Za-zÀ-ÖØ-öø-ÿÁÉÍÓÚáéíóúÜüÑñ' -]+$",
    message="Solo se permiten letras, espacios, guiones y apóstrofes."
    )],
        widget=forms.TextInput(attrs={
            "placeholder": "Tu nombre",
            "pattern": r"[A-Za-zÀ-ÖØ-öø-ÿÁÉÍÓÚáéíóúÜüÑñ' -]+",
            "title": "Solo letras, espacios, guiones y apóstrofes"
        }))

    email = forms.EmailField(
    label="Email",
    validators=[EmailValidator(), RegexValidator(
        regex=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
    )], widget=forms.TextInput(attrs={
            "placeholder": "Tu Correo"})
)

    contenido = forms.CharField(label="Contenido", widget=forms.Textarea(attrs={
        "placeholder": "Escribe Aqui Alguna Recomendacion o Queja"}), required=True)