from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout


class LogInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    next = '/'
    success_url = '/'
    template_name = 'login/login.html'


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
