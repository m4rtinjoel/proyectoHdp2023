from django.urls import path
from .views import *

urlpatterns=[
    path('',inicio, name='inicio'),
    path('graficos', graficos, name='graficos'),
    path('tablas',tablas, name='tablas'),
    path('resumen',Publicacion,name="publicacion"),
]