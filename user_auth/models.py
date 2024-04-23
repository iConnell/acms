from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


from .managers import UserManager


gender_choices = (
    ("F", "Female"),
    ("M", "Male")
)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    other_names = models.CharField(_('other names'), max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=gender_choices, null=True)
    phone = models.CharField(_('phone number'), max_length=15, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=12, blank=False, null=False, primary_key=True)
    department = models.CharField(max_length=50, blank=False, null=False)
    faculty = models.CharField(max_length=50, blank=False, null=False)
    residence = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.user.get_full_name()
    
    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.user.get_full_name()