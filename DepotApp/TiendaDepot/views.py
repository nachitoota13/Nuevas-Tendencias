
from django.shortcuts import render
from TiendaDepot.models import Articulo

def index(request):
    Articulos=Articulo.objects.all().order_by("Nombre")
    return render (request, "index.html", {"articulos":Articulos})

def indexPopu(request):
    articulos=Articulo.objects.all().filter(tipo__contains=2).order_by("Nombre")
    return render (request, "index.html", {"articulos":articulos})
    
def indexPromo(request):
    articulos=Articulo.objects.all().filter(tipo__contains=3).order_by("Nombre")
    return render (request, "index.html", {"articulos":articulos})
    