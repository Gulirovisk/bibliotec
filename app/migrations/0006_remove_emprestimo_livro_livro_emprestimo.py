# Generated by Django 5.1.3 on 2024-11-05 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cidade_options_alter_emprestimo_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro',
        ),
        migrations.AddField(
            model_name='livro',
            name='emprestimo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.emprestimo', verbose_name='Empréstimo'),
        ),
    ]
