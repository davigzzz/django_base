from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import Area, Usuario




class AdminUsuario(UserAdmin):
    list_display    = ('usuario', 'nombre', 'a_paterno', 'a_materno', 'area', 'id_empleado', 'is_active')
    search_fields   = ('usuario', 'nombre', 'a_paterno', 'a_materno', 'area__nombre', 'id_empleado')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario

    filter_horizontal = ()
    list_filter = ('is_active', 'area')
    fieldsets = (
        (None, {
            'fields': ('usuario', 'password', 'nombre', 'a_paterno', 'a_materno', 'id_empleado', 'correo')
        }),
        ('Avanzado', {
            'classes': ('collapse',),
            'fields': ('rfc', 'area'),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('id_empleado','usuario', 'password1', 'password2', 'nombre', 'a_paterno', 'a_materno', 'correo', 'rfc', 'area' ,'date_joined', 'last_login', 'is_admin' ,'is_active' ,'is_staff' ,'is_superuser')
        }),
    )

    ordering = ('usuario',)

class AdminArea(admin.ModelAdmin):
    list_display = ('id_area', 'nombre', 'siglas', 'superior', 'is_active')
    search_fields = ('id_area', 'nombre', 'siglas')
    readonly_fields = ()
    list_filter = ('is_active',)
    ordering = ('id_area',)

# Register your models here.
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Area, AdminArea)