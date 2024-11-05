from django.db import models


class Uf(models.Model): # generos com seus livros, uf com suas cidades, emprestimos com seus livros, autores com seus livros
    sigla= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Unidades Federativas'
    
    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome= models.CharField(max_length=255)
    Uf= models.ForeignKey(Uf, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    def __str__(self):
        return f'{self.nome} - {self.Uf}'


class Usuario(models.Model):
    nome= models.CharField(max_length=255)
    cpf= models.CharField(max_length=11, unique=True)
    data_nascimento= models.DateField()
    email= models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Usuários'
    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    nome= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Gêneros'
    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome= models.CharField(max_length=255)
    site= models.URLField()
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Editoras'
    
    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome= models.CharField(max_length=255)
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome= models.CharField(max_length=200, verbose_name= 'Nome do Livro')
    genero= models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name= 'Gênero')
    editora= models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name= 'Editora')
    autores= models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name= 'Autores')
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return f'{self.nome} - {self.genero}'
class Emprestimo(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livros= models.ManyToManyField(Livro)
    data_emprestimo= models.DateField()
    data_devolucao= models.DateField(null=True, blank=True)


    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
    
    def __str__(self):
        return f'{self.usuario} - {self.data_emprestimo}'
    
