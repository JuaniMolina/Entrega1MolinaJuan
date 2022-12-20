from django.shortcuts import render
from .models import Persona, Pais, ClubFutbol
from django.http import HttpResponse

from .forms import PersonaForm, PaisForm, ClubFutbolForm

# Create your views here.
def inicio(request):
    return render (request, 'FutbolApp/inicio.html')

def padre (request):
    return render (request, 'FutbolApp/padre.html')

def jugadores (request):
    return render (request, 'FutbolApp/jugadores.html')

def clubes (request):
    return render (request, 'FutbolApp/clubes.html')

def jugadoresFormulario (request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            fechaNacimiento = informacion["fechaNacimiento"]
            nacionalidad = informacion["nacionalidad"]
            tamanio = informacion["tamanio"]
            peso = informacion["peso"]

            jugador = Persona(nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, nacionalidad=nacionalidad, tamanio=tamanio, peso=peso)
            jugador.save()

            return render (request, 'FutbolApp/jugadores.html',{"form":form, "mensaje":"Jugador registrado correctamente"})
        else:
            return render (request, 'FutbolApp/jugadoresFormulario.html',{"form":form, "mensaje":"Error al registrar jugador"})
    else:
        formulario = PersonaForm()
        return render (request, 'FutbolApp/jugadoresFormulario.html',{"form":formulario})

def listarJugadores(request):
    jugadores = Persona.objects.all()
    return render (request, 'FutbolApp/jugadoresLista.html',{"jugadores":jugadores})


