from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

    login_url = reverse_lazy('accountapp:login')
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return HttpResponseRedirect(reverse_lazy('accountapp:login'))

        return super().dispatch(request, *args, **kwargs)

class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    login_url = reverse_lazy('accountapp:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)

        if request.method == 'GET':
            return HttpResponseRedirect(self.login_url)

        return super().dispatch(request, *args, **kwargs)