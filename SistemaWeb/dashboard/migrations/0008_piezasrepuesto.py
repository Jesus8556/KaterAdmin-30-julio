# Generated by Django 3.2 on 2023-07-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_cotizacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='piezasRepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('descripcion', models.ImageField(blank=True, null=True, upload_to='descPiezas/')),
                ('imagen_tienda', models.ImageField(blank=True, null=True, upload_to='imgPiezas/')),
                ('precio_soles', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]