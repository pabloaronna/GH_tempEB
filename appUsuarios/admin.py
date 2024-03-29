from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from appUsuarios.models import Usuario, Profile


class UsuarioAdmin(BaseUserAdmin):
	fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
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
admin.site.register(Profile)
