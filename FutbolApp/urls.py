from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('padre/', padre, name='padre'),
    path('jugadores/', jugadores, name='jugadores'),
    path('clubes/', clubes, name='clubes'),
    path('jugadoresFormulario/', jugadoresFormulario, name='jugadoresFormulario'),
    path('listarJugadores/', listarJugadores, name='listarJugadores'),

]