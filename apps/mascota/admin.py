from django.contrib import admin

from apps.mascota.models import Vacuna, Mascota
# Register your models here.
admin.site.register(Mascota)
admin.site.register(Vacuna)