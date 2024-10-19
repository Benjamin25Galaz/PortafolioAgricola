# Generated by Django 3.1.2 on 2024-10-15 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
                ('confirmar_contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_solicitud', models.CharField(choices=[('retiro_aguas_piscina', 'Retiro de aguas de piscinas'), ('retiro_arboles', 'Retiro de árboles')], max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=100)),
                ('fecha_retiro', models.DateField()),
                ('cantidad_arboles', models.IntegerField(blank=True, null=True)),
                ('cantidad_litros', models.IntegerField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.tema')),
            ],
        ),
    ]