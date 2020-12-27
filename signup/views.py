from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = UserCreationForm
    model = User
    success_url = "/login"
    next = "/login"
    template_name = 'signup/signup.html'

    '''
    def post(self, request, *args, **kwargs):
        try :
            User.objects.create_user(
                username=request.POST.get('username'), password=request.POST.get('password'))
        except IntegrityError:
            return HttpResponse("<html><p>Username Taken!</p></html>")
    '''