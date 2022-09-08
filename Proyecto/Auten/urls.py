from django.urls import path
from Auten.views import login_view, register_views, logout_view, About,editar_usuario
from django.contrib.auth.views import *

urlpatterns = [
    path("About/", About, name="sobreMi"),
   
    path("logeo",login_view , name="login"),
    path("registro/", register_views, name= "registro"),
    path("salir/", LogoutView.as_view(template_name="Auten/salir.html"), name="salir"),
    path("edit/", editar_usuario, name= "editar_usuario")
    
]
