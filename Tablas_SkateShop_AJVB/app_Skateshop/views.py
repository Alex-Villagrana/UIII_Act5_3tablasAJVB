# Contenido de app_Skateshop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Proveedor # Importamos los modelos

# 1. Función de Inicio
def inicio_skateshop(request):
    return render(request, 'inicio.html')

# 2. CRUD: Agregar Cliente
def agregar_cliente(request):
    if request.method == 'POST':
        # No validar entrada de datos:
        cliente = Cliente(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            activo=request.POST.get('activo', False) == 'on'
        )
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        # Asignar productos comprados
        productos_ids = request.POST.getlist('compra')
        if productos_ids:
            productos = Producto.objects.filter(id__in=productos_ids)
            cliente.compra.set(productos)
        return redirect('ver_clientes')
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/agregar_cliente.html', context)

# 3. CRUD: Ver Clientes (Listado)
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')
    context = {'clientes': clientes}
    return render(request, 'cliente/ver_clientes.html', context)

# 4. CRUD: Actualizar Cliente (Mostrar Formulario)
def actualizar_cliente(request, pk):
    cliente_a_actualizar = get_object_or_404(Cliente, pk=pk)
    productos = Producto.objects.all()
    context = {'cliente': cliente_a_actualizar, 'productos': productos}
    return render(request, 'cliente/actualizar_cliente.html', context)

# 5. CRUD: Actualizar Cliente (Procesar POST)
def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.activo = request.POST.get('activo', False) == 'on'
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        # Actualizar productos comprados
        productos_ids = request.POST.getlist('compra')
        productos = Producto.objects.filter(id__in=productos_ids)
        cliente.compra.set(productos)
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', pk=pk)

# 6. CRUD: Borrar Cliente
def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/borrar_cliente.html', context)

# 7. CRUD: Agregar Proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        proveedor = Proveedor(
            contacto_nombre=request.POST.get('contacto_nombre'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion=request.POST.get('direccion'),
            pais=request.POST.get('pais'),
            estado=request.POST.get('estado'),
            ciudad=request.POST.get('ciudad')
        )
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

# 8. CRUD: Ver Proveedores (Listado)
def ver_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('contacto_nombre')
    context = {'proveedores': proveedores}
    return render(request, 'proveedor/ver_proveedores.html', context)

# 9. CRUD: Actualizar Proveedor (Mostrar Formulario)
def actualizar_proveedor(request, pk):
    proveedor_a_actualizar = get_object_or_404(Proveedor, pk=pk)
    context = {'proveedor': proveedor_a_actualizar}
    return render(request, 'proveedor/actualizar_proveedor.html', context)

# 10. CRUD: Actualizar Proveedor (Procesar POST)
def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.contacto_nombre = request.POST.get('contacto_nombre')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.pais = request.POST.get('pais')
        proveedor.estado = request.POST.get('estado')
        proveedor.ciudad = request.POST.get('ciudad')
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', pk=pk)

# 11. CRUD: Borrar Proveedor
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/borrar_proveedor.html', context)

# 12. CRUD: Agregar Producto
def agregar_producto(request):
    if request.method == 'POST':
        producto = Producto(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            stock=request.POST.get('stock'),
            proveedor_id=request.POST.get('proveedor'),
            marca=request.POST.get('marca'),
            modelo=request.POST.get('modelo'),
            disponible=request.POST.get('disponible', False) == 'on'
        )
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    context = {'proveedores': proveedores}
    return render(request, 'producto/agregar_producto.html', context)

# 13. CRUD: Ver Productos (Listado)
def ver_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    context = {'productos': productos}
    return render(request, 'producto/ver_productos.html', context)

# 14. CRUD: Actualizar Producto (Mostrar Formulario)
def actualizar_producto(request, pk):
    producto_a_actualizar = get_object_or_404(Producto, pk=pk)
    proveedores = Proveedor.objects.all()
    context = {'producto': producto_a_actualizar, 'proveedores': proveedores}
    return render(request, 'producto/actualizar_producto.html', context)

# 15. CRUD: Actualizar Producto (Procesar POST)
def realizar_actualizacion_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.proveedor_id = request.POST.get('proveedor')
        producto.marca = request.POST.get('marca')
        producto.modelo = request.POST.get('modelo')
        producto.disponible = request.POST.get('disponible', False) == 'on'
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', pk=pk)

# 16. CRUD: Borrar Producto
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    context = {'producto': producto}
    return render(request, 'producto/borrar_producto.html', context)
