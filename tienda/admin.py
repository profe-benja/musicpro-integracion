from django.contrib import admin

# Register your models here.
from .models import Producto, Boleta, DetalleBoleta

admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)