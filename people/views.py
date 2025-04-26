
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Person

@login_required
def person_list(request):
    people = Person.objects.all()
    return render(request, 'people/person_list.html', {'people': people})

@login_required
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'people/person_detail.html', {'person': person})

@login_required
def person_create(request):
    if request.method == 'POST':
        person = Person.objects.create(
            name=request.POST['name'],
            birth_date=request.POST['birth_date'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            marital_status=request.POST['marital_status'],
            church_id=request.POST['church'],
        )
        messages.success(request, 'Pessoa cadastrada com sucesso!')
        return redirect('people:person_detail', pk=person.pk)
    return render(request, 'people/person_form.html')

@login_required
def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.name = request.POST['name']
        person.birth_date = request.POST['birth_date']
        person.email = request.POST['email']
        person.phone = request.POST['phone']
        person.address = request.POST['address']
        person.marital_status = request.POST['marital_status']
        person.church_id = request.POST['church']
        person.save()
        messages.success(request, 'Pessoa atualizada com sucesso!')
        return redirect('people:person_detail', pk=person.pk)
    return render(request, 'people/person_form.html', {'person': person})

@login_required
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')
        return redirect('people:person_list')
    return render(request, 'people/person_confirm_delete.html', {'person': person})
