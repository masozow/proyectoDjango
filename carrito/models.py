from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)

    def publish(self):
        self.save()

    def eliminar(sekf):
        self.delete()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    cliente = models.CharField(max_length=200)
    tarjeta_credito = models.CharField(max_length=100)
    direccion_entrega = models.TextField()
    telefonos_cliente = models.CharField(max_length=30)
    fecha_compra = models.DateTimeField(
        default=timezone.now)
    cod_producto = models.ForeignKey(Producto)
    
    def almacenar(self):
        self.save()

    def eliminar(self):
        self.delete()

    def __str__(self):
        return self.pk
