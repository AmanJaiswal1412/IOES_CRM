from django import forms
from .models import Academics, Document, ApplicationStatus


class AcademicsForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = ['std_10', 'std_12', 'bachelors']

        widgets = {
            'std_10': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
            'std_12': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
            'bachelors': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_type', 'file']

        widgets = {
            'document_type': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        fields = ['student', 'universities', 'status']

        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'universities': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }