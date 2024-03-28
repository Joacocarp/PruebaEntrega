# Generated by Django 5.0.2 on 2024-03-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_cliente_apellido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArticulo', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('talle', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArticulo', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('talle', models.CharField(max_length=10)),
            ],
        ),
    ]
