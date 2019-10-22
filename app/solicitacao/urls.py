from django.urls import include, path
from . import views as solicitacao

app_name = 'solicitacao'

urlpatterns = [
    path('', solicitacao.Home.as_view(), name = 'home'),
    # adição
    path('nova/solicitacao/motorista/', solicitacao.AddMotorista.as_view(), name = 'add-motorista'),
    path('nova/solicitacao/pedreiro/', solicitacao.AddPedreiro.as_view(), name = 'add-pedreiro'),
    path('nova/solicitacao/cozinheiro/', solicitacao.AddCozinheiro.as_view(), name = 'add-cozinheiro'),
    path('nova/solicitacao/professor/', solicitacao.AddProfessor.as_view(), name = 'add-professor'),
    # listagem adm
    path('lista/solicitacoes/motorista/', solicitacao.AdmMotorista.as_view(), name='adm-motorista'),
    path('lista/solicitacoes/pedreiro/', solicitacao.AdmPedreiro.as_view(), name='adm-pedreiro'),
    path('lista/solicitacoes/cozinheiro/', solicitacao.AdmCozinheiro.as_view(), name='adm-cozinheiro'),
    path('lista/solicitacoes/professor/', solicitacao.AdmProfessor.as_view(), name='adm-professor'),
    # listagem user
    path('lista/minhas/solicitacoes/motorista/', solicitacao.UserMotorista.as_view(), name='user-motorista'),
    path('lista/minhas/solicitacoes/pedreiro/', solicitacao.UserPedreiro.as_view(), name='user-pedreiro'),
    path('lista/minhas/solicitacoes/cozinheiro/', solicitacao.UserCozinheiro.as_view(), name='user-cozinheiro'),
    path('lista/minhas/solicitacoes/professor/', solicitacao.UserProfessor.as_view(), name='user-professor'),
    # visualizar solicitacao
    path('visualizar/solicitacao/<pk>/', solicitacao.Visualizar.as_view(), name = 'visualizar')
]