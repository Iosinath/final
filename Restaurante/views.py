from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Menu
from .forms import MenuForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request): 
    return render(request, 'paginas/nosotros.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def chefs(request):
    return render(request, 'paginas/chefs.html')

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus/index.html', {'menus': menus})

def crear(request):
    formulario = MenuForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('menus')
    return render(request, 'menus/crear.html', {'formulario': formulario})

def editar(request, ID):
    menu = Menu.objects.get(ID=ID)
    formulario = MenuForm(request.POST or None, request.FILES or None, instance=menu)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('menus')
    return render(request,'menus/editar.html',{'formulario':formulario})

def eliminar(request, ID):
    menu = Menu.objects.get(ID=ID)
    menu.delete()
    return redirect('menus')
