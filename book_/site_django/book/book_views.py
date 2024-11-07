
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
import datetime

@login_required
def lista_libros(request):
    """Renderiza la lista de libros disponibles."""
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

@login_required
def crear_libro(request):
    """Permite crear un nuevo libro mediante un formulario."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado correctamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('crear_libro'))
    else:
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})

@login_required
def editar_libro(request, libro_id):
    """Edita los detalles de un libro existente."""
    book = get_object_or_404(Book, pk=libro_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book.fecha_modificacion = datetime.datetime.now()
            form.save()
            messages.success(request, 'Libro modificado correctamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('editar_libro', args=[book.id]))
    else:
        form = BookForm(instance=book)
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id})

@login_required
def eliminar_libro(request, libro_id):
    """Elimina un libro específico de la base de datos."""
    book = get_object_or_404(Book, pk=libro_id)
    book.delete()
    messages.info(request, 'Libro eliminado correctamente')
    return redirect('lista_libros')
