from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UfAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla',)
    inlines = [CidadeInline,]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline,]

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome','cidade',)
    search_fields = ('nome','cidade',)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','cidade',)
    search_fields = ('nome','cidade',)
    inlines = [LivroInline,]

class EmprestimoAdmin(admin.ModelAdmin):
    class LivroInline(admin.TabularInline):
        model = Emprestimo.livros.through
        extra = 1
    list_display = ('usuario','data_emprestimo','data_devolucao',)
    search_fields = ('usuario',)
    inlines = [LivroInline]
    exclude = ['livros']

admin.site.register(Uf, UfAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro)
admin.site.register(Emprestimo, EmprestimoAdmin)
