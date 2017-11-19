from django.contrib.auth.models import AbstractUser
from django.db import models

ORDEM_STATUS = (
    ('0', 'Criada'),
    ('1', 'Delegada'),
    ('2', 'Finalizada'),
)

class UserProfile(AbstractUser):
    type_choices = (
        ('ADV', 'Advogado'),
        ('EMP', 'Empresa'),
    )
    user_type = models.CharField(max_length=4,
                                 choices=type_choices,
                                 default='ADM')

class Advogado(UserProfile):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=32, null=True, blank=True)
    telefone = models.CharField(max_length=32)

class Empresa(UserProfile):
    nome_razao_social = models.CharField(max_length=255)
    ramo = models.CharField(max_length=100)

class OrdemServico(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa,
                                related_name='empresa',
                                blank=True, null=True)
    status = models.CharField(max_length=1,
                              choices=ORDEM_STATUS,
                              default='0')
    preco_advogado = models.ManyToManyField(
        Advogado,
        related_name='advogados_ordem',
        through='Preco')

    def __unicode__(self):
        return 'Ordem: ' + self.titulo

    def __str__(self):
        return 'Ordem: ' + self.titulo

class Preco(models.Model):
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    ordem = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    preco = models.FloatField()
    delegada = models.BooleanField(default=False)
