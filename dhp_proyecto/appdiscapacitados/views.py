from django.shortcuts import render

# Create your views here.
def Publicacion(request):
    return render(request,'publicacion.html')

def Graficos(request):
    return render(request, 'graficos.html')
