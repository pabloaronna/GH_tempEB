from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Usuario
from django.forms import ModelForm
from PIL import Image
    

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'imagen', 'telefono', 'dni','latitud',
		'longitud', 'fecha_nacimiento']
        #exclude['is_admin']

    def save(self):
        perfil = super(ProfileForm, self).save()

        if perfil.imagen:
            image = Image.open(perfil.imagen)
            w, h = image.size
            if w>800:
                h=int(800*h/w)
                w=800
            elif h>800:
                w=int(800*w/h)
                h=800

            #cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = image.resize((w, h), Image.ANTIALIAS)
            resized_image.save(perfil.imagen.path)

        return perfil


    