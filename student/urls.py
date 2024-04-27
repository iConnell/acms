from django.urls import path
from .views import index, perform_clearance, library_clearance

app_name='student'
urlpatterns = [
    path('', index, name='student_dashboard'),
    path('clearance/', perform_clearance, name='perform_clearance'),
    path('library_clearance/', library_clearance, name='library_clearance'),
]