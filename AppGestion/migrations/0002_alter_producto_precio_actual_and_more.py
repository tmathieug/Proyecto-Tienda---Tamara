# Generated by Django 4.2 on 2023-08-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_actual',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock_disponible',
            field=models.PositiveSmallIntegerField(),
        ),
    ]