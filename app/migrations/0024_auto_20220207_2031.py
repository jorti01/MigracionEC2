# Generated by Django 2.2.10 on 2022-02-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_calificacionproveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacionproveedores',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
