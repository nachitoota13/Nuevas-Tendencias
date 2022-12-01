from django.db import models

# Create your models here.
class Articulo(models.Model):
    Nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="TiendaDepot",null=True, blank=True)
    precio=models.FloatField()
    stock=models.IntegerField()
    TIPO_ARTICULO_CHOICES = [
        (1,'Normal'),
        (2,'Popular'),
        (3,'Promo'),
    ]
    tipo=models.IntegerField(choices=TIPO_ARTICULO_CHOICES, default=1)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'

    def __str__(self):
        return self.Nombre


class Pedido(models.Model):
    Usuario=models.CharField(max_length=50)
    NombreArticulo=models.CharField(max_length=50)
    Precio=models.FloatField()
    Cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural='Pedidos'
    
def __str__(self):
    return self.Usuario+ " "+self.NombreArticulo