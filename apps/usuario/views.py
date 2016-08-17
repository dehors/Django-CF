from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import ResgistroForm

class  RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = ResgistroForm
	success_url = reverse_lazy('mascota:mascota_listar')
