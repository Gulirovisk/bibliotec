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

class AutorView(View):
    def get(self, request):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

    def post(self, request):
        pass

class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

    def post(self, request):
        pass
class EditoraView(View):
    def get(self, request):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

    def post(self, request):
        pass

class EmprestimoView(View):
    def get(self, request):
        emprestimos = Emprestimo.objects.all()
        return render(request, 'emprestimo.html', {'emprestimos': emprestimos})

    def post(self, request):
        pass

class GeneroView(View):
    def get(self, request):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

    def post(self, request):
        pass

class PessoaFisicaView(View):
    def get(self, request):
        pessoasfisicas = PessoaFisica.objects.all()
        return render(request, 'pessoafisica.html', {'pessoafisica': pessoasfisicas})

    def post(self, request):
        pass

class PessoaJuridicaView(View):
    def get(self, request):
        pessoasjuridicas = PessoaJuridica.objects.all()
        return render(request, 'pessoajuridica.html', {'pessoajuridica': pessoasjuridicas})

    def post(self, request):
        pass

class LivrosView(View):
    def get(self, request):
        livros = Livro.objects.all()
        return render(request, 'livros.html' , {'livros': livros})

    def post(self, request):
        pass
class UfView(View):
    def get(self, request):
        ufs = Uf.objects.all()
        return render(request, 'ufs.html', {'uf': ufs})

    def post(self, request):
        pass

class UsuarioView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        print(usuarios)
        return render(request, 'usuarios.html', {'usuarios': usuarios})

    def post(self, request):
        pass

class AdmView(View):
    def get(self, request):
        return render(request, 'adm.html')

    def post(self, request):
        pass