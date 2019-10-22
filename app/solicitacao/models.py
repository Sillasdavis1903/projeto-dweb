from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Motorista(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'Usuário')
    endereco = models.TextField(verbose_name = 'Endereço')
    data = models.DateField(verbose_name = 'Data')
    hora = models.TimeField(verbose_name = 'Hora')
    solicitacao = models.DateTimeField(verbose_name = 'Data da Solicitação', auto_now_add = True)

    def __str__(self):
        return 'Corrida de %s' % self.user.first_name

class Pedreiro(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'Usuário')
    descricao = models.TextField(verbose_name = 'Descrição do Serviço')
    solicitacao = models.DateTimeField(verbose_name = 'Data da Solicitação', auto_now_add = True)

    def __str__(self):
        return 'Solicitação de %s' % self.user.first_name

class Professor(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'use', verbose_name = 'Usuário')
    materia = models.CharField(max_length = 100, verbose_name = 'Matéria')
    descricao = models.TextField(verbose_name = 'Descrição do Problema')
    solicitacao = models.DateTimeField(verbose_name = 'Data da Solicitação', auto_now_add = True)

    def __str__(self):
        return 'Aula de %s' % self.user.first_name

class Cozinheiro(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'usuario', verbose_name = 'Usuário')
    descricao = models.TextField(verbose_name = 'Descrição da Refeição')
    solicitacao = models.DateTimeField(verbose_name = 'Data da Solicitação', auto_now_add = True)

    def __str__(self):
        return 'Refeição de %s' % self.user.first_name