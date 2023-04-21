from django.db import models

from accountapp.models import CustomUser


# Create your models here.
# writer title image content created_at

class Article(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='article')
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)