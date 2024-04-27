from django.db import models
from user_auth.models import Student, Staff
from utils import CLEARANCES, CLEARANCE_STATUS_CHOICES

# Create your models here.

class Clearance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ClearanceItem(models.Model):
    name = models.CharField(max_length=50, choices=CLEARANCES)
    clearance = models.ForeignKey(Clearance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CLEARANCE_STATUS_CHOICES, default='pending')
    feedback = models.CharField(max_length=1000, blank=True, null=True)
    cleared_by = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                'name', 'clearance',
                name='Clearance item unique for each clearance',
            ),
        ]

class ClearanceDocument(models.Model):
    clearance_item = models.ForeignKey(ClearanceItem, on_delete=models.CASCADE)
    document = models.FileField(upload_to='student_clearance_fiels')