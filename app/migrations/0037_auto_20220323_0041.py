# Generated by Django 2.2.10 on 2022-03-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_ausentismo_adjunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausentismo',
            name='motivo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='adjunto',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
