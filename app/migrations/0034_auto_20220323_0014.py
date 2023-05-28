# Generated by Django 2.2.10 on 2022-03-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20220323_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausentismo',
            name='solicitado',
            field=models.ManyToManyField(to='app.HojasdeVida'),
        ),
        migrations.RemoveField(
            model_name='ausentismo',
            name='solicitante',
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='solicitante',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]