# Generated by Django 3.1 on 2023-05-31 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appdiscapacitados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre_categoria', models.CharField(max_length=60)),
                ('estado_categoria', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InformacionGrafica',
            fields=[
                ('id_grafica', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='estado',
            new_name='estado_autor',
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='autor',
            name='correo',
            field=models.EmailField(max_length=25),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Tablas',
            fields=[
                ('id_tablas', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(max_length=40)),
                ('descripcion_tabla', models.CharField(max_length=200)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.autor')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id_resumen', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sintesis', models.CharField(max_length=10000)),
                ('referencias', models.CharField(max_length=1000)),
                ('estado', models.BooleanField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo_publicacion', models.CharField(max_length=60)),
                ('estado_publicacion', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion_publicacion', models.CharField(max_length=2000)),
                ('fecha_creacion', models.DateField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.autor')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionPorDiscapacidad',
            fields=[
                ('id_participacion', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo_discapacidad', models.CharField(max_length=50)),
                ('porcentaje_participacion', models.CharField(max_length=5)),
                ('id_grafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.informaciongrafica')),
            ],
        ),
        migrations.AddField(
            model_name='informaciongrafica',
            name='id_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.autor'),
        ),
        migrations.AddField(
            model_name='informaciongrafica',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.categoria'),
        ),
        migrations.CreateModel(
            name='DiscapacitadoPorGenero',
            fields=[
                ('id_discapacidad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('genero', models.CharField(max_length=25)),
                ('estado_discapacitado', models.CharField(max_length=40)),
                ('porcentaje_discapacidad', models.CharField(max_length=5)),
                ('id_grafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.informaciongrafica')),
            ],
        ),
        migrations.CreateModel(
            name='CondicionEconomicaPorDiscapacidad',
            fields=[
                ('id_condicion', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo_discapacidad', models.CharField(max_length=50)),
                ('estado_discapacidad', models.CharField(max_length=50)),
                ('cantidad_condicion', models.IntegerField()),
                ('porcentaje_economica', models.CharField(max_length=5)),
                ('id_tablas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.tablas')),
            ],
        ),
        migrations.CreateModel(
            name='CondicionActividadEconomica',
            fields=[
                ('id_actividad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('estado_economico', models.CharField(max_length=40)),
                ('situacionEconomica', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
                ('porcentaje', models.CharField(max_length=5)),
                ('id_tablas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdiscapacitados.tablas')),
            ],
        ),
    ]
