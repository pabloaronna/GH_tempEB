from django.db import models
from django.conf import settings
from appUsuarios.models import Usuario

User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
	im = None
	if filename:
		filebase, extension = filename.split(".")
		im = "%s/%s.%s" %("empresas",filebase, extension)
	
	return im

class Empresas(models.Model):
    usuario 				= models.ForeignKey(Usuario, verbose_name=("Usuario"), on_delete=models.CASCADE)
    nombre                  = models.CharField(max_length=50, blank=True)
    telefono				= models.CharField(max_length=20, blank=True)
    latitud				    = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitud				= models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    url_facebook			= models.URLField( max_length=200, blank=True)
    url_Youtube				= models.URLField( max_length=200, blank=True)
    url_Instagram			= models.URLField( max_length=200, blank=True)
    url_Twitter				= models.URLField( max_length=200, blank=True)
    url_web					= models.URLField( max_length=200, blank=True)
    descripcion				= models.TextField(blank=True)
    is_bloqueado			= models.BooleanField(verbose_name="Login Bloqueado", default=False)
    last_update				= models.DateTimeField(auto_now=True)
    date_joined				= models.DateTimeField(verbose_name='Fecha de registro', auto_now_add=True)
    imagen_logo		        = models.ImageField(verbose_name="Logo", upload_to=upload_location, null=True, blank=True)
    imagen_cabecera         = models.ImageField(verbose_name="Imagen de cabecera", upload_to=upload_location, null=True, blank=True)
    slug                    = models.SlugField(unique=True, default='')
    
    def __str__(self):
        return self.nombre

    def get_info_url(self):
        return f"/empresa/info/{self.slug}"

    def get_admin_url(self):
        return f"/empresa/admin/{self.slug}"

    def get_delete_url(self):
        return f"/empresa/delete/{self.slug}"
	

