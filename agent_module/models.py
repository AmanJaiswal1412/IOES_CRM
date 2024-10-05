from django.contrib.auth.models import User
from django.db import models


class BussinessInfo(models.Model):
    business_name = models.CharField(max_length=100)
    business_phone = models.CharField(max_length=12)
    business_email = models.EmailField(unique=True)
    business_website = models.URLField()
    business_info = models.TextField(max_length=500)
    business_location = models.CharField(max_length=100)
    business_address = models.TextField(max_length=200)
    gstin = models.CharField(max_length=12)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    business_info = models.ForeignKey(BussinessInfo, on_delete=models.SET_NULL, null=True, related_name='agents')
    agent_email = models.EmailField(unique=True, null=True)
    agent_phone = models.CharField(max_length=12, null=True)
    location = models.CharField(max_length=100)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
