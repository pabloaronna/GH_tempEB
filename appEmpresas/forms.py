from django import forms
from .models import Empresas
from PIL import Image



class EmpresasModelForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre', 'telefono','imagen_cabecera','imagen_logo','slug']

    def save(self, commit=True):
        empresa = super(EmpresasModelForm, self).save()

        if empresa.imagen_logo:
            imageL = Image.open(empresa.imagen_logo)
            w, h = imageL.size
            if w>800:
                h=int(800*h/w)
                w=800
            elif h>800:
                w=int(800*w/h)
                h=800

            #cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = imageL.resize((w, h), Image.ANTIALIAS)
            resized_image.save(empresa.imagen_logo.path)

        if empresa.imagen_cabecera:
            imageC = Image.open(empresa.imagen_cabecera)
            w, h = imageC.size
            if w>800:
                h=int(800*h/w)
                w=800
            elif h>800:
                w=int(800*w/h)
                h=800

            #cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = imageC.resize((w, h), Image.ANTIALIAS)
            resized_image.save(empresa.imagen_cabecera.path)

        return empresa