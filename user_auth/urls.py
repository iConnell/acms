from django.urls import path, include
from .views import student_login, student_sign_up, staff_login

app_name='user_auth'
urlpatterns = [
    path('student/login/', student_login, name='student_login'),
    path('register/', student_sign_up, name='student_register'),
    path('staff/login', staff_login, name='staff_login')
]