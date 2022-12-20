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
            jugadores = Persona.objects.all()
            return render (request, 'FutbolApp/jugadoresLista.html',{"jugadores":jugadores, "parrafo":"Jugador registrado correctamente"})
        else:
            return render (request, 'FutbolApp/jugadoresFormulario.html',{"form":form, "mensaje":"Error al registrar jugador"})
    else:
        formulario = PersonaForm()
        return render (request, 'FutbolApp/jugadoresFormulario.html',{"form":formulario})

def listarJugadores(request):
    jugadores = Persona.objects.all()
    return render (request, 'FutbolApp/jugadoresLista.html',{"jugadores":jugadores})

def editarJugador(request, id):
    jugador = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            jugador.nombre = info["nombre"]
            jugador.apellido = info["apellido"]
            jugador.fechaNacimiento = info["fechaNacimiento"]
            jugador.nacionalidad = info["nacionalidad"]
            jugador.tamanio = info["tamanio"]
            jugador.peso = info["peso"]
            jugador.save()
            jugadores = Persona.objects.all()
            return render (request, 'FutbolApp/jugadoresLista.html',{"jugadores":jugadores, "parrafo":"Jugador editado correctamente"})
        pass
    else:
        form= PersonaForm(initial={"nombre":jugador.nombre, "apellido":jugador.apellido, "fechaNacimiento":jugador.fechaNacimiento, "nacionalidad":jugador.nacionalidad, "tamanio":jugador.tamanio, "peso":jugador.peso})
        return render (request, 'FutbolApp/editarJugador.html',{"form":form, "jugador":jugador})

def eliminarJugador(request, id):
    jugador = Persona.objects.get(id=id)
    jugador.delete()
    jugadores = Persona.objects.all()
    return render (request, 'FutbolApp/jugadoresLista.html',{"jugadores":jugadores, "parrafo":"Jugador eliminado correctamente"})


def clubesFormulario (request):
    if request.method == 'POST':
        form = ClubFutbolForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            pais = informacion["pais"]
            fechaFundacion = informacion["fechaFundacion"]
            estadio = informacion["estadio"]
            club = ClubFutbol(nombre=nombre, pais=pais, fechaFundacion=fechaFundacion, estadio=estadio)
            club.save()
            clubes = ClubFutbol.objects.all()
            return render (request, 'FutbolApp/clubesLista.html',{"clubes":clubes, "parrafo":"Club registrado correctamente"})
        else:
            return render (request, 'FutbolApp/clubesFormulario.html',{"form":form, "mensaje":"Error al registrar club"})
    else:
        formulario = ClubFutbolForm()
        return render (request, 'FutbolApp/clubesFormulario.html',{"form":formulario})

def listarClubes(request):
    clubes = ClubFutbol.objects.all()
    return render (request, 'FutbolApp/clubesLista.html',{"clubes":clubes})

def editarClub(request, id):
    club = ClubFutbol.objects.get(id=id)
    if request.method == 'POST':
        form = ClubFutbolForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            club.pais = info["pais"]
            club.nombre = info["nombre"]
            club.apodo = info["apodo"]
            club.colores = info["colores"]
            club.fundacion = info["fundacion"]
            club.web = info["web"]
            club.diminutivo = info["diminutivo"]
            club.save()
            clubes = ClubFutbol.objects.all()
            return render (request, 'FutbolApp/clubesLista.html',{"clubes":clubes, "parrafo":"Club editado correctamente"})
        pass
    else:
        form= ClubFutbolForm(initial={"pais":club.pais, "nombre":club.nombre, "apodo":club.apodo, "colores":club.colores, "fundacion":club.fundacion, "web":club.web, "diminutivo":club.diminutivo})
        return render (request, 'FutbolApp/editarClub.html',{"form":form, "club":club})

def eliminarClub(request, id):
    club = ClubFutbol.objects.get(id=id)
    club.delete()
    clubes = ClubFutbol.objects.all()
    return render (request, 'FutbolApp/clubesLista.html',{"clubes":clubes, "parrafo":"Club eliminado correctamente"})

def clubesBuscar(request):
    return render (request, 'FutbolApp/clubesBuscar.html')

def buscar_club(request):
    nombre=request.GET["nombre"]
    if nombre != "":
        clubes = ClubFutbol.objects.filter(nombre__contains=nombre)
        return render (request, 'FutbolApp/clubesLista.html',{"clubes":clubes, "parrafo":"Resultado de la busqueda"})
    else:
        return render (request, 'FutbolApp/clubesBuscar.html',{"mensaje":"Debe ingresar un nombre"})

