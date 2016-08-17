from django import forms

from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio'
		]
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'domicilio':forms.Textarea(attrs={'class':'form-control'}),
		}

class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = [
			'numero_mascota',
			'razones',
		]
		widgets = {
			'numero_mascota':forms.TextInput(attrs={'class':'form-control'}),
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}