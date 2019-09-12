# Generated by Django 2.2.5 on 2019-09-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='dni',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_bloqueado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_deuda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='latitud',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='longitud',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_Instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_Pinterest',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_Twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_Youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_web',
            field=models.URLField(blank=True),
        ),
    ]
