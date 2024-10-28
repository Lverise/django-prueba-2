
from django.contrib import admin
from django.urls import path
from enemigosapp.views import ( index, listarEnemigos, agregarEnemigo, eliminarEnemigo, actualizarEnemigo,  )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('listarEnemigos/', listarEnemigos),
    path('agregarEnemigo', agregarEnemigo),
    path('eliminarEnemigo/<int:id>', eliminarEnemigo),
    path('actualizarEnemigo/<int:id>', actualizarEnemigo),
]
