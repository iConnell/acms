from django.urls import path, include
from .views import forgot_password, student_login, student_sign_up, staff_login, forgot_password, reset_password

app_name='user_auth'
urlpatterns = [
    path('student/login/', student_login, name='student_login'),
    path('register/', student_sign_up, name='student_register'),
    path('staff/login', staff_login, name='staff_login'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password, name='reset-password')
]