from django.db import models
from estructura.models import Usuario, Area, Cat_Externo

# Create your models here.
class Cat_Categoria(models.Model):
    descripcion     = models.CharField(max_length=120)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    

class Cat_Marca(models.Model):
    nombre          = models.CharField(max_length=128, null=False)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Cat_Modelo(models.Model):
    nombre          = models.CharField(max_length=128, null=False)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Cat_Proveedor(models.Model):
    nombre          = models.CharField(max_length=128, null=False)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class Bien(models.Model):
    no_serie        = models.CharField(max_length=128, unique=True)
    descripcion     = models.CharField(max_length=255)
    marca           = models.ForeignKey(Cat_Marca, null= True, on_delete=models.CASCADE, blank = True)
    modelo          = models.ForeignKey(Cat_Modelo, null= True, on_delete=models.CASCADE, blank = True)
    proveedor       = models.ForeignKey(Cat_Proveedor, null= True, on_delete=models.CASCADE, blank = True)
    area_it         = models.ForeignKey(Area, null = True, on_delete=models.CASCADE, blank = True)
    categoria       = models.ForeignKey(Cat_Categoria, null = False, on_delete=models.CASCADE)
    fecha_ingreso   = models.DateTimeField(verbose_name='fecha ingreso', auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    mac_address     = models.CharField(max_length=15, unique=True, null=True)
    ip_address      = models.GenericIPAddressField(null=True)
    motivo_baja     = models.TextField()
    fecha_baja      = models.DateTimeField(blank = True, null = True)
    observaciones   = models.TextField()
    externo         = models.ForeignKey(Cat_Externo, null=True, on_delete=models.CASCADE)
    creador         = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Telefono(models.Model):
    id_telefono         = models.OneToOneField(Bien, on_delete=models.CASCADE)
    is_active       = models.BooleanField(default=True)
    extension       = models.IntegerField(null=True)
    nombre_ext      = models.CharField(max_length=255)

    def __str__(self):
        return self.id_telefono
        

class Resguardo(models.Model):
    bien            = models.ForeignKey(Bien, on_delete=models.CASCADE)
    usuario         = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_alta      = models.DateField(auto_now_add=True)
    fecha_baja      = models.DateField()
    is_active       = models.BooleanField(default=True)
    observaciones   = models.TextField()


    def __str__(self):
        return self.bien


class Documento(models.Model):
    propietario    = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre         = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
