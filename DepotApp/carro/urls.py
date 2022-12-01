from django.urls import path
from . import views

app_name="carro"

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregar/<int:articulo_id>/', views.agregar_articulo, name="agregar"),
    path('restar/<int:articulo_id>/', views.restar_articulo, name="restar"),
    path('okpedido', views.okPedido, name="okPedido"),
]