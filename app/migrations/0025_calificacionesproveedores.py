# Generated by Django 2.2.10 on 2022-02-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20220207_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalificacionesProveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
                ('proveedor_relacionado', models.IntegerField(blank=True, null=True)),
                ('categoria', models.ManyToManyField(to='app.CalificacionProveedores')),
            ],
        ),
    ]
