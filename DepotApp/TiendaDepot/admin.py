from django.contrib import admin

# Register your models here.
from .models import Articulo

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Articulo,ArticuloAdmin)