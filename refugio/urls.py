from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # Examples:
    # url(r'^$', 'refugio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('apps.mascota.urls',namespace="mascota")),
    url(r'^adopcion/', include('apps.adopcion.urls',namespace="adopcion")),
    url(r'^usuario/', include('apps.usuario.urls',namespace="usuario")),
    url(r'^accounts/login/', login,{'template_name':'index.html'}, name="login"),
    url(r'^logout/', logout_then_login,name="logout"),
    url(r'^reset/password_reset', password_reset,{'template_name':'registration/password_reset_form.html','email_template_name':'registration/password_reset_email.html'},name="password_reset"),
    url(r'^reset/password_reset_done', password_reset_done,{'template_name':'registration/password_reset_done.html'},name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name':'registration/password_reset_confirm.html'},name="password_reset_confirm"),
    url(r'^reset/done', password_reset_complete,{'template_name':'registration/password_reset_complete.html'},name="password_reset_complete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)