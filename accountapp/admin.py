from django.contrib import admin

from accountapp.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'phone_number','telecom','aws_access_key')