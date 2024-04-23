from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User, Student


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help text for password fields
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your Last name'
        self.fields['other_names'].widget.attrs['placeholder'] = 'Enter your Other names'
        self.fields['gender'].widget.attrs['placeholder'] = 'Select your gender'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter your Phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'other_names', 'phone', 'gender', )



class StudentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders for form fields
        self.fields['matric_number'].widget.attrs['placeholder'] = 'Enter your Matric number'
        self.fields['department'].widget.attrs['placeholder'] = 'Enter your Department'
        self.fields['faculty'].widget.attrs['placeholder'] = 'Enter your faculty'
        self.fields['residence'].widget.attrs['placeholder'] = 'Enter your hostel'


    class Meta:
        model = Student
        fields = ('matric_number', 'department', 'faculty', 'residence')

