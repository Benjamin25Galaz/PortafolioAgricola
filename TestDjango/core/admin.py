from django.contrib import admin
from .models import Solicitud, Tema, Register #Donacion

# Register your models here.

#admin.site.register(Donacion)
admin.site.register(Solicitud)
admin.site.register(Tema)
admin.site.register(Register)



