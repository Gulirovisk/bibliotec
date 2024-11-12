# Generated by Django 5.1.3 on 2024-11-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_autor_cpf_alter_autor_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='cnpj',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
