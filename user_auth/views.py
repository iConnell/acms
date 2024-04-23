from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import Student, Staff
from .forms import UserRegistrationForm, StudentCreationForm

User = get_user_model()
# Create your views here.

def index(request):
    """Render the landing page."""
    return render(request, 'index.html')

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
                return redirect('dashboard')
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
