# Generated by Django 2.2.10 on 2022-03-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_subcategoriascalificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoriascalificacion',
            name='nombre',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]