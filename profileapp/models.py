from django.db import models

from accountapp.models import CustomUser


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=15, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='profile/', null=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'user_profile'
        verbose_name_plural = 'user_profile_group'


