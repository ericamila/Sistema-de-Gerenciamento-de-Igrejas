
from django.db import models
from churches.models import Church
from people.models import Person

class Account(models.Model):
    TYPES = [
        ('asset', 'Ativo'),
        ('liability', 'Passivo'),
        ('equity', 'Patrimônio'),
        ('revenue', 'Receita'),
        ('expense', 'Despesa'),
    ]
    
    code = models.CharField('Código', max_length=20, unique=True)
    name = models.CharField('Nome', max_length=100)
    type = models.CharField('Tipo', max_length=20, choices=TYPES)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Conta Pai')
    
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Transaction(models.Model):
    TYPES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]
    
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='Igreja')
    description = models.CharField('Descrição', max_length=200)
    amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    type = models.CharField('Tipo', max_length=20, choices=TYPES)
    date = models.DateField('Data')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='Conta', default=1)

    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Pessoa')
    notes = models.TextField('Observações', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['-date']

    def __str__(self):
        return f"{self.description} - {self.amount}"
