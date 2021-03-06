from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.viewsets import ModelViewSet, ViewSet

from core.models import Empresa, Advogado, OrdemServico, Preco
from core.serializers import (
    EmpresaSerializer,
    OrdemServicoSerializer,
    PrecoSerializer,
)


class EmpresaViewSet(ViewSet):
    serializer_class = EmpresaSerializer
    permission_classes = (AllowAny,)
    queryset = Empresa.objects.all()

    def create(self, validated_data):
        if validated_data.data['type'] == 2:
            obj = Empresa.objects.create(
                username=validated_data.data['username'],
                nome_razao_social=validated_data.data['username'])
            obj.ramo = validated_data.data['ramo']
            obj.set_password(validated_data.data['password'])
            obj.user_type = "EMP"
            obj.save()
        else:
            obj = Advogado.objects.create(
                username=validated_data.data['username'],
                nome=validated_data.data['username'])
            obj.cpf = validated_data.data['cpf']
            if validated_data.data['telefone']:
                obj.telefone = validated_data.data['telefone']
            obj.set_password(validated_data.data['password'])
            obj.user_type = "ADV"
            obj.save()

        user = authenticate(username=validated_data.data['username'],
                            password=validated_data.data['password'])
        if user:
            login(self.request, user)
            return redirect('indexview')
        else:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


class OrdemServicoViewSet(ModelViewSet):
    serializer_class = OrdemServicoSerializer
    queryset = OrdemServico.objects.all()

    @detail_route(methods=['get'])
    def finaliza_ordem(self, request, pk=None):
        ordem = OrdemServico.objects.get(id=pk)
        ordem.status = 2
        ordem.save()
        return Response(
            self.serializer_class(ordem).data,
            status=HTTP_200_OK)


    @list_route(methods=['post'])
    def delegate_ordem(self, request):
        ordem = OrdemServico.objects.get(id=request.data['id'])
        if ordem.status == '0':
            ordem.status = '1'
            ordem.save()
            preco = Preco.objects.get(
                ordem__id=ordem.id,
                advogado__id=request.data['advogado'])
            preco.delegada = True
            preco.save()
            return Response(
                self.serializer_class(ordem).data,
                status=HTTP_200_OK)
        else:
            return Response(
                self.serializer_class(ordem).data,
                status=HTTP_409_CONFLICT)

    @list_route(methods=['get'])
    def advogado_ordens(self, request, pk=None):
        ordens = Preco.objects.filter(advogado=request.user)
        return Response(PrecoSerializer(ordens).data)

    def get_queryset(self):
        if self.request.user.user_type == 'EMP':
            return OrdemServico.objects.all().filter(
                empresa_id=self.request.user.id)
        else:
            return OrdemServico.objects.all()

    def create(self, request, *args, **kwargs):
        empresa = Empresa.objects.get(id=self.request.user.id)
        obj = OrdemServico.objects.create(
            titulo=request.data['titulo'],
            descricao=request.data['descricao'],
            empresa=empresa)
        obj.save()
        return Response(self.serializer_class(obj).data)


class PrecoViewSet(ModelViewSet):
    serializer_class = PrecoSerializer
    queryset = Preco.objects.all()

    # Recebe o id do advogado e retorna as ordens enviadas por ele
    @list_route(methods=['get'])
    def ordens_advogado(self, request, *args, **kwargs):
        advogado = Advogado.objects.get(id=request.user.id)
        ordens_enviadas = Preco.objects.filter(advogado=advogado)
        return Response(PrecoSerializer(ordens_enviadas, many=True).data)

    # Recebe o id da ordem de servico e retorna a ordem com seus precos
    @list_route(methods=['get'])
    def list_precos(self, request, *args, **kwargs):
        ordem = OrdemServico.objects.get(id=request.query_params['id'])
        ordem_json = OrdemServicoSerializer(ordem)
        return Response(ordem_json.data)

    def create(self, request, *args, **kwargs):
        advogado = Advogado.objects.get(id=self.request.user.id)
        ordem = OrdemServico.objects.get(id=self.request.data['ordem'])
        try:
            preco = Preco.objects.get(
                advogado=advogado,
                ordem=ordem)
            preco.preco = self.request.data['preco']
            preco.save()
        except:
            preco = Preco.objects.create(
                advogado=advogado,
                ordem=ordem,
                preco=self.request.data['preco'])
        return Response(self.serializer_class(preco).data)
