from django.conf.urls import url, include
from django.contrib import admin
from django.template.context_processors import static

from core import urls as coreurls
from seudireito import settings
from seudireito.views import LoginView, UserLogoutView, IndexView, CadastroView, EmpresaView, AdvogadoView
from rest_framework.authtoken import views as rest_framework_views

app_name = 'seudireito'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(coreurls)),
    url(r'^logout/$', UserLogoutView.as_view(), name='logoutview'),

    url(r'^$', EmpresaView.as_view(), name='indexview'),
    url(r'^login/$', LoginView.as_view(), name='loginview'),

    url(r'^cadastro/$', CadastroView.as_view(), name='cadastroview'),
    url(r'^empresa/$', EmpresaView.as_view(), name='empresaview'),
    url(r'^advogado/$', AdvogadoView.as_view(), name='advogadoview'),
]
