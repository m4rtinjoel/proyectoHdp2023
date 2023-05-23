from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True, null=False ,unique=True)
    nombre= models.CharField(max_length=20, null=False)
    apellido= models.CharField(max_length=20, null=False)
    correo=models.EmailField(max_length=256, null= False)
    estado=models.BooleanField()
