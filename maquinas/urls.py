# IMPORTA PATH DE DJANGO E IMPORTA OS COMPONENTES DE views.py PARA SEREM USADOS AQUI 
from django.urls import path
from . import views


# CRIA UMA LISTA COM AS URLS
urlpatterns = [
    # URL QUE DIRECIONA PARA A PÁGINA INDEX
    path('', views.index, name='index'),
    path('manual/', views.manual, name='manual'),  # Nova aba para o manual
    path('equipe/', views.equipe, name='equipe'),   # Nova aba para a equipe

    # URL QUE DIRECIONA PARA A PÁGINA DE MÁQUINAS QUE PRECISAM DE PREVENTIVA.
    # path('pendentes', views.pendentes, name='pendentes'),--------------------não utilizada

    path('adicionarMaquina/', views.adicionarMaquina, name='adicionarMaquina'),

    path('atualizarHor/<maq_id>/', views.atualizarHor, name='atualizarHor'),
    
    path('deletar/<maq_id>/', views.deletar, name='deletar'),

    path('deletar_usuario/<int:user_id>/', views.deletar_usuario, name='deletar_usuario')

]
