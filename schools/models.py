
from django.db import models
from churches.models import Church
from people.models import Person

class Course(models.Model):
    name = models.CharField('Nome', max_length=200)
    description = models.TextField('Descrição')
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='Igreja')
    instructor = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, verbose_name='Instrutor')
    start_date = models.DateField('Data de Início')
    end_date = models.DateField('Data de Término')
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Pessoa')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    enrollment_date = models.DateField('Data de Matrícula', auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        unique_together = ['person', 'course']

    def __str__(self):
        return f"{self.person.name} - {self.course.name}"
