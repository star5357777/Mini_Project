from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

