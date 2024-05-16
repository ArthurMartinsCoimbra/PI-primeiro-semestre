from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Lote, ProdutoNome
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoteModelForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def home(request):
    lotes = Lote.objects.all()
    context = {
        'lotes': lotes
    }
    return render(request, 'home.html', context)

def product(request):
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