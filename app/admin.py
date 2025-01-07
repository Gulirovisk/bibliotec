from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UfAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla',)
    inlines = [CidadeInline]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class livroInline(admin.TabularInline):
    model = Livro
    extra = 1

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [livroInline]

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [livroInline]

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_emprestimo', 'data_devolucao')
    search_fields = ('usuario__nome',)


admin.site.register(Uf, UfAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Livro)
admin.site.register(Emprestimo, EmprestimoAdmin)
