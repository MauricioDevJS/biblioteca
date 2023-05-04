from django.shortcuts import render, HttpResponse
from .models import Livros

# Create your views here.

def index(request):
    livros = Livros.objects.all()
    return render(request, 'pages/index.html',{'livros' : livros})

def search(request):
    q = request.GET.get('search')
    livros = Livros.objects.filter(title__icontains = q)
    return render(request, 'pages/index.html',{'livros' : livros})