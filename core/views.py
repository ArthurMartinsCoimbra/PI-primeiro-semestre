from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
from .models import Lote, ProdutoNome, Fornecedor, MovProd
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoteModelForm
from mailersend import emails
from django.conf import settings
from django.core.mail import EmailMessage, get_connection, send_mail
from django.utils import timezone
from datetime import date
import mailersend
import json
# Create your views here.


def index(request):
    prod = get_object_or_404(ProdutoNome, Nome = 'ry5y545y46')

    email1 = prod.Formail1
    email2 = prod.Formail2
    email3 = prod.Formail3
    email4 = prod.Formail4
    email5 = prod.Formail5

    emails = [email1, email2, email3, email4, email5]
    emailspure = []
    for em in emails:
        for i in em:
            if i == '@':
                emailspure.append(em)
    print(emails)
    print(emailspure)
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
    fornecedores = Fornecedor.objects.all()
    context = {
        'produtos': produtos,
        'fornecedores': fornecedores
    }
    return render(request, 'product.html', context)

def forn(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
    }
    return render(request, 'supplier.html', context)



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
        
def create_forn(request):
    if request.POST:
        Atribforn = ['Nomefornecedor', 'Emailfornecedor']
        forner = Fornecedor.objects.create(
            Emailforn = request.POST.get('Emailfornecedor'),
            Nome = request.POST.get('Nomefornecedor')
        )
        forner.save()
    return redirect('/forn/')



def create_produto(request):
    if request.POST:
        Atribprod = ['Nome', 'Formail1', 'Formail2', 'Formail3', 'Formail4', 'Formail5']
        if not request.POST.get('Nomeproduto'):
            return render(request, 'product.html')
        print(request.POST.get('Nomeproduto'))
        produto = ProdutoNome.objects.create(
            Nome = request.POST.get('Nomeproduto'),
            Formail1 = request.POST.get('Formail1produto'),
            Formail2 = request.POST.get('Formail2produto'),
            Formail3 = request.POST.get('Formail3produto'),
            Formail4 = request.POST.get('Formail4produto'),
            Formail5 = request.POST.get('Formail5produto')
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

    produto = ProdutoNome.objects.get(Nome = lote.Nome)

    MovProd.objects.create(
        Produto = produto,
        Tipo = "entrada",
        Data = date.today(),
        Quantidade = lote.Quantidade
    )

    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def delet_prod(request, coletNome):
    produto = get_object_or_404(ProdutoNome, Nome = coletNome)
    produto.delete()
    return redirect('/produtos/')

def delet_forn(request, coletFornEmail):
    forn = get_object_or_404(Fornecedor, Emailforn = coletFornEmail)
    forn.delete()
    return redirect('/forn/')

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
    produto = ProdutoNome.objects.get(Nome = lote.Nome)
    if quantidade > 0:
        tipo = "entrada"
        MovProd.objects.create(
        Produto = produto,
        Tipo = tipo,
        Data = date.today(),
        Quantidade = quantidade
    )
    elif quantidade < 0:
        tipo = "saida"
        quantidade *= -1
        MovProd.objects.create(
            Produto = produto,
            Tipo = tipo,
            Data = date.today(),
            Quantidade = quantidade
        )

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


def enviar_em(request, prodid):
    prod = get_object_or_404(ProdutoNome, Nome = prodid)
    
    email1 = prod.Formail1
    email2 = prod.Formail2
    email3 = prod.Formail3
    email4 = prod.Formail4
    email5 = prod.Formail5

    emailsfor = [email1, email2, email3, email4, email5]
    emailspure = []
    linkforms = 'https://docs.google.com/forms/d/e/1FAIpQLSe7xfz5brAOtG2HsIkJtTU71AIqGtvfWKfFg3faC-0tuentzg/viewform?usp=sf_link'
    for em in emailsfor:
        for i in em:
            if i == '@':
                emailspure.append(em)
    if emailspure != []:
        send_mail(
            f'Requisição do produto {prod.Nome}',
            f'Olá, segue o link para a cotação do produto {prod.Nome}, por favor, preencher para que eu possa saber o preço {linkforms}',
            'settings.EMAIL_HOST_USER',
            emailspure,
            fail_silently=False
        )

    return redirect('/produtos/')

def quantidade_graf(request):
    produtos=ProdutoNome.objects.all()
    nomes = []
    quantidades = []

    for produto in produtos:
        total = Lote.objects.filter(Nome = produto.Nome).aggregate(soma=Sum('Quantidade'))['soma'] or 0


        nomes.append(produto.Nome)
        quantidades.append(float(total))

    context = {
        'nomes' : json.dumps(nomes),
        'quantidades' : json.dumps(quantidades),
    }
    print(nomes)
    print(quantidades)

    return render(request, 'grafico.html', context)






'''
    email_data = {
        'from' :{
            'email':'amc5347@gmail.com',
            'name': 'Nometeste'
        },
        'to': [{'email':email} for email in emailspure],
        'subject': 'Pedido de produto',
        'html': '<p>Este é o meu email de teste</p>'

    }

    try:
        response = mailersend.send(email_data)
        print(response)
        return HttpResponse('Emails enviados com sucesso')
    except Exception as e:
        return HttpResponse(f'Erro ao enviar: {e}', status = 500)

    return redirect('/produtos/')

    
    mailersend = emails.NewEmail(settings.MAILERSEND_API_KEY)
    print(emailspure)
    subject = 'Teste de requisicao'
    recipient_list = emailspure
    from_email = 'amc5347@gmail.com'
    message = '<p>Este e o meu email de teste</p>'
    host1=settings.MAILERSEND_SMTP_HOST
    print(host1)
    with get_connection(
        host=settings.MAILERSEND_SMTP_HOST,
        port=settings.MAILERSEND_SMTP_PORT,
        username=settings.MAILERSEND_SMTP_USERNAME,
        password='pYmituV9VgvhA1HB',
        use_tls=True,
        ) as connection:
            r = EmailMessage(
                  subject=subject,
                  body=message,
                  to=recipient_list,
                  from_email=from_email,
                  connection=connection).send()
    return JsonResponse({"status": "ok"})



'''


'''def env_mail(dest, prod, linkform):
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

    return response'''

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