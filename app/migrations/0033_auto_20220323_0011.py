# Generated by Django 2.2.10 on 2022-03-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20220323_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausentismo',
            name='solicitado',
            field=models.ManyToManyField(related_name='solicitadoAusentismo', to='app.HojasdeVida'),
        ),
        migrations.RemoveField(
            model_name='ausentismo',
            name='solicitante',
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='solicitante',
            field=models.ManyToManyField(related_name='solicitanteAusentismo', to='app.HojasdeVida'),
        ),
    ]
