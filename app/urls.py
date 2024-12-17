from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('livros/', views.LivrosView.as_view(), name='livros'),
    path('admin/', views.AdmView.as_view(), name='adm'),

]