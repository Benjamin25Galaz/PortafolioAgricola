from django.shortcuts import render

# Create your views here.

#Funcion para conectar con el documento home .html
def home(request):
    return render(request, 'core/home.html')

