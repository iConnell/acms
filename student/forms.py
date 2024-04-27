from clearance.models import Clearance, ClearanceDocument, ClearanceItem
from django import forms


class ClearanceForm(forms.ModelForm):
    class Meta:
        model = ClearanceItem
        fields = [
            
        ]


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result



class ClearanceDocumentsForm(forms.ModelForm):
    document = MultipleFileField()
    class Meta:
        model = ClearanceDocument
        fields = ['document']

        
class ClearanceDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a custom class to the file input widget
        self.fields['document'].widget.attrs.update({'class': 'custom-file-input'})

    class Meta:
        model = ClearanceDocument
        fields = ['document']
        labels = {'document': ''}

        widgets = {
            'document': forms.FileInput(attrs={'disabled': False}),
        }