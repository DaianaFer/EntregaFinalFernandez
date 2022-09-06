from django.urls import path
from Auten.views import login_view, register_views, logout_view, About

urlpatterns = [
    path("logeo",login_view , name="login"),
    path("registro/", register_views, name= "registro"),
    path("salir/", logout_view, name="salir"),
    path("About/", About, name="sobreMi")
]
