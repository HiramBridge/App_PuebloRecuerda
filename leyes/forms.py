from  django import forms
from .models import Iniciativa



class IniciativaForm(forms.ModelForm):

    class Meta:
        model=Iniciativa

        fields =[

            'num',
            'nombre',
            'turno',
            'comision',
            'resolutivos',
            'enlace',
            'diputado',

        ]

        labels={

            'num':'Numero',
            'nombre':'Nombre',
            'turno':'Turno',
            'comision':'Comision',
            'resolutivos':'Resolutivos',
            'enlace':'Enlace',
            'diputado':'Diputado',

        }
        widgets={

            'num':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'turno':forms.TextInput(attrs={'class':'form-control'}),
            'comision':forms.TextInput(attrs={'class':'form-control'}),
            'resolutivos':forms.TextInput(attrs={'class':'form-control'}),
            'enlace':forms.URLInput(attrs={'class':'form-control'}),
            'diputado':forms.Select(attrs={'class':'form-control'}),


        }