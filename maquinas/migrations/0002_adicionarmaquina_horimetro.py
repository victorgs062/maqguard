# Generated by Django 5.0.6 on 2024-09-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adicionarmaquina',
            name='horimetro',
            field=models.IntegerField(default=0, verbose_name='Horimetro atualizado'),
        ),
    ]
