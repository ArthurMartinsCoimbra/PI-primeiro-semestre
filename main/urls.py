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
from core.views import home, product, register, index, create_usuario, login_user, login_submit, create_produto, logout_view, create_lote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produtos/', product, name = 'produtos'),
    path('cadastro/', register, name= 'cadastro'),
    path('teste/', index),
    path('cadastro/submit', create_usuario, name = 'create_usuario'),
    path('login/', login_user, name='login'),
    path('login/submit', login_submit, name='login_submit'),
    path('produtos/submit', create_produto, name = 'produtossubmit'),
    path('logout/', logout_view, name='logout'),
    path('submit/', create_lote, name = 'lotessubmit')
]
