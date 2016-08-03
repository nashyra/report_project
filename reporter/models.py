from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo = models.CharField(max_length=15)
    descripcion = models.TextField()
    
    def __str__(self):
        return "%s -- %s" % (self.codigo, self.descripcion)

class Sabor(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class Galletas(models.Model):
    sabores = models.ManyToManyField(Sabor)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.SmallIntegerField(default=10)
    proveedor = models.ForeignKey(Proveedor)