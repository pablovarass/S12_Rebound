
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Book

def registro(request):
    """Registra un nuevo usuario y le asigna permisos específicos."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            content_type = ContentType.objects.get_for_model(Book)
            permission = Permission.objects.get(codename='development', content_type=content_type)
            user.user_permissions.add(permission)
            user.save()
            messages.success(request, 'Registro exitoso')
            return redirect('login')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    """Autentica y mantiene la sesión del usuario."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('lista_libros')
        else:
            messages.error(request, 'Credenciales inválidas')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'login.html')

@login_required
def cerrar_sesion(request):
    """Finaliza la sesión del usuario actual."""
    logout(request)
    return redirect('index')
