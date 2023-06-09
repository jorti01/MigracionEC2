# Generated by Django 3.2.8 on 2023-03-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_alter_hojasdevida_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionesSeleccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documentos_legales', models.IntegerField()),
                ('forma_pago', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('gestion_cotizaciones', models.IntegerField()),
                ('certificaciones_calidad', models.IntegerField()),
                ('implementacion_sgsst', models.IntegerField()),
                ('documentos_ambientales', models.IntegerField()),
                ('proveedor_relacionado', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='plazo_etapa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='resumen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
