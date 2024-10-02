from django.contrib.auth.models import User
from django.db import models


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    region = models.CharField(max_length=100)
    contact_info = models.TextField()
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
