from django.shortcuts import render,redirect
from .carro import carro
from TiendaDepot.models import Articulo

def agregar_articulo(request,articulo_id):
    Carro = carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    Carro.agregar(articulo)
    return redirect("Index")

def restar_articulo(request,articulo_id):
    Carro = carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    Carro.restar(articulo)
    return redirect("Index")

def limpiar_carro(request):
    Carro = carro(request)
    Carro.limpiarCarro()
    return redirect("Index")

def carrito(request):
    return render (request, "carro.html")