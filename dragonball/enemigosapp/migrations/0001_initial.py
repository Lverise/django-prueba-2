# Generated by Django 3.2 on 2024-10-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enemigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nivel_de_poder', models.IntegerField(default=0)),
                ('asesinatos', models.IntegerField(default=0)),
                ('veces_que_ha_muerto', models.IntegerField(default=0)),
                ('raza', models.CharField(max_length=50)),
                ('organizacion', models.CharField(max_length=50)),
                ('planetas_destruidos', models.IntegerField(default=0)),
            ],
        ),
    ]
