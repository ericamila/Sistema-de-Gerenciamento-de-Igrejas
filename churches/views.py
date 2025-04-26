
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Church, ChurchMember

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
