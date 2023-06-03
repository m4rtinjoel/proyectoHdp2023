from django.shortcuts import render
from .models import Publicacion
from .models import CondicionEconomicaPorDiscapacidad
from .models import CondicionActividadEconomica
from .models import DiscapacitadoPorGenero
from .models import ParticipacionPorDiscapacidad


# Create your views here.
def publicacion(request):
    publicaciones=Publicacion.objects.all()
    return render(request,'paginas/publicacion.html',{'publicaciones':publicaciones})


def inicio(request):
    return render(request, 'paginas/inicio.html')

def graficos(request):
    gra1 = DiscapacitadoPorGenero.objects.all()
    nombres1 = ""
    dat1 = ""
    for elemento in gra1:
        nombres1 = nombres1 + "'" + elemento.estado_discapacitado + "',"
        dat1 = dat1 + elemento.porcentaje_discapacidad + ","

    gra2 = ParticipacionPorDiscapacidad.objects.all()
    nombres2 = ""
    dat2 = ""
    for elemento in gra2:
        nombres2 = nombres2 + "'"+ elemento.tipo_discapacidad + "',"
        dat2 = dat2 + elemento.porcentaje_participacion +","
    return render(request, 'paginas/graficos.html',{"gra1":gra1,"nombres1":nombres1,"dat1":dat1,"gra2":gra2,"nombres2":nombres2,"dat2":dat2})

def tablas(request):
    datos1 = CondicionEconomicaPorDiscapacidad.objects.all()
    datos2 = CondicionActividadEconomica.objects.all()
    return render(request,'paginas/tablas.html',{'datos1':datos1,'datos2':datos2})
