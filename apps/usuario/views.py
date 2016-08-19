import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import ResgistroForm
from rest_framework.views import APIView
from apps.usuario.serialize import UserSerializer

class  RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = ResgistroForm
	success_url = reverse_lazy('mascota:mascota_listar')

class UserAPI(APIView):
	serializer = UserSerializer
	def get(self, resource, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')