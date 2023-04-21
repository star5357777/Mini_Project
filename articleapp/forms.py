from django import forms
from django.forms import ModelForm
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
