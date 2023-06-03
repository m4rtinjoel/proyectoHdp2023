from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True, null=False ,unique=True)
    nombre= models.CharField(max_length=30, null=False)
    apellido= models.CharField(max_length=30, null=False)
    correo=models.EmailField(max_length=25, null= False)
    estado_autor=models.BooleanField('Activo/No Activo',null=False,default=True)

    def __str__(self):
      return self.nombre
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'
        ordering=['nombre']

class Categoria(models.Model):
    id_categoria=models.AutoField(primary_key=True, null=False, unique=True)
    nombre_categoria=models.CharField(max_length=60, null=False)
    estado_categoria=models.BooleanField('Activo/No Activo', null=False,default=True)

    def __srt__(self):
        return self.nombre_categoria
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['nombre_categoria']

class Publicacion(models.Model):
    id_publicacion=models.AutoField(primary_key=True, null=False, unique=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE, null=False)
    titulo_publicacion=models.CharField(max_length=60, null=False)
    estado_publicacion=models.BooleanField('Activo/No Activo',null=False,default=True)
    imagen=models.ImageField(upload_to='publicaciones/',null=True,blank=True)
    descripcion_publicacion=models.CharField(max_length=2000, null=False)
    fecha_creacion=models.DateField( null=False)

    def __str__(self):
        return self.titulo_publicacion

    class Meta:
        verbose_name='Publicacion'
        verbose_name_plural='Publicaciones'
        ordering=['titulo_publicacion']

class Tablas(models.Model):
    id_tablas=models.AutoField(primary_key=True, null=False, unique=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    tipo=models.CharField(max_length=40, null=False)
    descripcion_tabla=models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name='Tabla'
        verbose_name_plural='Tablas'
        ordering=['tipo']

class CondicionEconomicaPorDiscapacidad(models.Model):
    id_condicion=models.AutoField(primary_key=True, null=False, unique=True)
    tablas=models.ForeignKey(Tablas, on_delete=models.CASCADE, null=False)
    tipo_discapacidad=models.CharField(max_length=50, null=False)
    estado_discapacidad=models.CharField(max_length=50, null=False)
    cantidad_condicion=models.IntegerField(null=False)
    porcentaje_economica=models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.tipo_discapacidad

    class Meta:
        verbose_name='Condicion Economica por discapacidad'
        verbose_name_plural='Condicion Economica por discapacidad'
        ordering=['tipo_discapacidad']

class CondicionActividadEconomica(models.Model):
    id_actividad=models.AutoField(primary_key=True, null=False, unique=True)
    tabla=models.ForeignKey(Tablas, on_delete=models.CASCADE,null=False)
    estado_economico=models.CharField(max_length=40, null=False)
    situacion_economica=models.CharField(max_length=40, null=False)
    cantidad=models.IntegerField(null=False)
    porcentaje=models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.estado_economico
    
    class Meta:
        verbose_name='Condicion Actividad Economica'
        verbose_name_plural='Condicion Actividad Economica'
        

class InformacionGrafica(models.Model):
    id_grafica=models.AutoField(primary_key=True, null=False, unique=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    titulo=models.CharField(max_length=50, null=False)
    fecha_creacion=models.DateField(null=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Informacion gráfica'
        verbose_name_plural='Información gráfica'
        

class DiscapacitadoPorGenero(models.Model):
    id_discapacidad=models.AutoField(primary_key=True, null=False, unique=True)
    grafica=models.ForeignKey(InformacionGrafica, on_delete=models.CASCADE, null=False)
    genero=models.CharField(max_length=25, null=False)
    estado_discapacitado=models.CharField(max_length=40, null=False)
    porcentaje_discapacidad=models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name='Discapacitado Por Genero'
        verbose_name_plural='Discapacitado Por Genero'
        ordering=['genero']

class ParticipacionPorDiscapacidad(models.Model):
    id_participacion=models.AutoField(primary_key=True, null=False, unique=True)
    grafica=models.ForeignKey(InformacionGrafica, on_delete=models.CASCADE, null=False)
    tipo_discapacidad=models.CharField(max_length=50, null=False)
    porcentaje_participacion=models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.tipo_discapacidad

    class Meta:
        verbose_name='Participacion Por Discapacidad'
        verbose_name_plural='Participacion Por Discapacidad'
        ordering=['tipo_discapacidad']
