from django.shortcuts import render
from django.shortcuts import redirect
from enemigosapp.models import Enemigo
from enemigosapp.forms import FormEnemigo
# Create your views here.
def index(request):
    return render(request, 'enemigosapp/index.html')

def listarEnemigos(request):
    enemigos = Enemigo.objects.all()
    data = {'enemigos' : enemigos}
    return render(request, 'enemigosapp/listarEnemigos.html', data)

def agregarEnemigo(request):
    form = FormEnemigo()
    if request.method == 'POST':
        form = FormEnemigo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarEnemigo.html', data)

def eliminarEnemigo(request, id):
    enemigo = Enemigo.objects.get(id = id)
    enemigo.delete()
    return redirect('/listarEnemigos')