
from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('<int:course_pk>/enroll/', views.student_enroll, name='student_enroll'),
]
