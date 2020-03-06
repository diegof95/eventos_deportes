from django import forms
from .models import Evento, LocalidadEvento

class EventoForm(forms.ModelForm):
    """ Formulario para crear y editar evento"""

    class Meta:
        model = Evento
        fields = ['tipo', 'nombre', 'descripcion', 'imagen', 'fecha', 'hora', 'estadio', 'estado']
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'})
        }