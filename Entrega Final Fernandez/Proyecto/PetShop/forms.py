from django.forms import Form, CharField

class FormularioFiltro(Form):
    nombre_producto = CharField(max_length=100)
    
