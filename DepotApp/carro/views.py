from django.shortcuts import render,redirect
from .carro import carro
from TiendaDepot.models import Articulo, Pedido

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

def okPedido(request):
    if request.user.is_authenticated:

        for key, value in request.session["carro"].items():
            usuario=request.user
            nombreArticulo=value["nombre"]
            precio=value["precio"]
            cantidad=value["cantidad"]
            pedido= Pedido.objects.create(Usuario=usuario, NombreArticulo=nombreArticulo, Precio=precio, Cantidad=cantidad)
        limpiar_carro(request)
        return render (request,"pedido.html")
    else:
        return render (request, "autenticar.html")