from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Usuario
from django.forms import ModelForm
    

#class SignUpForm(UserCreationForm):
#    class Meta:
#        model = Usuario
#        fields = ('email',)




class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'url_imagen_perfil', 'telefono', 'dni','latitud',
		'longitud', 'fecha_nacimiento']
        #exclude['is_admin']


    