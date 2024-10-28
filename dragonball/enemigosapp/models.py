from django.db import models

# Create your models here.
class Enemigo(models.Model):
    nombre = models.CharField(max_length=50)
    nivel_de_poder = models.IntegerField(default = 0)
    asesinatos = models.IntegerField(default=0)
    veces_que_ha_muerto = models.IntegerField(default = 0)
    raza = models.CharField(max_length=50)
    organizacion = models.CharField(max_length=50)
    planetas_destruidos = models.IntegerField(default=0)