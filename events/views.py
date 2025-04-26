
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from churches.models import Church
from django.contrib import messages

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    churches = Church.objects.all()
    if request.method == 'POST':
        event = Event.objects.create(
            church_id=request.POST['church'],
            name=request.POST['name'],
            type=request.POST['type'],
            date=request.POST['date'],
            description=request.POST['description'],
            is_public=request.POST.get('is_public', True),
        )
        messages.success(request, 'Evento criado com sucesso!')
        return redirect('events:event_detail', pk=event.pk)
    return render(request, 'events/event_form.html')

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.church_id = request.POST['church']
        event.name = request.POST['name']
        event.type = request.POST['type']
        event.date = request.POST['date']
        event.description = request.POST['description']
        event.is_public = request.POST.get('is_public', True)
        event.save()
        messages.success(request, 'Evento atualizado com sucesso!')
        return redirect('events:event_detail', pk=event.pk)
    return render(request, 'events/event_form.html', {'event': event})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('events:event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
