
from django.db import models
from django.contrib.auth import get_user_model

class Church(models.Model):
    name = models.CharField('Nome', max_length=200)
    address = models.CharField('Endereço', max_length=200)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email')
    founded_date = models.DateField('Data de Fundação')
    service_times = models.TextField('Horários de Culto')
    is_headquarters = models.BooleanField('É Sede', default=False)
    parent_church = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(get_user_model(), through='ChurchMember')

    class Meta:
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'

    def __str__(self):
        return self.name

class ChurchMember(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('pastor', 'Pastor'),
        ('leader', 'Líder'),
        ('member', 'Membro'),
    ]
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    role = models.CharField('Cargo', max_length=20, choices=ROLES)
    join_date = models.DateField('Data de Ingresso')

    class Meta:
        verbose_name = 'Membro da Igreja'
        verbose_name_plural = 'Membros da Igreja'
