from django import forms
from .models import Evento, LocalidadEvento

class EventoForm(forms.ModelForm):
    """ Formulario para crear y editar evento"""

    class Meta:
        model = Evento
        fields = ['tipo', 'nombre', 'descripcion', 'imagen', 'fecha', 'hora', 'estadio', 'estado']
        
class LocalidadEventoForm(forms.ModelForm):
    """ Formulario para crear y editar una localidad relacionada a un evento"""
    
    class Meta:
        model = LocalidadEvento
        fields = ['localidad','aforo','precio']

LocalidadEventoFormSet = forms.inlineformset_factory(
        Evento,
        LocalidadEvento,
        form = LocalidadEventoForm,
        fields = ('localidad','aforo','precio',),
        extra = 2,
        can_delete = True
    )