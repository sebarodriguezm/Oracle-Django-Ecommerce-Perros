from django.urls import path
from . import views



urlpatterns = [
  path('', views.home, name="home"),
  path('tienda/', views.tienda, name="tienda"),
  path('historia/', views.historia, name="historia"),
  path('registro/', views.registro, name="registro"),
  path('listar/', views.listar, name="listar"),
  path('editar_raza/<id>/', views.editar_raza, name="editar_raza"),
  path('eliminar_raza/<id>/', views.eliminar_raza, name="eliminar_raza"),
  path('agregar_raza/', views.agregar_raza, name="agregar_raza"),
  path('agregar_marca/', views.agregar_marca, name="agregar_marca"),
  path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
]