from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        add_profile = form.save(commit=False)
        add_profile.user = self.request.user
        add_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)



class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        if request.method == 'GET' and not user == request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})