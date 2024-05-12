from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def registerUserScreen(request):
    return render(request, 'registerUserScreen.html')