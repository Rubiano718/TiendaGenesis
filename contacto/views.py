from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contacto(request):
    form = FormularioContacto(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            nombre   = form.cleaned_data['nombre']
            correo   = form.cleaned_data['email']       
            contenido = form.cleaned_data['contenido']

            msg = EmailMessage(
                subject="Mensaje desde App Django",
                body=f"El usuario {nombre} cuya dirección es {correo} escribe:\n\n{contenido}",
                from_email="",                           
                to=["genesisclothing04@gmail.com"],
                reply_to=[correo],
            )

            try:
                
                msg.send(fail_silently=False)
                return redirect(reverse('Contacto') + '?ok=1')
            except Exception as e:
            
                return redirect(reverse('Contacto') + '?ok=0')


    return render(request, "contacto/contacto.html", {'formulario': form})