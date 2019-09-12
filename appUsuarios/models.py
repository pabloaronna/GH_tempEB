from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone



class UsuarioManager(BaseUserManager):
	def _create_user(self, email, password, is_staff, is_superuser, is_admin, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')
		now = timezone.now()
		email = self.normalize_email(email)
		user = self.model(
			email=email,
			is_staff=is_staff, 
			is_active=True,
			is_admin=is_admin,
			is_superuser=is_superuser, 
			last_login=now,
			date_joined=now, 
			**extra_fields
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password, **extra_fields):
		return self._create_user(email, password, False, False, False, **extra_fields)
		
	def create_superuser(self, email, password, **extra_fields):
		user=self._create_user(email, password, True, True, True, **extra_fields)
		return user


class Usuario(AbstractBaseUser, PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	name 				    = models.CharField(verbose_name='Nombre de usuario',max_length=30, null=True, blank=True)
	date_joined				= models.DateTimeField(verbose_name='Fecha de registro', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='Último login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	nombre                  = models.CharField(max_length=50, blank=True)
	apellido                = models.CharField(max_length=50, blank=True)
	telefono				= models.CharField(max_length=20, blank=True)
	dni 					= models.CharField(max_length=15, blank=True)
	latitud				    = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
	longitud				= models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
	fecha_nacimiento		= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True) #(default=timezone.now)
	url_facebook			= models.URLField( max_length=200, blank=True)
	url_Youtube				= models.URLField( max_length=200, blank=True)
	url_Instagram			= models.URLField( max_length=200, blank=True)
	url_Twitter				= models.URLField( max_length=200, blank=True)
	url_Pinterest			= models.URLField( max_length=200, blank=True)
	url_web					= models.URLField( max_length=200, blank=True)
	descripcion				= models.TextField(blank=True)
	is_bloqueado			= models.BooleanField(verbose_name="Login Bloqueado", default=False)
	is_deuda				= models.BooleanField(verbose_name="Posee Deuda", default=False)


	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UsuarioManager()
	
	def get_absolute_url(self):
		return "/users/%i/" % (self.pk)

	@property
	def nombre_completo(self):
		"retorna - nombre + apellido"
		return '%s %s' % (self.nombre, self.apellido)

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


