from django.shortcuts import render, redirect
from Contacto.forms import Formulario_contacto
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError
from smtplib import SMTPException
# Create your views here.

def contacto(request):
    formulario_contacto = Formulario_contacto()
    if request.method == 'POST':
        formulario_contacto = Formulario_contacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage('Mensaje desde App Django', 
            'El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}'.format(nombre, email, contenido), '',[settings.EMAIL_HOST_USER], reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except SMTPException as e:
                print(f"Error en SMTP: {e}")
                return redirect('/contacto/?no_valido')
    return render(request, 'contacto/contacto.html', {'mi_formulario': formulario_contacto})

