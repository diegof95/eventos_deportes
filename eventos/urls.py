from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.CrearView.as_view(), name='crear'),
    path('localidades/<int:id>', views.LocalidadesView.as_view(), name='localidades'),
    path('listar', views.ListarView.as_view(), name='listar'),
    path('editar', views.EditarView.as_view(), name='editar'),
]