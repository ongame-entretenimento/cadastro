from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'usuario.views.cadastro', name='home'),
    url(r'^cadastro/cadastrar/', 'usuario.views.cadastrar'),
    url(r'^cadastro/ativar/(?P<codigo>.+)/$', 'usuario.views.ativar'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
