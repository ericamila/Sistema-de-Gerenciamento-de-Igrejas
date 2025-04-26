
from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('members/', views.members_report, name='members_report'),
    path('finances/', views.finances_report, name='finances_report'),
    path('events/', views.events_report, name='events_report'),
]
