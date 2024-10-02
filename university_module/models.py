from django.db import models
from setting_module.models import *


# Create your models here.
class UniversityList(models.Model):
    countrylist = models.ForeignKey(CountryList, on_delete=models.CASCADE, related_name='University_list')
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)


class ProgrammeList(models.Model):
    universitylist = models.ForeignKey(UniversityList, on_delete=models.CASCADE, related_name='programme_list')
    programme_name = models.CharField(max_length=20, null=False, default='Bachelor')
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)