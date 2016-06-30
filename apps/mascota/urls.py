from django.conf.urls import include, url

from apps.mascota.views import index, mascota_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo', mascota_view, name='mascota_crear'),
]