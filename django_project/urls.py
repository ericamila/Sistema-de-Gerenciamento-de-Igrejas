
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', login_required(home), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('churches/', include('churches.urls')),
    path('people/', include('people.urls')),
    path('finances/', include('finances.urls')),
    path('events/', include('events.urls')),
    path('schools/', include('schools.urls')),
    path('reports/', include('reports.urls')),
]
