from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from profileApp.models import Profile
from profileApp.forms import ProfileCreationForm
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'profileApp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'profileApp/update.html'