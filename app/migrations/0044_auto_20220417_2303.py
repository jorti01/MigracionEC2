# Generated by Django 2.2.10 on 2022-04-18 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20220417_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistenciacapacitacion',
            old_name='Presence',
            new_name='asistencia',
        ),
    ]
