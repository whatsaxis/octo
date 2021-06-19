from django.shortcuts import resolve_url, redirect
from django.contrib.auth import logout
from django.views.generic import View
from django.views.generic.edit import CreateView

import django.contrib.auth.views as auth

from .forms import CustomUserLoginForm, CustomUserCreationForm

from {{ project_name }}.settings import LOGIN_URL


class LoginView(auth.LoginView):
    template_name = 'registration/login.html'
    form_class = CustomUserLoginForm

    
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return resolve_url('accounts:login')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(LOGIN_URL)