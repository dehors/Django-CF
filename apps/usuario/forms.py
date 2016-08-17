from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ResgistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Primer nombre',
			'last_name': 'Segundo nombre',
			'email': 'Correo',
		}