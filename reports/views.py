
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from people.models import Person
from finances.models import Transaction
from events.models import Event
from datetime import datetime, timedelta

@login_required
def report_list(request):
    return render(request, 'reports/report_list.html')

@login_required
def members_report(request):
    members = Person.objects.all()
    context = {
        'members': members,
        'total_members': members.count(),
        'active_members': members.filter(is_active=True).count(),
    }
    return render(request, 'reports/members_report.html', context)

@login_required
def finances_report(request):
    year = datetime.now().year
    months = range(1, 13)
    
    monthly_data = []
    for month in months:
        income = Transaction.objects.filter(
            type='income',
            date__year=year,
            date__month=month
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        expense = Transaction.objects.filter(
            type='expense',
            date__year=year,
            date__month=month
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        monthly_data.append({
            'month': datetime(year, month, 1).strftime('%B'),
            'income': income,
            'expense': expense,
            'balance': income - expense
        })
    
    context = {
        'year': year,
        'monthly_data': monthly_data
    }
    return render(request, 'reports/finances_report.html', context)

@login_required
def events_report(request):
    start_date = datetime.now() - timedelta(days=30)
    events = Event.objects.filter(date__gte=start_date)
    context = {
        'events': events,
        'total_events': events.count(),
    }
    return render(request, 'reports/events_report.html', context)
