from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['nombre', 'documento', 'correo', 'telefono', 'tipo', 'asunto', 'descripcion', 'fecha', 'archivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 5}),
            'tipo': forms.Select(),
        }
