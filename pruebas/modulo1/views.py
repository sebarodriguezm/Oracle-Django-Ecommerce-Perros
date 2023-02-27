from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    
     # Obtener la lista de productos y aplicar la paginación
    productos = Producto.objects.all()
    paginator = Paginator(productos, 6)  # Mostrar 6 productos por página
    page = request.GET.get('page')
    productos_pagina = paginator.get_page(page)
    
    # Obtener la lista de razas y crear el formulario
    razas = Raza.objects.all()
    raza_formulario = RazaForm()
    
    # Si se recibe un formulario de raza, procesarlo
    if request.method == 'POST':
        formulario = RazaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Raza creada con éxito")
            return redirect('home')
        else:
            raza_formulario = formulario
            
    # Agregar los datos al contexto y renderizar el template
    data = {
        'producto_formulario': ProductoForm(),
        'productos_pagina': productos_pagina,
        'raza_formulario': raza_formulario,
        'razas': razas,
    }
    return render(request, 'modulo1/front/home.html', data)


def tienda(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'modulo1/front/tienda.html', context)

@permission_required('modulo1.add_raza')
def listar(request):
    
    razas = Raza.objects.all()
    
    data = {
        'razas' : razas
    }
    return render(request, 'modulo1/back/listar.html', data)

def historia(request):
    razas = Raza.objects.all()
    context = {'razas': razas} 
    return render(request, 'modulo1/front/historia.html', context);

def registro(request):

    data = {
        'form': CustomerUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario =CustomerUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            Cliente.objects.create(user=user, nombre=user.username, email=user.email)
            login(request, user)
            messages.success(request, "Registro con éxito ahora puedes comprar en nuestra tienda")
            return redirect(to="home")
        data["form"] = formulario
    
    
    return render(request, 'registration/registro.html',data)

@permission_required('modulo1.add_raza')
def editar_raza(request, id):
    
    raza = get_object_or_404(Raza, id = id)
    data = {
        'form': RazaForm(instance = raza)
    }
    
    if request.method == 'POST':
        formulario= RazaForm(data=request.POST, instance=raza, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listar")
        data['form']= formulario
      
    return render(request, 'modulo1/back/editar_raza.html', data)

@permission_required('modulo1.add_raza')
def eliminar_raza(request, id):
    razas= get_object_or_404(Raza, id= id)
    razas.delete()
    messages.success(request, "raza eliminado correctamente")
    return redirect(to="listar")

@permission_required('modulo1.add_raza')
def agregar_raza(request):

    data= {
            'raza_form': RazaForm()
        }    
   
    if request.method == 'POST':
            formulario = RazaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Raza creada con éxito")    
                data["mensaje"] = "guardado"
            else:
                data ["form"] = formulario
    return render(request, 'modulo1/back/agregar_raza.html', data);


@permission_required('modulo1.add_raza')
def agregar_marca(request):

    data= {
            'marca_form': MarcaForm()
        }    
   
    if request.method == 'POST':
            formulario = MarcaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Marca creada con éxito")    
                data["mensaje"] = "guardado"
            else:
                data ["form"] = formulario
    return render(request, 'modulo1/back/agregar_marca.html', data);

@permission_required('modulo1.add_raza')
def agregar_producto(request):

    data= {
            'producto_form': ProductoForm()
        }    
   
    if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto creado con éxito")    
                data["mensaje"] = "guardado"
            else:
                data ["form"] = formulario
    return render(request, 'modulo1/back/agregar_producto.html', data);