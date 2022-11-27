from django.db import models

# Create your models here.
class Articulo(models.Model):
    Nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="TiendaDepot",null=True, blank=True)
    precio=models.FloatField()
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'

    def __str__(self):
        return self.Nombre
