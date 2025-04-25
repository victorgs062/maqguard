# FAZ AS IMPORTAÇÕES DO DJANGO
from django.contrib import admin
from django.urls import path, include

# CRIA UMA LISTA ONDE FICAM OS CAMINHOS 
urlpatterns = [
    # O CAMINHO /ADMIN DIRECIONA O USUÁRIO PARA A PÁGINA DE ADMINISTRAÇÃO CRIADA PELO PRÓRPIO DJANGO
    path('admin/', admin.site.urls),
    # O CAMINHO VAZIO DEFINE, TODOS OS CAMINHOS QUE NÃO COMEÇAREM COM /ADMIN SERAM DIRECIONADOS PARA O APP maquinas
    path('', include('maquinas.urls')),
    
    path('users/', include('users.urls'))
]
