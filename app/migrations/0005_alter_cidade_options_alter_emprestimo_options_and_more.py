# Generated by Django 5.1.3 on 2024-11-05 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_livro_devolucao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'verbose_name': 'Empréstimo', 'verbose_name_plural': 'Empréstimos'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterField(
            model_name='livro',
            name='autores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor', verbose_name='Autores'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editora', verbose_name='Editora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero', verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome do Livro'),
        ),
    ]