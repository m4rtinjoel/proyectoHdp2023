from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns=[
    path('',inicio, name='inicio'),
    path('graficos', graficos, name='graficos'),
    path('tablas',tablas, name='tablas'),
    path('resumen',publicacion,name="publicacion"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)