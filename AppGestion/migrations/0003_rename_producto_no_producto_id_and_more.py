# Generated by Django 4.2 on 2023-08-29 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0002_alter_producto_precio_actual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='producto_no',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio_actual',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock_disponible',
        ),
    ]
