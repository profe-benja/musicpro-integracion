from django.contrib import admin
from django.urls import path

from tienda.views import musicpro_productos, musicpro_transporte_estado, listar_productos, pagar, boletas,musicpro_transporte

urlpatterns = [
    path('listar_productos', listar_productos, name="listar_productos"),
    path('pagar', pagar, name="pagar"),
    path('boletas', boletas, name="boletas"),
    
    
    
    path('musicpro_productos', musicpro_productos, name="musicpro_productos"),
    path('musicpro_transporte', musicpro_transporte, name="musicpro_transporte"),
    path('musicpro_transporte_estado', musicpro_transporte_estado, name="musicpro_transporte_estado"),
]
