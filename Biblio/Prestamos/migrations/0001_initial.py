# Generated by Django 5.1.3 on 2024-11-14 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('apellido', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('apellido', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateTimeField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.cliente')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_multa', models.DateField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos.prestamo')),
            ],
        ),
    ]