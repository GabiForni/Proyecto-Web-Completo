from django.shortcuts import render, redirect
from .forms import Formulario_contacto
# Create your views here.

def contacto(request):
    formulario_contacto = Formulario_contacto()
    if request.method == 'POST':
        formulario_contacto = Formulario_contacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            mail = request.POST.get('email')
            contenido = request.POST.get('contenido')

            return redirect('/contacto/?valido')
    return render(request, 'contacto/contacto.html', {'mi_formulario': formulario_contacto})

