from django.contrib import admin
from enemigosapp.models import Enemigo

class EnemigoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel_de_poder', 'asesinatos', 'veces_que_ha_muerto', 'raza', 'organizacion', 'planetas_destruidos']

# Register your models here.
admin.site.register(Enemigo)