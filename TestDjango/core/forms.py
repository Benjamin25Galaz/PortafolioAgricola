from django import forms
from .models import Tema, Solicitud, Register, Donacion, Comment, Producto, Pago



class RegisterForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = Register
        fields = ['nombre', 'apellido', 'correo_electronico', 'contrasena', 'confirmar_contrasena']

    def clean_confirmar_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        confirmar_contrasena = self.cleaned_data.get('confirmar_contrasena')

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return confirmar_contrasena

class DonacionForm(forms.ModelForm):
    
    
    class Meta:
        model = Donacion
        fields = ['opcion', 'comuna', 'tipo_arbol', 'cantidad']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['nombre', 'apellido', 'correo', 'telefono']

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'content', ]  # Los campos que el usuario llenará


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre',
            'apellido',
            'tipo_solicitud',
            'telefono',
            'correo',
            'direccion',
            'comuna',
            'fecha_retiro',
            'cantidad_arboles',
            'cantidad_litros',
            'comentarios'
        ]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'categoria',
            'descripcion',
            'precio',
            'imagen',
            'stock'
            ]




