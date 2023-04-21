from django.contrib import admin

from articleapp.models import Article


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','writer','create_at')