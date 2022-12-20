from django.contrib import admin
from .models import Persona, Pais, ClubFutbol

# Register your models here.

admin.site.register(Persona)
admin.site.register(Pais)
admin.site.register(ClubFutbol)