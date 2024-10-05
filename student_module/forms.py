from django import forms
from .models import Student, StudentProfile, StudentPermanentAddress, StudentTempAddress

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'middle_name', 'last_name', 'email', 'phone',
            'city', 'state', 'country', 'dob', 'gender',
            'marital_status', 'lead_source',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),  # Date input for Date of Birth
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            'passport_no', 'passport_issue_date', 'passport_exp_date',
            'passport_issue_country', 'city_of_birth', 'country_of_birth',
            'nationality', 'citizenship', 'citizenship_of_more_country',
            'living_in_any_other_company'
        ]

class StudentPermanentAddressForm(forms.ModelForm):
    class Meta:
        model = StudentPermanentAddress
        fields = [
            'address_1', 'address_2', 'state', 'city',
            'postal_code', 'country'
        ]


class StudentTempAddressForm(forms.ModelForm):
    class Meta:
        model = StudentTempAddress
        fields = ['address_1', 'address_2', 'state', 'city', 'postal_code', 'country']

        widgets = {
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }