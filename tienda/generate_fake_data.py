# tienda/generate_fake_data.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')  # Reemplaza 'ecommerce' con el nombre de tu proyecto Django

import django
django.setup()

from faker import Faker
from tienda.models import Producto, Boleta, DetalleBoleta

fake = Faker()

def generate_fake_product():
    return Producto.objects.create(
        codigo=fake.uuid4(),
        nombre=fake.word(),
        descripcion=fake.sentence(),
        precio=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        asset=fake.image_url(),
        estado=fake.random_int(min=1, max=5)
    )

def generate_fake_boleta():
    return Boleta.objects.create(
        total=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        codigo_seguimiento=fake.uuid4(),
        nombre_comprador=fake.name(),
        direccion_comprador=fake.address()
    )

def generate_fake_detalle_boleta(boleta, producto):
    return DetalleBoleta.objects.create(
        boleta=boleta,
        producto=producto,
        precio=producto.precio,
        cantidad=fake.random_int(min=1, max=10),
        total=producto.precio * DetalleBoleta.cantidad
    )

def generate_fake_data():
    for _ in range(10):  # Puedes ajustar la cantidad de datos falsos a generar
        producto = generate_fake_product()
        boleta = generate_fake_boleta()
        generate_fake_detalle_boleta(boleta, producto)

# if __name__ == '__main__':
#     generate_fake_data()
