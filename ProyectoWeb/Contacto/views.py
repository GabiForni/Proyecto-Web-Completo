from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage
from django.conf import settings
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
            'El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}'
            .format(nombre, email, contenido), '',[settings.EMAIL_HOST_USER], reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?no_valido')
    return render(request, 'contacto/contacto.html', {'mi_formulario': formulario_contacto})

