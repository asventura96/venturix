# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = PasswordResetForm

class UserListView(ListView):
    model = User
    template_name = 'accounts/user_list.html'

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'groups']
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('user_list')

def app_list_view(request):
    installed_apps = apps.get_app_configs()
    return render(request, 'accounts/app_list.html', {'installed_apps': installed_apps})
