from django import forms
from .models import Persona, Evento

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nombre', 'fecha_evento', 'descripcion','capacidad')

        
class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'edad','telefono','eventos')