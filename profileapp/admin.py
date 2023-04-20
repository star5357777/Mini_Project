from django.contrib import admin

from profileapp.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname','message','user']

