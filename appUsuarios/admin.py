from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from appUsuarios.models import Usuario


class UsuarioAdmin(BaseUserAdmin):
	fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
		('Datos Personales',{'fields':('nombre', 'apellido', 'telefono', 'dni','latitud',
		'longitud', 'fecha_nacimiento')}),
		('Redes Sociales',{'fields':('url_facebook', 'url_Youtube', 'url_Instagram', 'url_Twitter','url_Pinterest',
		'url_web')}),
		('BIO',{'fields':('descripcion',)}),
		('Restriccion de acceso',{'fields':('is_bloqueado', 'is_deuda')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
			'is_admin',
            'groups', 
            'user_permissions',
        )}),
    )

	add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
	
	list_display = ('email', 'name', 'is_staff', 'last_login')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ('groups', 'user_permissions',)





#admin.site.unregister(Usuario)
admin.site.register(Usuario, UsuarioAdmin)
