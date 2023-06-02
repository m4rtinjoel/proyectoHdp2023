# Generated by Django 3.1 on 2023-06-02 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdiscapacitados', '0004_auto_20230602_0448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condicionactividadeconomica',
            old_name='situacionEconomica',
            new_name='situacion_economica',
        ),
        migrations.RenameField(
            model_name='condicionactividadeconomica',
            old_name='id_tablas',
            new_name='tabla',
        ),
        migrations.RenameField(
            model_name='condicioneconomicapordiscapacidad',
            old_name='id_tablas',
            new_name='tablas',
        ),
        migrations.RenameField(
            model_name='discapacitadoporgenero',
            old_name='id_grafica',
            new_name='grafica',
        ),
        migrations.RenameField(
            model_name='informaciongrafica',
            old_name='id_autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='participacionpordiscapacidad',
            old_name='id_grafica',
            new_name='grafica',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='id_autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='resumen',
            old_name='id_autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='tablas',
            old_name='id_autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='tablas',
            old_name='id_categoria',
            new_name='categoria',
        ),
    ]
