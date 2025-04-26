
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Transaction
from churches.models import Church
from django.db.models.functions import TruncMonth
from django.utils import timezone

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'finances/transaction_list.html', {'transactions': transactions})

@login_required
def transaction_create(request):
    if request.method == 'POST':
        transaction = Transaction.objects.create(
            church_id=request.POST['church'],
            description=request.POST['description'],
            amount=request.POST['amount'],
            type=request.POST['type'],
            date=request.POST['date'],
            category=request.POST['category'],
            notes=request.POST.get('notes', '')
        )
        messages.success(request, 'Transação registrada com sucesso!')
        return redirect('finances:transaction_list')
    churches = Church.objects.all()
    return render(request, 'finances/transaction_form.html', {'churches': churches})

@login_required
def financial_dashboard(request):
    # Dados para o dashboard
    current_month = timezone.now().month
    current_year = timezone.now().year
    
    monthly_income = Transaction.objects.filter(
        type='income',
        date__month=current_month,
        date__year=current_year
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    monthly_expense = Transaction.objects.filter(
        type='expense',
        date__month=current_month,
        date__year=current_year
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    balance = monthly_income - monthly_expense
    
    context = {
        'monthly_income': monthly_income,
        'monthly_expense': monthly_expense,
        'balance': balance,
    }
    return render(request, 'finances/dashboard.html', context)
