from django.db import models

# Create your models here.
# tienda/models.py
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    asset = models.URLField()
    estado = models.IntegerField()

class Boleta(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=3)
    codigo_seguimiento = models.CharField(max_length=50, null=True)
    nombre_comprador = models.CharField(max_length=255)
    direccion_comprador = models.TextField()
    estado = models.CharField(max_length=255, null=True, blank=True)
    proveedor_transporte = models.CharField(max_length=255, null=True, blank=True, default='MusicPro')

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=3)