# Generated by Django 2.2.5 on 2019-09-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
