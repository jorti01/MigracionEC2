# Generated by Django 2.2.10 on 2022-03-01 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_calificacionesproveedores'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacionesproveedores',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
