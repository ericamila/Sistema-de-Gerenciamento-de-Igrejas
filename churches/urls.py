
from django.urls import path
from . import views

app_name = 'churches'

urlpatterns = [
    path('', views.church_list, name='church_list'),
    path('<int:pk>/', views.church_detail, name='church_detail'),
    path('my-churches/', views.my_churches, name='my_churches'),
    path('create/', views.church_create, name='church_create'),
    path('<int:pk>/update/', views.church_update, name='church_update'),
    path('<int:pk>/delete/', views.church_delete, name='church_delete'),
]
