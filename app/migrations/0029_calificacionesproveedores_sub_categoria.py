# Generated by Django 2.2.10 on 2022-03-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_subcategoriascalificacion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacionesproveedores',
            name='sub_categoria',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
