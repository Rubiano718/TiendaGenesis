from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse

def contacto(request):
    form = FormularioContacto(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['email']
            contenido = form.cleaned_data['contenido']

            msg = EmailMessage(
                subject="Mensaje desde la web TiendaGenesis",
                body=f"El usuario {nombre} cuyo correo es {correo} escribió:\n\n{contenido}",
                from_email="camilo.rubiano@estudiantesunibague.edu.co",   # <-- IMPORTANTÍSIMO
                to=["camilo.rubiano@estudiantesunibague.edu.co"],         # <-- Te llegará a ti
                reply_to=[correo],
            )

            try:
                msg.send(fail_silently=False)
                return redirect(reverse('Contacto') + '?ok=1')
            except Exception as e:
                print("Error al enviar:", e)
                return redirect(reverse('Contacto') + '?ok=0')

    return render(request, "contacto/contacto.html", {'formulario': form})
