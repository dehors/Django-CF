from django.conf.urls import include, url

from apps.mascota.views import index

urlpatterns = [
    url(r'^$', index),
]