from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Tablas)
admin.site.register(CondicionEconomicaPorDiscapacidad)
admin.site.register(CondicionActividadEconomica)
admin.site.register(InformacionGrafica)
admin.site.register(DiscapacitadoPorGenero)
admin.site.register(ParticipacionPorDiscapacidad)

