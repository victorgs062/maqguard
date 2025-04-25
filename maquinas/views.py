# FAZ IMPORAÇÕES NECESSÁRIAS PARA FUNCIONAR A LOGICA DO APP

from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import UltimaPreventiva, Patrimonio, AdicionarMaquina, AtualizarHorimetro
from .forms import PrevForm, Addmaq, Atualizar, UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User


# FUNÇÃO QUE CRIA A PÁGINA INICAIAL

@login_required
def index(request):
    query = request.GET.get('query', '')
    maq = AdicionarMaquina.objects.all()

    if query:
        try:
            # Tente converter query em inteiro para comparar com frota
            query_int = int(query)
            maq = AdicionarMaquina.objects.filter(
                Q(frota=query_int)  # Filtro exato
            )
        except ValueError:
            # Caso query não seja um número, retorna todos os objetos ou lida com o erro
            maq = AdicionarMaquina.objects.filter(
                Q(frota__icontains=query) | Q(modelo__icontains=query)
            )
    no_results = not maq.exists()



    paginator = Paginator(maq, 5)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)

    # CRIA UM DICIONÁRIO QUE DEFINE O VALOR DE maquinas PARA maq
    context = {'page': page, 'query': query, 'no_results': no_results}

    # RENDERIZA A PÁGINA DIRECIONANDO ELA PARA O CAMINHO maquinas/index.html E PASSA PARA O INDEX O CONTEXT PARA SER USADO NO INDEX
    return render(request, 'maquinas/index.html', context)



@login_required
def atualizarHor(request, maq_id):
    id_maq = AdicionarMaquina.objects.get(id = maq_id)
   
    # VARIAVEIS PARA EVITAR ERRO DE ACESSO A PÁGINA 
    primeira_valor = id_maq.Primeira or 0
    segunda_valor = id_maq.Segunda or 0
    hora1_valor = id_maq.hora1 or 0
    hora2_valor = id_maq.hora2 or 0
    horimetro_valor = id_maq.horimetro or 0

    faltam = (primeira_valor + hora1_valor) - horimetro_valor
    faltam2 = (segunda_valor + hora2_valor) - horimetro_valor
    h1 = id_maq.hora1
    h2 = id_maq.hora2

    passou = 0
    passou2 = 0

    if faltam < 0:
        passou = faltam * -1
    
    if faltam2 < 0:
        passou2 = faltam2 * -1


    preventivas = UltimaPreventiva.objects.filter(frota=id_maq.frota).order_by('-data') 

    mensagem = None

    if request.method != 'POST':
        form = Atualizar(instance=id_maq)
        prev_form = PrevForm()
    else:
        form = Atualizar(request.POST, instance=id_maq)
        prev_form = PrevForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atualizarHor', args=[maq_id]))
        
        if prev_form.is_valid():
            prev_form.save()
            return HttpResponseRedirect(reverse('atualizarHor', args=[maq_id]))
        
    mensagem = None
    
    
    if id_maq.horimetro is not None and id_maq.hora1 is not None and id_maq.horimetro >= id_maq.Primeira + id_maq.hora1:
        mensagem = f"É necessário realizar a manutenção preventiva de {id_maq.hora1}"

    if id_maq.horimetro is not None and id_maq.hora2 is not None and id_maq.horimetro >= id_maq.Segunda + id_maq.hora2:
        mensagem = f"É necessário realizar a manutenção preventiva de {id_maq.hora2}"
    

    
    context = {'id_maq': id_maq,
               'form': form,
               'mensagem': mensagem,
               'prev_form': prev_form,
               'preventivas': preventivas,
               'faltam': faltam,
               'faltam2': faltam2,
               'passou': passou,
               'passou2': passou2,
               'h1': h1,
               'h2': h2,
               }
    return render(request, 'maquinas/atualizarHor.html', context)

@login_required
def adicionarMaquina(request):

    if request.method != 'POST':
        form = Addmaq()
    else:
        form = Addmaq(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        
    context = {'form': form}
    return render(request, 'maquinas/addmaq.html', context)

def deletar(request, maq_id):
    maquina = get_object_or_404(AdicionarMaquina, id=maq_id)

    if request.method == 'POST':
        maquina.delete()
        messages.success(request, 'Máquina deletada com sucesso!')
        return redirect(index)
    
    context = {'maquina': maquina}
    return render(request, 'maquinas/deletar.html', context)

def manual(request):
    return render(request, 'maquinas/manual.html')

def deletar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)


    if user == request.user:
        messages.error(request, 'Você não pode deletar sua própra conta')
        return redirect("equipe")

    if request.method == 'POST':
        user.delete()
        return redirect('equipe')
    
    context = {'user': user}
    return render(request, 'maquinas/deletar_usuario.html', context)

def equipe(request):
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        account_type = request.POST.get('account_type')  

        # Validações básicas
        if password != password2:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('equipe')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe!')
            return redirect('equipe')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado!')
            return redirect('equipe')

        # Tipo da conta
        try:
            if account_type == 'superusuario':
                User.objects.create_superuser(username=username, email=email, password=password)
                messages.success(request, 'Conta de superusuário criada com sucesso!')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Conta de usuário criada com sucesso!')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao criar a conta: {e}')
            return redirect('equipe')

        return redirect('equipe')  # Substitua com a rota desejada após criação da conta

    return render(request, 'maquinas/equipe.html', context)