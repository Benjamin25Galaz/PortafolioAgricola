from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout as django_logout, authenticate
from .forms import TemaForm, SolicitudForm, RegisterForm, DonacionForm, CommentForm, ProductoForm
from .models import Tema, Solicitud, Register, Donacion, Producto
from .carrito import Carrito
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def donacion(request):
    return render(request, 'core/donacion.html')

def donacion(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumen')  # Redirige a la página de resumen o éxito
    else:
        form = DonacionForm()

    return render(request, 'core/donacion.html', {'form': form})


def tema_detail(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    comments = tema.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tema = tema
            comment.author = request.user
            comment.save()
            return redirect('core/tema_detail', tema_id=tema.id)
    else:
        form = CommentForm()

    return render(request, 'core/tema_detail.html', {
        'tema': tema,
        'comments': comments,
        'form': form,
    })

def resumen(request):
    donaciones= Donacion.objects.all()  # Obtenemos todas las solicitudes
    return render(request, 'core/resumen.html', {'donaciones': donaciones})



def register(request):
    return render(request, 'core/register.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()  # Asegúrate de que esta línea cree un formulario vacío si la solicitud es GET
    return render(request, 'core/register.html', {'form': form})

def bienvenido(request):
    return render(request, 'core/bienvenido.html')

def resumen(request):
    return render(request, 'core/resumen.html')

def solicitudes(request):
    return render(request, 'core/solicitudes.html')
    

def solicitudes(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la solicitud en la base de datos
            return redirect('lista_solicitudes')  # Redirige a la lista de solicitudes
    else:
        form = SolicitudForm()

    return render(request, 'core/solicitudes.html', {'form': form})


def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all()  # Obtenemos todas las solicitudes
    return render(request, 'core/lista_solicitudes.html', {'solicitudes': solicitudes})

def logout(request):
    logout(request)
    return HttpResponseRedirect('core/logout.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')


def pago(request):
    return render(request, 'core/pago.html')


def detallepro(request):
    return render(request, 'core/detallepro.html')


def foro(request):
    return render(request, 'core/foro.html')

def foro(request):
    temas = Tema.objects.all()  # Obtiene todos los temas
    return render(request, 'core/foro.html', {'temas': temas})

# Vista del tema del foro
def crear_tema(request):
    return render(request, 'core/crear_tema.html')


@login_required
def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit=False)  # No guarda todavía
            tema.author = request.user  # Asigna el autor
            tema.save()  # Guarda el tema en la base de datos
            return redirect('foro')  # Redirige a donde quieras
    else:
        form = TemaForm()
    return render(request, 'core/crear_tema.html', {'form': form})

def acceder(request):
    if request.method == "POST":
        # Obtener los valores de usuario y contraseña desde el formulario
        correo_electronico = request.POST.get('correo_electronico')
        contrasena = request.POST.get('contrasena')
        # Verifica si el registro existe en la base de datos
        try:
            usuario = Register.objects.get(correo_electronico=correo_electronico, contrasena=contrasena)
            # Almacena el nombre en la sesión
            request.session['nombre_usuario'] = usuario.nombre  # Guarda el nombre del usuario en la sesión
            return redirect('bienvenido')  # Redirigir a la página de inicio
        except Register.DoesNotExist:
            error_message = "Credenciales inválidas."  # Mensaje de error si el usuario no existe
            return render(request, 'core/acceder.html', {'error': error_message})

    # Si el método no es POST, renderiza el formulario de inicio de sesión
    return render(request, 'core/acceder.html')  # Siempre se debe devolver un HttpResponse


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "core/listar_productos.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar_carrito(producto)
    return redirect("listar_productos")  # Cambiar por el nombre que corresponda


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect("listar_productos")  # Cambiar por el nombre que corresponda

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    return redirect("listar_productos")  # Cambiar por el nombre que corresponda

def sumar_producto(request, producto_id):
    carrito = Carrito(request)  # Crear una instancia del carrito
    producto = get_object_or_404(Producto, id=producto_id)  # Obtiene el producto por ID
    carrito.sumar(producto)  # Llama al método sumar en la clase Carrito
    return redirect("listar_productos")  # Redirige a la vista de productos

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("listar_productos")  # Cambiar por el nombre que corresponda

def formulario_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'core/formulario_producto.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/listar_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'core/detalle_producto.html', {'producto': producto})
