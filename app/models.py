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
<<<<<<< HEAD
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
=======

class Usuario(models.Model):
    nome= models.CharField(max_length=255)
    cpf= models.CharField(max_length=11, unique=True)
    data_nascimento= models.DateField()
    email= models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)
>>>>>>> 56ca819e743752563115669e6112d16d187fc9e5

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=255, default= None)
    data_nascimento = models.DateField(default='2000-01-01')

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=255, default= None)  
    razao_social = models.CharField(max_length=255, default= None)
    data_fundacao = models.DateField(default= '2000-01-01')

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nome
    
class Autor(PessoaFisica):
    pass

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Editora(PessoaJuridica):
    site =  models.URLField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
    
class Usuario(PessoaFisica):
    pass
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
 
class Genero(models.Model):
    nome= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Gêneros'
    def __str__(self):
        return self.nome


<<<<<<< HEAD
class Emprestimo(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)    
    data_emprestimo= models.DateField(null=True, blank=True, default= '2000-01-01')
    data_devolucao= models.DateField(null=True, blank=True, default= '2000-01-01')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
    
    def __str__(self):
        return f'{self.usuario} - {self.data_emprestimo}'
    
=======
>>>>>>> 56ca819e743752563115669e6112d16d187fc9e5
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