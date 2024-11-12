# Generated by Django 5.1.3 on 2024-11-12 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Unidades Federativas',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('telefone', models.IntegerField(default=None)),
                ('cpf', models.IntegerField(default=0)),
                ('data_nascimento', models.DateField(default='2000-01-01')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('telefone', models.IntegerField(default=None)),
                ('cnpj', models.IntegerField(default=0)),
                ('razao_social', models.CharField(default=None, max_length=255)),
                ('data_fundacao', models.DateField(default='2000-01-01')),
                ('site', models.CharField(max_length=255)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Livro')),
                ('autores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor', verbose_name='Autores')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editora', verbose_name='Editora')),
                ('emprestimo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.emprestimo', verbose_name='Empréstimo')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero', verbose_name='Gênero')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='Uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uf'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('telefone', models.IntegerField(default=None)),
                ('cpf', models.IntegerField(default=0)),
                ('data_nascimento', models.DateField(default='2000-01-01')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
