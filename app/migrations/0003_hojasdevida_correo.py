# Generated by Django 2.2.10 on 2021-11-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hojasdevida_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojasdevida',
            name='correo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
