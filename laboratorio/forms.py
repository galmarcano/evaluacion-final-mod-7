from django import forms
from .models import Laboratorio 

class LaboratorioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(LaboratorioForm, self).__init__(*args, **kwargs)
        self.fields['ciudad'].widget.attrs['placeholder'] = 'Ingrese ciudad'
        self.fields['ciudad'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese nombre'
        self.fields['nombre'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['pais'].widget.attrs['placeholder'] = 'Ingrese país'
        self.fields['pais'].widget.attrs['class'] = 'form-control mb-3 '
        
        self.fields['ciudad'].label = 'Ciudad'
        self.fields['nombre'].label = 'Nombre'
        self.fields['pais'].label = 'Pais'
    
    class Meta:
        model = Laboratorio
        exclude = []