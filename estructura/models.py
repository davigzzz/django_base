from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

class Area(models.Model):
    id_area         = models.IntegerField(primary_key=True)
    nombre          = models.CharField(max_length=255)
    superior        = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    siglas          = models.CharField(max_length=10, default="")
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class MiUsuarioAdmin(BaseUserManager):
    def create_user(self, usuario, correo, id_empleado, nombre, a_paterno, a_materno, password=None):
        if not usuario:
            raise ValueError("Al usuario le falta el usuario")
        if not id_empleado:
            raise ValueError("Falta usuario empleado")
        if not nombre:
            raise ValueError("Falta nombre")
        if not a_paterno:
            raise ValueError("Falta a paterno")
        if not a_materno:
            raise ValueError("Falta a materno")
        if not correo:
            raise  ValueError("Falta el correo")

        user = self.model(
            usuario = usuario,
            correo = correo,
            id_empleado = id_empleado,
            nombre = nombre,
            a_paterno = a_paterno,
            a_materno = a_materno

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, id_empleado, nombre, a_paterno, a_materno, password):
        user = self.create_user (
            usuario = usuario,
            id_empleado = id_empleado,
            nombre = nombre,
            a_paterno = a_paterno,
            a_materno = a_materno,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser):
    id_empleado     = models.IntegerField(primary_key=True, unique=True)
    usuario         = models.CharField(max_length=255, unique=True)
    nombre          = models.CharField(max_length=255)
    a_paterno       = models.CharField(max_length=255)
    a_materno       = models.CharField(max_length=255)
    correo          = models.EmailField(unique=True)
    rfc             = models.CharField(max_length=13, unique=True, blank = True)
    area            = models.ForeignKey(Area, null = True, on_delete=models.CASCADE, blank = True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)
    USERNAME_FIELD  = 'usuario'
    EMAIL_FIELD     = 'correo'
    REQUIRED_FIELDS = ['id_empleado', 'nombre', 'a_paterno', 'a_materno', 'password']

    objects = MiUsuarioAdmin()

    def __str__(self):
        return self.usuario

    def has_perm(self,perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    

class Cat_Externo(models.Model):
    id_externo     = models.IntegerField(primary_key=True, unique=True)
    usuario         = models.CharField(max_length=255, unique=True)
    nombre          = models.CharField(max_length=255)
    a_paterno       = models.CharField(max_length=255)
    a_materno       = models.CharField(max_length=255)
    correo          = models.EmailField(unique=True)
    rfc             = models.CharField(max_length=13, unique=True, blank = True)


