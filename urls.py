from django.urls import path
from .views import student_list, student_detail, student_login

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:id>/', student_detail, name='student-detail'),
    path('students/login/', student_login, name='student-login'),
]
