
from django.urls import path
from . import views

app_name = 'finances'

urlpatterns = [
    path('', views.financial_dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/create/', views.transaction_create, name='transaction_create'),
]
