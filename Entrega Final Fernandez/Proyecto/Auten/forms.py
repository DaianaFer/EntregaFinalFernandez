from django.forms import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class UserRegister(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2=CharField(label='Repetir Contaseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']