
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def welcome(request):
    if ChurchMember.objects.filter(user=request.user).exists():
        return redirect('home')
    return render(request, 'welcome.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')
