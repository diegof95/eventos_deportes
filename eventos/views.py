from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.messages import views as message_views
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Evento
from .forms import EventoForm, LocalidadEventoForm, LocalidadEventoFormSet

class CrearView(message_views.SuccessMessageMixin, generic.edit.CreateView):
    """ Crear view """

    template_name = 'eventos/crear.html'
    form_class= EventoForm
    model = Evento
    success_url = reverse_lazy('home')
    success_message = "El evento %(nombre)s fue creado con éxito"
    
class LocalidadesView(generic.FormView):
    
    template_name = 'eventos/localidades.html'
    form_class = LocalidadEventoForm
    success_url = reverse_lazy('eventos:listar')
    
    # instance <- event_id
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        id_evento = kwargs['id']
        evento = get_object_or_404(Evento, pk=id_evento)
        context['evento'] = evento
        
        if self.request.POST:
            context['formset'] = LocalidadEventoFormSet(self.request.POST, instance=evento)
        else:
            context['formset'] = LocalidadEventoFormSet(instance=evento)
        
        return self.render_to_response(context)
    
class ListarView(generic.list.ListView):
    
    queryset = Evento.objects.order_by('estado')
    template_name = "eventos/listar.html"
    context_object_name = "eventos"
    
    estados_sin_evento = set()
    extra_context = { 'estados_sin_evento': estados_sin_evento }
    
    def get_estado_sin_evento(self, context, *args,**kwargs):
        """ Verifica los Estado de evento para los cuales no hay un Evento a mostrar """
        
        estados_con_evento = set(context['eventos'].values_list('estado', flat=True))
        for opcion_estado in Evento.get_estados():
            if opcion_estado[0] not in estados_con_evento:
                self.estados_sin_evento.add(opcion_estado[1])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.get_estado_sin_evento(context)
        return context

class EditarView(generic.edit.UpdateView):
    pass