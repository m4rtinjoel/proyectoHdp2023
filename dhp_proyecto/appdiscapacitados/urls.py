from django.urls import path
from .views import *
urlpatterns=[
    path('/resumen',Publicacion,name="publicacion"),
]