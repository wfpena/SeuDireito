from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register("empresa", views.EmpresaViewSet)
router.register("ordem", views.OrdemServicoViewSet)
router.register("preco", views.PrecoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
