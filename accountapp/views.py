from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, TemplateView

from accountapp.forms import CustomUserCreationForm
from accountapp.models import CustomUser


# Create your views here.


@method_decorator(login_required,'get')

class HomeView(TemplateView):
    template_name = 'main.html'
class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/create.html'

class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
