from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('padre/', padre, name='padre'),
    path('clubes/', clubes, name='clubes'),

    path('jugadores/', jugadores, name='jugadores'),
    path('jugadoresFormulario/', jugadoresFormulario, name='jugadoresFormulario'),
    path('listarJugadores/', listarJugadores, name='listarJugadores'),
    path('editarJugador/<id>', editarJugador, name='editarJugador'),
    path('eliminarJugador/<id>', eliminarJugador, name='eliminarJugador'),

    path('clubesFormulario/', clubesFormulario, name='clubesFormulario'),
    path('listarClubes/', listarClubes, name='listarClubes'),
    path('editarClub/<id>', editarClub, name='editarClub'),
    path('eliminarClub/<id>', eliminarClub, name='eliminarClub'),
    path('clubesBuscar/', clubesBuscar, name='clubesBuscar'),
    path('buscar_club/', buscar_club, name='buscar_club'),
]

