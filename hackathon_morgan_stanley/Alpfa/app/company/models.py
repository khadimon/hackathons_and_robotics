from django.db import models
from users.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    estd = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)  # Company website
    description = models.TextField(null=True, blank=True)  # Brief description of the company
    industry = models.CharField(max_length=100, null=True, blank=True)  # Industry sector
    number_of_employees = models.PositiveIntegerField(null=True, blank=True)  # Number of employees

    def __str__(self):
        return self.name
