from django.shortcuts import render, redirect
from .generate_fake_data import generate_fake_data
import requests
import json
from django.http import JsonResponse
from .models import Producto, Boleta, DetalleBoleta

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def pagar(request):
    format = request.GET.get('format')
    
    nombre_comprador = request.POST.get('nombre')
    direccion_comprador = request.POST.get('direccion')
    listado_productos = request.POST.get('listado_productos')

    boleta = Boleta.objects.create(
        nombre_comprador=nombre_comprador,
        direccion_comprador=direccion_comprador,
        total=0
    )

    detalles_productos = json.loads(listado_productos)
    for detalle_producto in detalles_productos:
        DetalleBoleta.objects.create(
            boleta=boleta,
            producto_id=detalle_producto['id'],
            cantidad=detalle_producto['quantity'],
            precio=detalle_producto['price'],
            total=detalle_producto['total']
        )
        
    boleta.total += detalle_producto['total']
    boleta.save()
    
    if format == 'json':
        return JsonResponse({'status': 'success', 'boleta': list(boleta.values())})
    else: 
        return render(request, 'comprado.html', {'boleta': boleta})

    

def boletas(request):
    format = request.GET.get('format')
    
    boletas = Boleta.objects.all()
    if format == 'json':
        return JsonResponse({'status': 'success', 'boletas': list(boletas.values())})
    else: 
        return render(request, 'boletas.html', {'boletas': boletas})

# Create your views here.
def musicpro_productos(request):
    url = "https://musicpro.bemtorres.win/api/v1/bodega/producto"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verificar si hubo algún error en la solicitud
        data = response.json()  # Convertir la respuesta a JSON
    except requests.RequestException as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

    context = {
        'productos': data['productos']
    }
    
    return render(request, 'musicpro/productos.html', context)
    
    
    # for id, producto_data in enumerate(data['productos']):
    #     Producto.objects.create(
    #         codigo= id + random.randint(1, 1000),
    #         nombre=producto_data['nombre'],
    #         descripcion=producto_data['descripcion'],
    #         precio=producto_data['precio'],
    #         asset=producto_data['asset'],
    #         estado=producto_data['estado'],
    #     )

    # productos = Producto.objects.all()
    # return render(request, 'productos.html', {'productos': productos})
    # # return render(request, 'success_template.html', {'message': 'Productos actualizados correctamente'})

def musicpro_transporte(request):
    url_musicpro = "https://musicpro.bemtorres.win/api/v1/transporte/solicitud"
    url_cargafacil = "http://192.168.137.75:8000/api/v1/solicitud?format=json"
    
    
    transporte = request.POST.get('transporte')
    
    
    id_boleta = request.POST.get('id')
    boleta = Boleta.objects.get(id=id_boleta)
    
    if transporte == 'MUSICPRO':
        try:
            # Realizar la solicitud HTTP
            response = requests.post(url_musicpro, data={
                "nombre_origen": "Casa de musica",
                "direccion_origen": "Av San joaquin 1234",
                "nombre_destino": boleta.nombre_comprador,
                "direccion_destino": boleta.direccion_comprador,
                "comentario": "entrega de productos",
            })
            response.raise_for_status()  # Verificar si hubo algún error en la solicitud
            data = response.json()  # Convertir la respuesta a JSON
        except requests.RequestException as e:
            return render(request, 'error_template.html', {'error_message': str(e)})

        codigo_seguimiento = data['codigo_seguimiento']
        boleta.codigo_seguimiento = codigo_seguimiento
        boleta.proveedor_transporte = 'MUSICPRO'
        boleta.estado = 'Enviado solicitud transportista'
        boleta.save()
    elif transporte == 'CARGAFACIL':
        try:
            # Realizar la solicitud HTTP
            headers = {'Content-type': 'application/json'}
            data = {
                "persona_origen": "Casa de musica",
                "direccion_origen": "Av San joaquin 1234",
                "persona_destino": boleta.nombre_comprador,
                "direccion_destino": boleta.direccion_comprador,
                "descripcion": "entrega de productos",
            }
            response = requests.post(url_cargafacil, data= json.dumps(data), headers=headers)
            response.raise_for_status()  # Verificar si hubo algún error en la solicitud
            data = response.json()  # Convertir la respuesta a JSON
        except requests.RequestException as e:
            return render(request, 'error_template.html', {'error_message': str(e)})
        
        boleta.codigo_seguimiento = data['codigo_seguimiento']
        boleta.estado = data['estado']
        boleta.proveedor_transporte = 'CARGAFACIL'
        boleta.save()

    return redirect('boletas')
    # return JsonResponse({'status': 'success', 'data': data})


def musicpro_transporte_estado(request):
    url_musicpro = "https://musicpro.bemtorres.win/api/v1/transporte/seguimiento"
    url_cargafacil = "http://192.168.137.75:8000/api/v1/solicitud?format=json"
    
    id_boleta = request.POST.get('id')
    boleta = Boleta.objects.get(id=id_boleta)
    
    url = ""
    if boleta.proveedor_transporte == 'MUSICPRO':
        url = url_musicpro + "/" + boleta.codigo_seguimiento
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verificar si hubo algún error en la solicitud
            data = response.json()  # Convertir la respuesta a JSON
        except requests.RequestException as e:
            return render(request, 'error_template.html', {'error_message': str(e)})
    elif boleta.proveedor_transporte == 'CARGAFACIL':
        url = url_cargafacil + "/" + boleta.codigo_seguimiento
        headers = {'Content-type': 'application/json'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Verificar si hubo algún error en la solicitud
            data = response.json()  # Convertir la respuesta a JSON
        except requests.RequestException as e:
            return render(request, 'error_template.html', {'error_message': str(e)})

    # estado = data['result']['estado']
    # boleta.estado = estado
    # boleta.save()
    return JsonResponse({'status': 'success', 'data': data})

    return redirect('boletas')