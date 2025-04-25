# IMPORTA UltimaPreventiva, Pecas, Patrimonio PARA SEREM RELACIONADOS COM OS FORMULARIOS
from django import forms
from .models import UltimaPreventiva, Pecas, Patrimonio, AdicionarMaquina, AtualizarHorimetro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# CRIA UM FOMULÁRIO PARA REGISTRAR PREVETNIVAS
class PrevForm(forms.ModelForm):
    # CRIA UM CAMPO DE CHECKBOX QUE PERMITE ESCOLHER AS PEÇAS USADAS
    pecas = forms.ModelMultipleChoiceField(queryset=Pecas.objects.all(), widget=forms.CheckboxSelectMultiple)

    # DEFINE QUAL MODELS DEVE SER USADO DE MODELO, NESSE CASO O UltimaPreventiva
    class Meta:
        model = UltimaPreventiva
        fields = ['frota', 'horimetro', 'modelo','HoradePreventiva','OS', 'data','pecas' ]
        labels = {'frota': '',
                  'horimetro': 'Horimetro de máquina',
                  'modelo': 'Modelo de máquina',
                  'HoradePreventiva': 'Preventiva de quantas horas',
                  'OS': 'Ordem de serviço',
                  'data': 'Data da preventiva',
                  'pecas': 'Peças usadas'}
        

    # GARANTE QUE O FORMULÁRIO SEJA INICIALIZADO DA MANEIRA CORRETA
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # GARANTE QUE O CAMPO pecas TENHA TODAS AS OPÇÕES CORRETAMENTE ESTABELECIDAS 
        self.fields['pecas'].queryset = Pecas.objects.all()
        

class Addmaq(forms.ModelForm):
    class Meta: 
        model = AdicionarMaquina
        fields = ['frota', 'modelo', 'horimetro', 'hora1', 'hora2']
        labels = {
            'frota': 'Número de frota',
            'modelo': 'Modelo de Máquina',
            'horimetro': 'Horimetro atual',
            'hora1': 'Primeira hora de preventiva',
            'hora2': 'Segunda hora de preventiva',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

class Atualizar(forms.ModelForm):

    class Meta: 
        model = AdicionarMaquina
        fields = ['horimetro', 'Primeira', 'Segunda']
        labels = {
            'horimetro': 'Horimetro atual',
            'Primeira': 'Horimetro quando realizou a primeira preventiva',
            'Segunda': 'Horimetro quando realizou a segunda preventiva',
        }

# Formulário para adicionar um usuário
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
