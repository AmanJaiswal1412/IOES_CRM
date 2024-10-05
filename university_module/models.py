from django.db import models
from setting_module.models import *


# Create your models here.
class UniversityList(models.Model):
    university_name = models.CharField(max_length=255)
    campuslist = models.ForeignKey(UniversityCampus, null=True, on_delete=models.SET_NULL, related_name='University_list')
    university_logo = models.ImageField(null=True, upload_to='university_logo/')
    qs_ranking = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.university_name


class CollageList(models.Model):
    university_list = models.ForeignKey(UniversityList, null=True, on_delete=models.SET_NULL, related_name='collage_list')
    collage_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.collage_name


class ProgrammeList(models.Model):
    universitylist = models.ForeignKey(UniversityList, null=True, on_delete=models.SET_NULL, related_name='programme_list')
    collagelist = models.ForeignKey(CollageList, null=True, on_delete=models.SET_NULL, related_name='programme_list')
    programme_name = models.CharField(max_length=20, null=False, default='Bachelor')
    programme_duration = models.CharField(max_length=20, null=False, default='2024-2025')
    is_active = models.BooleanField(default=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.programme_name
