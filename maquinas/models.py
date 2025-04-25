from django.db import models
from django import forms


# será lançado as novos registros para serem comparados com as ultimas preventivas
class Patrimonio(models.Model):
    # CRIA UM CAMPO DE NÚMEROS INTEIROS E DA O NOME DE 'Número de frota'
    frota = models.IntegerField(verbose_name='Número de frota')

    # CRIA UM CAMPO DE NÚMEROS INTEIROS E DA O NOME DE 'Horimetro de máqiuna'
    horimetro = models.IntegerField(default=0, verbose_name='Horimetro de máquina')

    # FUNÇÃO QUE RETORNARÁ NA PÁGINA DE ADMIN OS VALORES DE FROTA E HORIMETRO
    def __str__(self):  
        return f"frota{self.frota} hor: {self.horimetro}"
    


# será registrado as preventiva de máquinas 
class Pecas(models.Model):
    # CRIA UM CAMPO DE STR PARA O NOME DAS PECAS USADAS
    nome = models.CharField(max_length=150)

    # FUNÇÃO QUE RETORNARÁ NA PÁGINA DE ADMIN OS VALORES DE NOME
    def __str__(self):
        return self.nome


# CLASS QUE REGISTRA A ULTIMA PREVENTIVA DE UMA MÁQUINA
class UltimaPreventiva(models.Model):

    # CRIA UM CAMPO DE NUMERO INTEIRO E PASSA O VALOR INICIAL VAZIO
    frota = models.IntegerField(default = 0, verbose_name='Número de frota')

    # CRIA UM CAMPO DE NUMERO INTEIRO E PASSA O VALOR INICIAL VAZIO
    horimetro = models.IntegerField(default = 0, verbose_name='Horimetro de máquina')

    # CRIA UM CAMPO DE STR E PASSA O VALOR INICIAL VAZIO
    modelo = models.CharField(default= '',max_length=100, verbose_name='Modelo de máquina')

    # CRIA UM CAMPO DE NUMERO INTEIRO E PASSA O VALOR INICIAL VAZIO
    HoradePreventiva = models.IntegerField(default =0,verbose_name='Preventiva de quantas horas')
    
    # CRIA UM CAMPO DE NUMERO INTEIRO E PASSA O VALOR INICIAL VAZIO
    OS = models.IntegerField(default = 0,verbose_name='Ordem de serviço')

    data = models.DateField(null=True, blank=True, verbose_name='Data da ultima preventiva')
    
    # CRIA UM CAMPO DE RELAÇÃO MUITOS PARA MUITOS DE PEÇAS, OU SEJA UMA UNICA MÁQUINA PODE TER MUITAS PEÇAS
    pecas = models.ManyToManyField(Pecas, verbose_name='Peças usadas')

    # @property PERMITE QUE OS VALORES DE  proximaPrev SEJAM ACESSADOS FACILMENTE
    @property
    def proximaPrev(self): 
        # FUNÇÃO QUE CALCULA COM QUANTAS HORAS SERAM FEITAS AS PROXIMAS PREVENTIVAS
        return self.horimetro + self.HoradePreventiva
    
    def __str__(self):
        return f"Frota: {self.frota} OS: {self.OS}" 

class ModeloMaquina(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Modelo de Máquina')

    def __str__(self):
        return self.nome

class AdicionarMaquina(models.Model):
    frota = models.IntegerField(default=0, verbose_name='Número de frota')
    modelo = models.ForeignKey(ModeloMaquina, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Modelo de Máquina')
    horimetro = models.IntegerField(default=0, verbose_name='Horimetro atualizado')
    Primeira = models.IntegerField(default=0, verbose_name='Horimetro da primerira preventiva')
    Segunda = models.IntegerField(default=0, verbose_name='Horimetro da segunda preventiva')
    Terceira = models.IntegerField(default=0, verbose_name='Horimetro da terceira preventiva')
    hora1 = models.IntegerField(verbose_name='Horas para preventiva 1', blank=True, null=True)
    hora2 = models.IntegerField(verbose_name='Horas para preventiva 2', blank=True, null=True)
    hora3 = models.IntegerField(verbose_name='Horas para preventiva 3', blank=True, null=True)
    hora4 = models.IntegerField(verbose_name='Horas para preventiva 4', blank=True, null=True)
    
    def __str__(self):
        return f"Frota: {self.frota} - Modelo: {self.modelo}"
    
class AtualizarHorimetro(models.Model):
    horimetro = models.IntegerField(default=0, verbose_name='Horimetro atualizado')
    def __str__(self):
        return f"Horimetro: {self.horimetro}"
    
    