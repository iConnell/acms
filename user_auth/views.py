from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model, logout
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import Student, Staff
from .forms import UserRegistrationForm, StudentCreationForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from utils.tokens import generate_token, decode_token

User = get_user_model()
# Create your views here.

def index(request):
    """Render the landing page."""
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def student_login(request):
    if request.method == 'POST':
        matric_number = request.POST.get('matric_number')
        password = request.POST.get('password')

        try:
            student = Student.objects.select_related('user').get(matric_number=matric_number)
            user = authenticate(request, email=student.user.email, password=password)
        
            if user:
                login(request, user)
                # Redirect to dashboard or desired page
                return redirect('student:student_dashboard')
            else:
                # Invalid credentials, show an error message
                context = {'error_message': 'Invalid matric number or password'}
                return render(request, 'user_auth/student_login.html', context)
        except Student.DoesNotExist:
            context = {'error_message': 'Invalid matric number or password'}
            return render(request, 'user_auth/student_login.html', context)
    else:
        return render(request, 'user_auth/student_login.html')
    
def student_sign_up(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentCreationForm(request.POST)
        
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            # Redirect to success page or desired URL
            # Log in the user
            # login(request, user)
            # Redirect to dashboard or desired page
            return redirect('dashboard')  # Change 'dashboard' to your actual URL name
        else: 

            return render(request, 'user_auth/register.html',{
                'user_form': user_form,
                'student_form': student_form,
            })
    else:
        user_form = UserRegistrationForm()
        student_form = StudentCreationForm()

        return render(request, 'user_auth/register.html', {'user_form': user_form, 'student_form': student_form})
    
def staff_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            
            user = authenticate(request, email=email, password=password)
        
            if user:
                try:
                    staff = Staff.objects.get(user=user)
                except Staff.DoesNotExist:
                    # Invalid credentials, show an error message
                    context = {'error_message': 'Invalid email or password'}
                    return render(request, 'user_auth/staff_login.html', context)
                login(request, user)
                # Redirect to dashboard or desired page
                return redirect('dashboard')
            else:
                # Invalid credentials, show an error message
                context = {'error_message': 'Invalid email or password'}
                return render(request, 'user_auth/staff_login.html', context)
        except Student.DoesNotExist:
            context = {'error_message': 'Invalid email or password'}
            return render(request, 'user_auth/staff_login.html', context)
    else:
        return render(request, 'user_auth/staff_login.html')

def forgot_password(request):
    email = request.POST.get('email')
    if request.method == 'POST':

        try:
            user = User.objects.get(email=email)

            token = generate_token(email)
            print(token)

            # send password reset email
            user.send_email("Forgot Password", f"Seems you forgot your password click this link to reset your password {token}")
            return render(request, 'user_auth/password_reset_link_sent.html')
        except:
            return render(request, 'user_auth/password_reset_link_sent.html')

    return render(request, 'user_auth/forgot_password.html')

def reset_password(request, token):
        email = decode_token(token)
        if email:
            user = User.objects.get(email=email)
            if request.method == 'POST':
                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    
                    return render(request, 'user_auth/password_reset_done.html')
                else: 
                    return render(request, 'user_auth/reset_password.html', {'form': form, 'error_message': form.errors})
            else:
                form = SetPasswordForm(user)
            return render(request, 'user_auth/reset_password.html', {'form': form})
        else:
            # Invalid token
            return render(request, 'user_auth/invalid_token.html')








