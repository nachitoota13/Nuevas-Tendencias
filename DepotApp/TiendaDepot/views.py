
from django.shortcuts import render
from TiendaDepot.models import Articulo

def index(request):
    Articulos=Articulo.objects.all().order_by("Nombre")
    return render (request, "index.html", {"articulos":Articulos})