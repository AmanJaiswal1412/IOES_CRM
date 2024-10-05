from django.db import models
from university_module.models import *
from agent_module.models import *
from setting_module.models import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


GENDER_CHOICE = (
    ('Male', 'male'),
    ('Female', 'female'),
)


MARITAL_STATUS = (
    ('Married', 'married'),
    ('Unmarried', 'unmarried'),
)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default='Middle Name')
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20, null=False, default='Delhi')
    state = models.CharField(max_length=20, default='Maharashtra')
    country = models.CharField(max_length=20, null=False, default='India')
    dob = models.DateField(default='2006-09-25')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='male')
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS, default='unmarried')
    lead_source = models.ForeignKey(LeadSource, null=True, on_delete=models.SET_NULL, related_name='students')
    # created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class StudentProfile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_profiles')
    passport_no = models.CharField(max_length=20, null=False, default='no_passport_no')
    passport_issue_date = models.DateField()
    passport_exp_date = models.DateField()
    passport_issue_country = models.CharField(max_length=20, default='India')
    city_of_birth = models.CharField(max_length=20, null=False, default='Delhi')
    country_of_birth = models.CharField(max_length=20, null=False, default='India')
    nationality = models.CharField(max_length=20, default='Indian')
    citizenship = models.CharField(max_length=20, default='India')
    citizenship_of_more_country = models.BooleanField(default=False)
    living_in_any_other_company = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student


class StudentPermanentAddress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student_Permanent_Addresses')
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20, null=False, default='Delhi')
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=False, default='India')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"


class StudentTempAddress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student_Temp_Addresses')
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20, null=False, default='Delhi')
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=False, default='India')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"


class StudentBackground(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student_backgrounds')
    has_applied_immigration_for_any_country = models.BooleanField(default=False)
    has_suffering_from_any_major_disease = models.BooleanField(default=False)
    visa_has_refused_once = models.BooleanField(default=False)
    has_convicted_in_a_criminal_case = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"


class ImportantContact(models.Model):
    # Phone No Validation
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    # Phone No Validation

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='important_contacts')
    name = models.CharField(max_length=20, null=False, default='Name')
    phone_no = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)
    email = models.EmailField(default=None, null=True, blank=True)
    relation_with_the_applicant = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"