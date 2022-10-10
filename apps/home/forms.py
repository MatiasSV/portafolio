from operator import attrgetter
from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from .models import *



class formDEPARTAMENTO(forms.ModelForm):
    
    class Meta:
        model = DEPARTAMENTO
        fields = ['DEP_NOMBRE', 'EST_ID','DEP_DESCRIPCION','DEP_CANTIDADHABITACIONES','DEP_CANTIDADCAMAS', 
                'DEP_CANTIDADBANOS','DEP_CANTIDADPERSONAS','DEP_DIRECCION','ZON_ID','DEP_VALOR_DIA',
                'DEP_IMAGEN1','DEP_IMAGEN2', 'DEP_IMAGEN3','TOU_ID1','TOU_ID2','TOU_ID3']

        labels = '__all__'

        widgets = {
            'DEP_NOMBRE': forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
            'EST_ID': forms.Select(),            
            'DEP_DESCRIPCION': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'DEP_CANTIDADHABITACIONES': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'DEP_CANTIDADCAMAS': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'DEP_CANTIDADBANOS': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'DEP_CANTIDADPERSONAS': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'DEP_DIRECCION': forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
            'ZON_ID': forms.Select(),
            'DEP_VALOR_DIA': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'TOU_ID1': forms.Select(),
            'TOU_ID2': forms.Select(),
            'TOU_ID3': forms.Select()
        }


class formTOUR(forms.ModelForm):

    class Meta:
        model = TOUR
        fields = ['ZON_ID','TOU_NOMBRE','TOU_DESCRIPCION','TOU_VALOR']
        labels = '__all__'
        widgets = {
            'ZON_ID': forms.Select(),
            'TOU_NOMBRE': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TOU_DESCRIPCION': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TOU_VALOR': forms.TextInput(attrs={'class':'form-control', 'type':'number'})
        }


class formTRANSPORTE(forms.ModelForm):

    class Meta:
        model = TRANSPORTE
        fields = ['TRA_NOMBRESERVICIO', 'TRA_HORARIO','TRA_VEHICULO','TRA_CONDUCTOR','TRA_VALOR']
        labels = '__all__'
        widgets = {
            'TRA_NOMBRESERVICIO': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TRA_HORARIO': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TRA_VEHICULO': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TRA_CONDUCTOR': forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'TRA_VALOR': forms.TextInput(attrs={'class':'form-control','type':'number'})
        }    



class formINVENTARIO(forms.ModelForm):

    class Meta:
        model = INVENTARIO
        fields = ['INV_MICROONDAS','INV_HORNOELECTRICO']
        labels = '__all__'
        widgets = {
            # 'INV_DEPARTAMENTO': forms.Select(),
            'INV_MICROONDAS': forms.CheckboxInput(),
            'INV_HORNOELECTRICO': forms.CheckboxInput()
        }


class formRESERVA(forms.Form):
    fecha_ingreso= forms.DateField(required=True)
    fecha_salida= forms.DateField(required=True)
    asistentes= forms.CharField(widget=forms.Textarea)
        