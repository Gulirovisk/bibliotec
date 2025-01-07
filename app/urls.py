from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('autor/', views.AutorView.as_view(), name='autor'),
    path('cidade/', views.CidadeView.as_view(), name='cidade'),
    path('editora/', views.EditoraView.as_view(), name='editora'),
    path('emprestimo/', views.EmprestimoView.as_view(), name='emprestimo'),
    path('genero/', views.GeneroView.as_view(), name='genero'),
    path('pessoafisica/', views.PessoaFisicaView.as_view(), name='pessoafisica'),
    path('pessoajuridica/', views.PessoaJuridicaView.as_view(), name='pessoajuridica'),
    path('livros/', views.LivrosView.as_view(), name='livros'),
    path('uf/', views.UfView.as_view(), name='uf'),
    path('usuario/', views.UsuarioView.as_view(), name='usuario'),
    path('admin/', views.AdmView.as_view(), name='adm'),

]