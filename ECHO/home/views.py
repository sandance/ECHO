from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

class HomepageView(TemplateView):
    template_name = 'index.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'