from django.db import models
from .models import *
from student_module.models import StudentProfile


class CommunicationLog(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='communication_logs')
    method = models.CharField(max_length=50, choices=(('email', 'Email'), ('call', 'Call'), ('meeting', 'Meeting')))
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()