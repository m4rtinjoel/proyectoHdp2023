from django.shortcuts import render

# Create your views here.
def Publicacion(request):
    return render(request,'publicacion.html')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def graficos(request):
    return render(request, 'paginas/graficos.html')

def tablas(request):
    return render(request,'paginas/tablas.html')
