from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.db.utils import IntegrityError


class LogInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    next = '/'
    success_url = '/'
    template_name = 'login/login.html'

'''
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect(self.success_url)
        else:
            return HttpResponse(f"<html><p>Invalid login</p></html>")
'''