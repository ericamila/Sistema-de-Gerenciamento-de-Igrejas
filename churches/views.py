
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Church, ChurchMember
from django.utils import timezone

@login_required
def church_list(request):
    churches = Church.objects.all()
    return render(request, 'churches/church_list.html', {'churches': churches})

@login_required
def church_detail(request, pk):
    church = get_object_or_404(Church, pk=pk)
    return render(request, 'churches/church_detail.html', {'church': church})

@login_required
def my_churches(request):
    member_churches = ChurchMember.objects.filter(user=request.user)
    return render(request, 'churches/my_churches.html', {'member_churches': member_churches})

@login_required
def church_create(request):
    if request.method == 'POST':
        church = Church.objects.create(
            name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            founded_date=request.POST['founded_date'],
            service_times=request.POST['service_times'],
            is_headquarters=request.POST.get('is_headquarters', False),
        )
        ChurchMember.objects.create(
            user=request.user,
            church=church,
            role='admin',
            join_date=timezone.now().date()
        )
        messages.success(request, 'Igreja criada com sucesso!')
        return redirect('churches:church_detail', pk=church.pk)
    return render(request, 'churches/church_form.html')

@login_required
def church_update(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        church.name = request.POST['name']
        church.address = request.POST['address']
        church.phone = request.POST['phone']
        church.email = request.POST['email']
        church.founded_date = request.POST['founded_date']
        church.service_times = request.POST['service_times']
        church.is_headquarters = request.POST.get('is_headquarters', False)
        church.save()
        messages.success(request, 'Igreja atualizada com sucesso!')
        return redirect('churches:church_detail', pk=church.pk)
    return render(request, 'churches/church_form.html', {'church': church})

@login_required
def church_delete(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        church.delete()
        messages.success(request, 'Igreja excluída com sucesso!')
        return redirect('churches:church_list')
    return render(request, 'churches/church_confirm_delete.html', {'church': church})
