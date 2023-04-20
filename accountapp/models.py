from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from miniProject import settings


# Create your models here.

class CustomUser(AbstractUser):
    TELECOM = [
        ('SKT','SKT'),
        ('KT','KT'),
        ('LG','LG')
    ]
    phone_number = models.CharField(max_length=15, null=False)
    telecom = models.CharField(max_length=15, choices=TELECOM, null=False)
    company = models.CharField(max_length=50, null=False, blank=False)
    aws_access_key = models.CharField(max_length=200, null=False, blank=False)
    aws_secret_key = models.CharField(max_length=200, null=False, blank=False)

