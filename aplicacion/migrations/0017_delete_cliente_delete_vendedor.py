# Generated by Django 5.0.2 on 2024-03-30 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_remove_buzo_user_remove_pantalon_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
