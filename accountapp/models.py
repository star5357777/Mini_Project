from django.db import models

# Create your models here.
class account(models.Model):
    Username = models.CharField(max_length=64, verbose_name="사용자 계정")

    password = models.CharField(max_length=64, verbose_name="비밀번호")
    # 아래거는 utc 시간으로만 기록이 되네
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    class Meta:
        db_table = 'account_user'