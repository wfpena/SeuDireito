from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Empresa, OrdemServico, Preco, Advogado


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'nome_razao_social')

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ('id', 'nome')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrdemSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = OrdemServico
        fields = ('id', 'titulo', 'status')

class PrecoSerializer(serializers.ModelSerializer):
    advogado = AdvogadoSerializer()
    ordem = OrdemSerializer()

    class Meta:
        model = Preco
        fields = '__all__'

class OrdemServicoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    preco_advogado = PrecoSerializer(source='preco_set', read_only=True, many=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = OrdemServico
        fields = '__all__'
