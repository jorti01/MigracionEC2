# Generated by Django 2.2.10 on 2022-03-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_capacitaciones_surge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ausentismo',
            name='Usuario',
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='solicitado',
            field=models.ManyToManyField(to='app.HojasdeVida'),
        ),
    ]
