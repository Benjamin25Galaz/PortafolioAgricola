from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout as django_logout, authenticate
from .forms import TemaForm, SolicitudForm, RegisterForm, DonacionForm, CommentForm, ProductoForm, PagoForm
from .models import Tema, Solicitud, Register, Donacion, Producto,Pago
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
            donacion_guardada = form.save()
            return redirect('resumen_donacion', donacion_id=donacion_guardada.id)
    else:
        form = DonacionForm()
    return render(request, 'core/donacion.html', {'form': form})

def resumen_donacion(request, donacion_id):
    donacion = Donacion.objects.get(id=donacion_id)
    return render(request, 'core/resumen_donacion.html', {'donacion': donacion})


def migrar_usuarios():
    # Obtener todos los registros de la tabla Register
    registros = Register.objects.all()

    for registro in registros:
        # Verifica si ya existe un usuario con ese correo electrónico
        if not User.objects.filter(username=registro.correo_electronico).exists():
            # Crea un usuario en la tabla User
            user = User.objects.create_user(
                username=registro.correo_electronico,  # Utiliza el correo como nombre de usuario
                email=registro.correo_electronico,
                password=registro.contrasena,  # Asegúrate de que la contraseña esté almacenada de forma segura
                first_name=registro.nombre,
                last_name=registro.apellido
            )
            user.save()

@login_required(login_url='acceder')
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
            return redirect('tema_detail', tema_id=tema.id)
    else:
        form = CommentForm()

    return render(request, 'core/tema_detail.html', {
        'tema': tema,
        'comments': comments,
        'form': form,
    })

def donacion(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            donacion_guardada = form.save()
            return redirect('resumen_donacion', donacion_id=donacion_guardada.id)
    else:
        form = DonacionForm()
    return render(request, 'core/donacion.html', {'form': form})

def resumen_donacion(request, donacion_id):
    donacion = Donacion.objects.get(id=donacion_id)
    return render(request, 'core/resumen_donacion.html', {'donacion': donacion})



def register(request):
    return render(request, 'core/register.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo_electronico']
            contrasena = form.cleaned_data['contrasena']

            # Crear el usuario en la tabla User
            user = User.objects.create_user(
                username=correo,  # Utiliza el correo como nombre de usuario
                email=correo,
                password=contrasena,
                first_name=nombre,
                last_name=apellido
            )
            user.save()
            
            # Opcionalmente, puedes autenticar y loguear al usuario después de registrarse
            from django.contrib.auth import login
            login(request, user)

            return redirect('home')  # Redirige a la página principal después del registro
    else:
        form = RegisterForm()
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

def pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = Pago(usuario=request.user, cantidad=form.cleaned_data['cantidad'])
            pago.save()
            messages.success(request, 'El pago ha sido procesado con éxito.')
            return redirect('pago_exitoso')
    else:
        form = PagoForm()

    return render(request, 'core/pago.html', {'form': form})

def pago_exitoso(request):
    return render(request, 'core/pago_exitoso.html')


def foro(request):
    return render(request, 'core/foro.html')

def foro(request):
    temas = Tema.objects.all()  # Obtiene todos los temas
    return render(request, 'core/foro.html', {'temas': temas})

# Vista del tema del foro
def crear_tema(request):
    return render(request, 'core/crear_tema.html')


@login_required(login_url='acceder')
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
        correo_electronico = request.POST.get('correo_electronico')
        contrasena = request.POST.get('contrasena')

        # Autenticar al usuario usando el correo como nombre de usuario
        usuario = authenticate(request, username=correo_electronico, password=contrasena)
        
        # Verificar si la autenticación fue exitosa
        if usuario is not None:
            login(request, usuario)
            # Almacena el nombre en la sesión
            request.session['nombre_usuario'] = usuario.first_name  # Cambia según el campo que desees mostrar
            return redirect('bienvenido')
        else:
            error_message = "Credenciales inválidas."
            return render(request, 'core/acceder.html', {'error': error_message})

    return render(request, 'core/acceder.html')

def listar_productos(request):
    productos = Producto.objects.all()
    carrito = Carrito(request)
    total = carrito.obtener_total()
    return render(request, "core/listar_productos.html", {
        'productos': productos,
        'carrito': carrito,
        'total': total
    })

'''
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "core/listar_productos.html", {'productos': productos})
'''
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

def mostrar_carrito(request):
    carrito = Carrito(request)
    total = carrito.obtener_total()
    return render("listar_productos")

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
