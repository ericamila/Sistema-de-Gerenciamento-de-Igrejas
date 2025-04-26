
from django.db import models
from churches.models import Church

class Person(models.Model):
    MARITAL_STATUS = [
        ('single', 'Solteiro(a)'),
        ('married', 'Casado(a)'),
        ('divorced', 'Divorciado(a)'),
        ('widowed', 'Viúvo(a)'),
    ]

    name = models.CharField('Nome', max_length=200)
    birth_date = models.DateField('Data de Nascimento')
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Telefone', max_length=20)
    address = models.CharField('Endereço', max_length=200)
    marital_status = models.CharField('Estado Civil', max_length=20, choices=MARITAL_STATUS)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='Igreja')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['name']

    def __str__(self):
        return self.name
