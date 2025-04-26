
from django.urls import path
from . import views

app_name = 'churches'

urlpatterns = [
    path('', views.church_list, name='church_list'),
    path('<int:pk>/', views.church_detail, name='church_detail'),
    path('my-churches/', views.my_churches, name='my_churches'),
]
