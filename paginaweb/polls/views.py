from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def index(request):
    return render(request, "polls/index.html")

def paginabaldurs(request):
    return render(request, 'polls/PaginaBaldurs.html')

def paginabanco(request):
    return render(request, 'polls/Bancojade.html')

def registrar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if not usuario or not correo or not contraseña:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('paginabanco')

        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('paginabanco')

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return redirect('paginabanco')

        nuevo_usuario = Usuario(usuario=usuario, correo=correo)
        nuevo_usuario.set_password(contraseña)
        nuevo_usuario.save()
        messages.success(request, 'Usuario registrado correctamente')
        return redirect('paginabanco')

    return redirect('paginabanco')


def ingresar(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        contraseña_input = request.POST.get('contraseña')
        try:
            usuario = Usuario.objects.get(usuario=usuario_input)
            if usuario.check_password(contraseña_input):
                return render(request, 'polls/BancoUsuario.html', {'usuario': usuario})
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')

    return redirect('paginabanco')