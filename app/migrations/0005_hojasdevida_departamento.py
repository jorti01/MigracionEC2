# Generated by Django 2.2.10 on 2021-11-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_hojasdevida_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojasdevida',
            name='departamento',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
