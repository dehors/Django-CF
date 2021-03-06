from django.conf.urls import url

from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitud/listar', SolicitudList.as_view(),name='solicitud_listar'),
    url(r'^solicitud/nueva', SolicitudCreate.as_view(),name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(),name='solicitud_editar'),
]