# Generated by Django 4.1 on 2022-09-26 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='INV_DEPARTAMENTO',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_depto', to='home.departamento'),
        ),
        migrations.DeleteModel(
            name='INVENTARIO_DEPARTAMENTO',
        ),
    ]
