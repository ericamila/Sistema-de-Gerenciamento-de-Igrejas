# Generated by Django 5.0.2 on 2025-04-26 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('churches', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('start_date', models.DateField(verbose_name='Data de Início')),
                ('end_date', models.DateField(verbose_name='Data de Término')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='churches.church', verbose_name='Igreja')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.person', verbose_name='Instrutor')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True, verbose_name='Data de Matrícula')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.course', verbose_name='Curso')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'unique_together': {('person', 'course')},
            },
        ),
    ]
