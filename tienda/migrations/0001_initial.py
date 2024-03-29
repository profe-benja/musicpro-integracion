# Generated by Django 4.2.3 on 2024-01-19 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('codigo_seguimiento', models.CharField(max_length=50, null=True)),
                ('nombre_comprador', models.CharField(max_length=255)),
                ('direccion_comprador', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('asset', models.URLField()),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.boleta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
