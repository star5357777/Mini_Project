from django.db import models

# Create your models here.
class Post(models.Model):
    Postname = models.CharField(max_length=50, verbose_name="게시글 이름")
    context = models.TextField()
    #게시글 제목을 Post object가 대신 한다함
    def __str__(self):
        return self.postname