from django.contrib import admin

# Register your models here.
from .models import Articulo, Pedido

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Articulo,ArticuloAdmin)

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=("created",)

admin.site.register(Pedido,PedidoAdmin)
