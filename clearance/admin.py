from django.contrib import admin
from .models import Clearance, ClearanceItem, ClearanceDocument

# Register your models here.

admin.site.register(Clearance)
admin.site.register(ClearanceItem)
admin.site.register(ClearanceDocument)