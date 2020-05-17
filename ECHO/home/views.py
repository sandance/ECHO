from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

class HomepageView(TemplateView):
    template_name = 'index.html'

class LoginpageView(TemplateView):
    template_name = 'contact.html'

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('login/')