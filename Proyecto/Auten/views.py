from http.client import *
from django.shortcuts import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, authenticate, logout
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
            
           user = authenticate(username=data["username"], password=data["password"])
            
           if user is not None:
                login(request, user)
                return redirect("inicio")
            
       formulario = AuthenticationForm()        
       return render(request, "Auten/login.html", {"form": formulario, "errores": ["Registro no valido"]})    
      
def register_views(request):
        
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "Auten/registro.html", {"registro": form})
                      
    else:
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
    
        return redirect("inicio")    
    
def logout_view(request):
   
    logout(request)
    return render(request, "Auten/salir.html")




