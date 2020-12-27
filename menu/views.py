from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu/index.html")

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, "menu/profile.html", context={'user':user})

def upgrade_user(request):
    user = request.user
    user.is_staff = True
    user.save()
    return redirect("menu/profile.html")
