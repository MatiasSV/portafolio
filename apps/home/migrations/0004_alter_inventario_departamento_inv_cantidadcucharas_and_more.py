# Generated by Django 4.1 on 2022-09-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_inventario_departamento_inv_hornoelectrico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADCUCHARAS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de cucharas'),
        ),
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADCUCHILLOS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de cuchillos'),
        ),
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADSILLAS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de sillas'),
        ),
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADTENEDORES',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de tenedores'),
        ),
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADTOALLAS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de toallas'),
        ),
        migrations.AlterField(
            model_name='inventario_departamento',
            name='INV_CANTIDADVASOS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de vasos'),
        ),
    ]
