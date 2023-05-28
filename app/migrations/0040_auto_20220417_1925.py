# Generated by Django 2.2.10 on 2022-04-18 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20220417_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojasdevida',
            name='nombre_usuario',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hojasdevida',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
