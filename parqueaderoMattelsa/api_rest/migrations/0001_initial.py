# Generated by Django 3.0.4 on 2020-03-14 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEmp', models.CharField(blank=True, max_length=50)),
                ('cedulaEmp', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'EmpleadoS',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tipoVehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_vehiculo', models.CharField(blank=True, max_length=50)),
                ('foto', models.CharField(max_length=10000, null=True)),
                ('cilindraje', models.CharField(max_length=50, null=True)),
                ('placa', models.CharField(max_length=10, null=True)),
                ('modelo', models.IntegerField()),
                ('numPuertas', models.IntegerField()),
                ('tiempos', models.CharField(max_length=3, null=True)),
                ('Empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.Empleado')),
            ],
            options={
                'verbose_name_plural': 'tipoVehiculos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Parqueadero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('celda', models.IntegerField()),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('cedulaEmp', models.IntegerField()),
                ('tipo_vehiculo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.tipoVehiculo')),
            ],
            options={
                'verbose_name_plural': 'Parqueaderos',
                'ordering': ['id'],
            },
        ),
    ]