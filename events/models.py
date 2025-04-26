
from django.db import models
from churches.models import Church

class Event(models.Model):
    TYPES = [
        ('service', 'Culto'),
        ('meeting', 'Reunião'),
        ('class', 'Aula'),
        ('other', 'Outro'),
    ]
    
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='Igreja')
    name = models.CharField('Nome', max_length=200)
    type = models.CharField('Tipo', max_length=20, choices=TYPES)
    date = models.DateTimeField('Data e Hora')
    description = models.TextField('Descrição')
    is_public = models.BooleanField('Público', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['date']

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%d/%m/%Y %H:%M')}"
