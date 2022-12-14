# Generated by Django 4.1 on 2022-09-30 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_delete_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='RESERVA',
            fields=[
                ('RES_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Reserva')),
                ('RES_FECHA_INGRESO', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('RES_FECHA_SALIDA', models.DateField(blank=True, null=True, verbose_name='Fecha de salida')),
                ('RES_CANTIDAD_DIAS', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de dias')),
                ('RES_ASISTENTES', models.TextField(blank=True, help_text='Ingrese nombre y rut de los asistentes a la reserva', null=True, verbose_name='Asistentes')),
                ('RES_VALOR_RESERVA', models.IntegerField(blank=True, null=True, verbose_name='Valor de la reserva')),
                ('RES_DEPARTAMENTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departamento')),
                ('RES_USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'RESERVA',
            },
        ),
    ]
