# Generated by Django 5.0.6 on 2024-09-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinas', '0007_alter_ultimapreventiva_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultimapreventiva',
            name='modelo',
            field=models.CharField(default='', max_length=100, verbose_name='Modelo de máquina'),
        ),
    ]
