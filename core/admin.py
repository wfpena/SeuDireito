from django.contrib import admin

from core.models import Advogado, Empresa, OrdemServico

admin.site.register(Advogado)
admin.site.register(Empresa)
admin.site.register(OrdemServico)
