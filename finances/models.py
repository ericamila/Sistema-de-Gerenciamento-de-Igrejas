
from django.db import models
from churches.models import Church

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
    category = models.CharField('Categoria', max_length=100)
    notes = models.TextField('Observações', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['-date']

    def __str__(self):
        return f"{self.description} - {self.amount}"
