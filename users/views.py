from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class Register(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/register.html'

class Login(LoginView):
  pass

class Logout(LogoutView):
  pass



  