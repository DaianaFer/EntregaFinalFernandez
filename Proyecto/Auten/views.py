from http.client import *
from django.shortcuts import *

from django.contrib.auth.forms import *
from django.contrib.auth import *
from Auten.forms import *
from django.contrib.auth.decorators import *

from django.views.generic import *
from Auten.models import *
from Auten.forms import *


def About(request):
    return render(request, "Auten/sobreMi.html")
    

def login_view(request):
    
    if request.method== "GET":
        formulario = AuthenticationForm()
        return render(request, "Auten/login.html", {"form": formulario})
    else:
       formulario = AuthenticationForm(request, data=request.POST)
        
       if formulario.is_valid():
           data = formulario.cleaned_data
            
           user = authenticate(username=data.get("username"), password=data.get("password"))
            
           if user is not None:
                login(request, user)
                return redirect("inicio")
            
           else:
               context = {
                   "error": "credenciales no validas",
                    "form": formulario }
                
               return render(request, "Auten/login.html", context )
               
       formulario = AuthenticationForm()        
       return render(request, "Auten/login.html", {"form": formulario, "errores": ["Registro no valido"]})    
      
def logout_view(request):
   
    logout(request)
    return render(request, "Auten/salir.html")
    

def register_views(request):
        
    if request.method == "GET":
        form = UserCustomCreationForm()
        return render(request, "Auten/registro.html", {"registro": form})
                      
    else:
        form = UserCustomCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
    
        return redirect("inicio")    

@login_required
def editar_usuario(request):
   
    if request.method == "GET":
        form = UserEditForm()
        return render(request, "Auten/editar_usuario.html", {"form": form})


