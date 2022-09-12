from django.shortcuts import render
from PetShop.models import *
from PetShop.forms import *
from django.http import *
from Auten.forms import*
from Auten.models import *
from django.contrib.auth.decorators import*


def producto_filtro(request):
    listado_productos = Productos.objects.all()
    
    if request.GET.get("nombre_producto"):
        formulario = FormularioFiltro(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Productos.objects.filter(nombre__icontains = data["nombre_producto"])
        
        return render(request, "Proyecto/Productos.html", {"productos": listado_productos})
   
    else :
        formulario = FormularioFiltro()
        return render (request, "Proyecto/Productos.html", {"productos": listado_productos, "formulario":formulario})
    
    
def inicio(request):
    
     avatar = Avatar.objects.filter(usuario = request.user).first()
     context = {'imagen': avatar.imagen.url}
        
     return render(request, "Proyecto/base.html", context)

def servicios(request):
    menu1 = Servicios.objects.all()
    return render(request, "Proyecto/Servicios.html", {"servicios":menu1})

def contacto(request):
   menu2 = Contacto.objects.all()
   return render(request, "Proyecto/Contacto.html", {"contactos":menu2})

@login_required
def agregar_avatar(request):
    
    if request.method == "GET":
        form = AvatarForm()
        contexto ={"form": form}
        return render(request, "Proyecto/editar_avatar.html", contexto)
        

