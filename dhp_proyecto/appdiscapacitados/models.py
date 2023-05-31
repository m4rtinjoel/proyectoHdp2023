from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True, null=False ,unique=True)
    nombre= models.CharField(max_length=30, null=False)
    apellido= models.CharField(max_length=30, null=False)
    correo=models.EmailField(max_length=25, null= False)
    estado_autor=models.BooleanField(null=False)

class Resumen(models.Model):
    id_resumen=models.AutoField(primary_key=True, null=False ,unique=True)
    id_autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    sintesis=models.CharField(max_length=10000, null=False)
    referencias=models.CharField(max_length=1000, null=False)
    estado=models.BooleanField(null=False)

class Categoria(models.Model):
    id_categoria=models.AutoField(primary_key=True, null=False, unique=True)
    nombre_categoria=models.CharField(max_length=60, null=False)
    estado_categoria=models.BooleanField( null=False)

class Publicacion(models.Model):
    id_publicacion=models.AutoField(primary_key=True, null=False, unique=True)
    id_autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    id_categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE, null=False)
    titulo_publicacion=models.CharField(max_length=60, null=False)
    estado_publicacion=models.BooleanField(null=False)
    imagen=models.ImageField(null=False)
    descripcion_publicacion=models.CharField(max_length=2000, null=False)
    fecha_creacion=models.DateField( null=False)

class Tablas(models.Model):
    id_tablas=models.AutoField(primary_key=True, null=False, unique=True)
    id_autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    tipo=models.CharField(max_length=40, null=False)
    descripcion_tabla=models.CharField(max_length=200, null=False)

class CondicionEconomicaPorDiscapacidad(models.Model):
    id_condicion=models.AutoField(primary_key=True, null=False, unique=True)
    id_tablas=models.ForeignKey(Tablas, on_delete=models.CASCADE, null=False)
    tipo_discapacidad=models.CharField(max_length=50, null=False)
    estado_discapacidad=models.CharField(max_length=50, null=False)
    cantidad_condicion=models.IntegerField(null=False)
    porcentaje_economica=models.CharField(max_length=5, null=False)

class CondicionActividadEconomica(models.Model):
    id_actividad=models.AutoField(primary_key=True, null=False, unique=True)
    id_tablas=models.ForeignKey(Tablas, on_delete=models.CASCADE,null=False)
    estado_economico=models.CharField(max_length=40, null=False)
    situacionEconomica=models.CharField(max_length=40, null=False)
    cantidad=models.IntegerField(null=False)
    porcentaje=models.CharField(max_length=5, null=False)

class InformacionGrafica(models.Model):
    id_grafica=models.AutoField(primary_key=True, null=False, unique=True)
    id_autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    titulo=models.CharField(max_length=50, null=False)
    fecha_creacion=models.DateField(null=False)

class DiscapacitadoPorGenero(models.Model):
    id_discapacidad=models.AutoField(primary_key=True, null=False, unique=True)
    id_grafica=models.ForeignKey(InformacionGrafica, on_delete=models.CASCADE, null=False)
    genero=models.CharField(max_length=25, null=False)
    estado_discapacitado=models.CharField(max_length=40, null=False)
    porcentaje_discapacidad=models.CharField(max_length=5, null=False)

class ParticipacionPorDiscapacidad(models.Model):
    id_participacion=models.AutoField(primary_key=True, null=False, unique=True)
    id_grafica=models.ForeignKey(InformacionGrafica, on_delete=models.CASCADE, null=False)
    tipo_discapacidad=models.CharField(max_length=50, null=False)
    porcentaje_participacion=models.CharField(max_length=5, null=False)
