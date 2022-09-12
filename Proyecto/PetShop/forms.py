from django.forms import Form, CharField, ImageField

class FormularioFiltro(Form):
    nombre_producto = CharField(max_length=100)
    
    
class AvatarForm(Form):
    imagen = ImageField()    
