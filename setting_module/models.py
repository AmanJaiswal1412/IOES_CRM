from django.db import models


# Create your models here.
class LeadSource(models.Model):
    source_name = models.CharField(max_length=20, null=False, default='IOES')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_name


class DocumentList(models.Model):
    document_name = models.CharField(max_length=20, null=False, default='IOES')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_name


class CountryList(models.Model):
    country_list = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_list


class CityList(models.Model):
    country_list = models.ForeignKey(CountryList, on_delete=models.SET_NULL, null=True)
    city_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_list


class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=100)
    campus_city = models.ForeignKey(CityList, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campus_name


class IntakeList(models.Model):
    intake_name = models.CharField(max_length=20, null=True)
    intake_year = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
