from os import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clearance.models import Clearance, ClearanceItem, ClearanceDocument
from user_auth.models import Student
from .forms import ClearanceDocumentForm, ClearanceDocumentsForm
from utils import CLEARANCES
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

@login_required()
def index(request):
    return render(request, 'student/index.html')

def perform_clearance(request):
    pass

@login_required()
def library_clearance(request):
    # check if student has done this clearance before
    student = Student.objects.get(user=request.user)
    form = ClearanceDocumentForm()
    try:
        clearance = Clearance.objects.get(student=student)
        clearance_item = ClearanceItem.objects.get(clearance=clearance, name=CLEARANCES['library'].lower())

        form.disabled = True
        form.fields['document'].widget.attrs['disabled'] = True
        context = {
            'form': form,
            'heading': 'Library Clearance',
            'message': 'Upload a clear photo of your library card or letter of identification from your HOD',
            'error_message': "Library card already uploaded"
        }

        return render(request, "student/clearance_form.html", context)
        
    except Exception as e: 
        pass
        

    if request.method == 'POST':
        form = ClearanceDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # get clearance
            clearance, created = Clearance.objects.get_or_create(student=student)

            # create clearance item
            clearance_item = ClearanceItem.objects.create(
                clearance=clearance,
                name=CLEARANCES['library'].lower(),
            )

            clearance_document = form.save(commit=False)
            clearance_document.clearance_item = clearance_item
            clearance_document.save()

            return HttpResponseRedirect(reverse('student:student_dashboard'))
    else:
        context = {
            'form': form,
            'heading': 'Library Clearance',
            'message': 'Upload a clear photo of your library card or letter of identification from your HOD',
            'url': "{% url 'student:library_clearance' %}"
        }
        return render(request, 'student/clearance_form.html', context)