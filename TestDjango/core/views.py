from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import TemaForm, SolicitudForm, RegisterForm, DonacionForm
from .models import Tema, Solicitud, Register, Donacion
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

