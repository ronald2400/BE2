from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario', 'correo', 'contraseña']

class IngresoForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    contraseña = forms.CharField(widget=forms.PasswordInput)