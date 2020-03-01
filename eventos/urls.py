from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.CrearView.as_view(), name='crear')
]