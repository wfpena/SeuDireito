from django.conf.urls import url, include
from django.contrib import admin

from core import urls as coreurls
from seudireito.views import (
    LoginView,
    UserLogoutView,
    CadastroView,
    EmpresaView,
    AdvogadoView,
)

app_name = 'seudireito'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(coreurls)),
    url(r'^logout/$', UserLogoutView.as_view(), name='logoutview'),
    url(r'^login/$', LoginView.as_view(), name='loginview'),

    # App core modules
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastroview'),
    url(r'^empresa/$', EmpresaView.as_view(), name='empresaview'),
    url(r'^advogado/$', AdvogadoView.as_view(), name='advogadoview'),
]
