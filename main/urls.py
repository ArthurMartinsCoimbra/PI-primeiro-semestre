"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, product, register, index, create_usuario, login_user, login_submit, create_produto, logout_view, create_lote, delet_prod, delet_lote, add_quant, sub_quant, forn, create_forn, delet_forn, enviar_em, quantidade_graf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produtos/', product, name = 'produtos'),
    path('cadastro/', register, name= 'cadastro'),
    path('forn/', forn, name = 'fornecedor'),
    path('teste/', index),
    path('cadastro/submit', create_usuario, name = 'create_usuario'),
    path('login/', login_user, name='login'),
    path('login/submit', login_submit, name='login_submit'),
    path('produtos/submit', create_produto, name = 'produtossubmit'),
    path('fornecedores/submit', create_forn, name = 'fornsubmit'),
    path('logout/', logout_view, name='logout'),
    path('submit/', create_lote, name = 'lotessubmit'),
    path('produtos/produtosdel/<str:coletNome>/', delet_prod, name = 'proddelet'),
    path('forn/forndel/<str:coletFornEmail>/', delet_forn, name = 'forndelet'),
    path('lotesdel/<str:coletNlote>/', delet_lote, name = 'lotedelet'),
    path('add/<str:pegNlote>/', add_quant, name = 'addquant'),
    path('sub/<str:pegNlote>/', sub_quant, name = 'subquant'),
    path('produtos/envmail/<str:prodid>/', enviar_em, name = 'enviar_email_forn'),
    path('analytcs/', quantidade_graf, name = 'graf'), 
    ]
