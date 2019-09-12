# Generated by Django 2.2.5 on 2019-09-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsuarios', '0002_auto_20190910_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_bloqueado',
            field=models.BooleanField(default=False, verbose_name='Login Bloqueado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_deuda',
            field=models.BooleanField(default=False, verbose_name='Posee Deuda'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Último login'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
    ]
