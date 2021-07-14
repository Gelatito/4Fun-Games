# Generated by Django 3.2.4 on 2021-07-14 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('CategoriaDejuego', models.CharField(max_length=50, verbose_name='Categoria del juego')),
            ],
        ),
        migrations.CreateModel(
            name='Pag1juegos',
            fields=[
                ('Codigo', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='CodigoJuego')),
                ('NombreDelJuego', models.CharField(max_length=50, verbose_name='NombreDeljuego')),
                ('CompañiaCreadora', models.CharField(max_length=50, verbose_name='CompañiaCreadora')),
                ('Plataforma', models.CharField(blank=True, max_length=50, null=True, verbose_name='Plataforma')),
                ('Descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('Caratula', models.ImageField(null=True, upload_to='Caratulas')),
                ('Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categorias')),
            ],
        ),
    ]
