from django.urls import path
from PetShop.views import  producto_filtro, contacto, servicios

urlpatterns = [
    path("productos_filtrar", producto_filtro, name="formulario"),
    path("", producto_filtro, name="inicio"),
    path("contacto", contacto, name="contactos"),
    path("servicios", servicios, name="servicios")
    
]
