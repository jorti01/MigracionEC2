# Generated by Django 3.2.8 on 2022-12-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_auto_20220427_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capacitaciones',
            options={'ordering': ('-fecha',)},
        ),
        migrations.AddField(
            model_name='documentoshojavida',
            name='categoria',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='codigo_enfermedad',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='solicitado',
            field=models.ManyToManyField(to='app.HojasdeVida', verbose_name='Solicitar a'),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='adjunto',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='evaluacion_texto',
            field=models.TextField(verbose_name='Evaluación del Capacitador'),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='tema_texto',
            field=models.TextField(verbose_name='Temas de la Capacitación'),
        ),
    ]
