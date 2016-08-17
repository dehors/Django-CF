from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'refugio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('apps.mascota.urls',namespace="mascota")),
    url(r'^adopcion/', include('apps.adopcion.urls',namespace="adopcion")),
    url(r'^usuario/', include('apps.usuario.urls',namespace="usuario")),
    url(r'^$', login,{'template_name':'index.html'}, name="login"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)