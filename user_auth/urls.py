from django.urls import path, include
from .views import forgot_password, student_login, student_sign_up, staff_login, forgot_password, reset_password, logout_view
from django.contrib.auth.views import LogoutView


app_name='user_auth'
urlpatterns = [
    path('student/login/', student_login, name='student_login'),
    path('logout/', logout_view, name='user_logout'),
    path('register/', student_sign_up, name='student_register'),
    path('staff/login', staff_login, name='staff_login'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password, name='reset-password')
]