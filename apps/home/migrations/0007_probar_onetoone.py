# Generated by Django 4.1 on 2022-09-27 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_inventario_inv_departamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PROBAR_ONETOONE',
            fields=[
                ('PRO_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='Id probar')),
                ('PRO_TEXTO', models.CharField(blank=True, max_length=100, null=True)),
                ('PRO_DEP', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PROBAR_ONETOONE_DEPTO', to='home.departamento')),
            ],
            options={
                'db_table': 'PROBAR_ONETOONE',
            },
        ),
    ]