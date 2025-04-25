from django.contrib import admin
from maquinas.models import Patrimonio
from maquinas.models import UltimaPreventiva
from maquinas.models import Pecas
from maquinas.models import AdicionarMaquina
from maquinas.models import ModeloMaquina
from maquinas.models import AtualizarHorimetro

# DEFINE OS MODELS PRESENTES NA PAGINA ADMINISTRATIVA
admin.site.register(Patrimonio)
admin.site.register(UltimaPreventiva)
admin.site.register(Pecas)
admin.site.register(AdicionarMaquina)
admin.site.register(ModeloMaquina)
admin.site.register(AtualizarHorimetro)
