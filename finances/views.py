
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from datetime import datetime
from .models import Transaction, Account
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
    from django.db.models import Count
    from people.models import Person
    from churches.models import Church
    from events.models import Event

    current_month = timezone.now().month
    current_year = timezone.now().year
    
    # Estatísticas gerais
    total_members = Person.objects.count()
    total_churches = Church.objects.count()
    total_events = Event.objects.filter(
        date__month=current_month,
        date__year=current_year
    ).count()

    # Dados financeiros do mês
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

    # Dados para os gráficos
    last_6_months = []
    for i in range(5, -1, -1):
        month = timezone.now() - timezone.timedelta(days=i*30)
        members = Person.objects.filter(created_at__lte=month).count()
        income = Transaction.objects.filter(
            type='income',
            date__month=month.month,
            date__year=month.year
        ).aggregate(total=Sum('amount'))['total'] or 0
        expense = Transaction.objects.filter(
            type='expense',
            date__month=month.month,
            date__year=month.year
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        last_6_months.append({
            'month': month.strftime('%b'),
            'members': members,
            'income': income,
            'expense': expense
        })
    
    context = {
        'total_members': total_members,
        'total_churches': total_churches,
        'total_events': total_events,
        'monthly_income': monthly_income,
        'monthly_expense': monthly_expense,
        'last_6_months': last_6_months,
    }
    return render(request, 'finances/dashboard.html', context)

@login_required
def balance_sheet(request):
    assets = Account.objects.filter(type='asset')
    liabilities = Account.objects.filter(type='liability')
    equity = Account.objects.filter(type='equity')
    
    context = {
        'assets': assets,
        'liabilities': liabilities,
        'equity': equity,
        'date': datetime.now()
    }
    return render(request, 'finances/balance_sheet.html', context)

@login_required
def income_statement(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    revenues = Account.objects.filter(type='revenue')
    expenses = Account.objects.filter(type='expense')
    
    context = {
        'revenues': revenues,
        'expenses': expenses,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'finances/income_statement.html', context)
