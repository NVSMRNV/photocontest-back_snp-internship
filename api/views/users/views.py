from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from api.forms.forms import LoginUserForm, RegisterUserForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/index.html')
    
    
class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    redirect_authenticated_user = ''


class LogoutUserView(LogoutView):
    pass