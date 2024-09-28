from django.urls import path
from . import views

urlpatterns = [
    path('recursos/', views.listar_recursos, name='listar_recursos'),
    path('recursos/crear/', views.crear_recurso, name='crear_recurso'),
    path('recursos/modificar/<int:id>/', views.modificar_recurso, name='modificar_recurso'),
    path('recursos/eliminar/<int:id>/', views.eliminar_recurso, name='eliminar_recurso'),
]
