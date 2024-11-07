
from django.urls import path
from .views import IndexPageView  # la vista de página principal
from .book_views import lista_libros, crear_libro, editar_libro, eliminar_libro
from .auth_views import registro, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('crear_libro/', crear_libro, name='crear_libro'),
    path('editar_libro/<int:libro_id>/', editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:libro_id>/', eliminar_libro, name='eliminar_libro'),
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
