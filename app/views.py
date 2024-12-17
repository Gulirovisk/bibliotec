from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django import forms

class IndexView(View):
    def get(self, request):
        uf = Uf.objects.all()
        return render(request, 'index.html', {'Uf': uf})
    
    def post(self, request):
        pass

class LivrosView(View):
    def get(self, request):
        livros = Livro.objects.all()
        return render(request, 'livros.html' , {'livro': livros})

    def post(self, request):
        pass


class AdmView(View):
    def get(self, request):
        return render(request, 'adm.html')

    def post(self, request):
        pass