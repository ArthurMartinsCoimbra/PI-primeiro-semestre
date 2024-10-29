from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from .models import Lote, ProdutoNome
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoteModelForm
from mailersend import emails
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    lotes = Lote.objects.all()
    produtos = ProdutoNome.objects.all()
    context = {
        'lotes': lotes,
        'produtos': produtos
    }
    return render(request, 'home.html', context)

def product(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    produtos = ProdutoNome.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'product.html', context)


def login_submit(request):
    if request.method == 'POST':
        if request.POST:
            usuario = request.POST.get('usuario')
            senha = request.POST.get('senha')
            print(usuario)
            print(senha)
            user = authenticate(username=usuario, password=senha)
            if user:
                messages.success(request, 'Login com sucesso')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Erro: Usuario ou senha invalida')
                return render(request, 'login.html')
    messages.error(request, 'Erro ao logar, nao envio de dados')
    return render(request, 'login.html')



def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html')

def create_usuario(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.POST:
        print(request.POST.get('usuario'))
        print(request.POST.get('email'))
        print(request.POST.get('senha1'))
        print(request.POST.get('senha2'))
        if not request.POST.get('senha1'):
            return render(request, 'register.html')
        if not request.POST.get('senha2'):
            return render(request, 'register.html')
        if request.POST.get('senha1') == request.POST.get('senha2'):
            '''
            print(request.POST.get('usuario'))
            print(request.POST.get('email'))'''
            user = User.objects.create(
                username = request.POST.get('usuario'),
                email = request.POST.get('email'),
            )
            user.set_password(request.POST.get('senha1'))
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request='senhas não batem')
            return render(request, 'register.html')
        

def create_produto(request):
    if request.POST:
        if not request.POST.get('Nomeproduto'):
            return render(request, 'product.html')
        print(request.POST.get('Nomeproduto'))
        produto = ProdutoNome.objects.create(
            Nome = request.POST.get('Nomeproduto')
        )
        print(request.POST.get('Nomeproduto'))
        produto.save()
        return redirect('/produtos/')

def create_lote(request):
    if request.POST:
        AtribLote=['Nomelote', 'Quantlote','Nlotelote','Valilote','Usurlote']
        '''for Atrib in AtribLote:
            if not request.POST.get(Atrib):
                return render(request, 'home.html')'''
        lote = Lote.objects.create(
            Nome = request.POST.get('Nomelote'),
            Quantidade = request.POST.get('Quantlote'),
            Nlote = request.POST.get('Nlotelote'),
            Validade = request.POST.get('Valilote'),
            Usuario = request.user
        )
        lote.save()
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def delet_prod(request, coletNome):
    produto = get_object_or_404(ProdutoNome, Nome = coletNome)
    produto.delete()
    return redirect('/produtos/')

def delet_lote(request, coletNlote):
    lote = get_object_or_404(Lote, Nlote = coletNlote)
    lote.delete()
    return redirect('/')

def add_quant(request, pegNlote):
    lote = get_object_or_404(Lote, Nlote = pegNlote)
    quantidade  = int(request.POST.get('quantidade', 0))
    print(quantidade)
    lote.Quantidade += quantidade
    lote.save()
    return redirect('/')

def sub_quant(request, pegNlote):
    lote = get_object_or_404(Lote, Nlote = pegNlote)
    quantidade  = int(request.POST.get('quantidade', 0))
    if quantidade <= lote.Quantidade:
        lote.Quantidade -= quantidade
        lote.save()
        return redirect('/')
    else:
        return redirect('/')



def env_mail(dest, prod, linkform):
    mailer = emails.NewEmail(settings.MAILERSEND_API_KEY)

    subject = f'Preencha o seguinte formulário do produto: {prod}'
    body = f'O link do formulário é este: {linkform}'

    response = mailer.send(
    recipients = [dest],
    sender = settings.DEFAULT_FROM_EMAIL,
    subject = subject,
    text = body,
    html = body
    )

    return response

'''def createUser(request):
    if request.POST:
        if not request.POST.get('senha'):
            return render(request, 'register.html')
        if not request.POST.get('reptsenha'):
            return render(request, 'register.html')
        if request.POST.get('senha') == request.POST.get('reptsenha'):
            user = User.objects.create(
                username=request.POST.get('nome'),
                email=request.POST.get('email')
            )
            user.set_password(request.POST.get('senha'))
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request='senhas não batem')
            return render(request, 'register.html')
    return render(request, 'home.html')'''


def aaaa(request):
    pass