from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Evento
from .forms import EventoForm

class CrearView(generic.CreateView):
    """ Crear view """

    template_name = 'eventos/crear.html'
    form_class= EventoForm
    model = Evento
    success_url = reverse_lazy('')

