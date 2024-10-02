from django.db import models
from student_module.models import *
from university_module.models import *
# Create your models here.


class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)


class ApplicationStatus(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='application_statuses')
    universities = models.ForeignKey('university_module.UniversityList', on_delete=models.CASCADE, related_name='applications', default=1)
    status = models.CharField(max_length=50, choices=(('in_progress', 'In Progress'), ('submitted', 'Submitted'),
                                                      ('accepted', 'Accepted')))
    updated_at = models.DateTimeField(auto_now=True)
