from django.shortcuts import render, redirect
from django.views import View
from .models import get_resumes, make_resume
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = get_resumes()
        return render(request, f"resume/index.html", context={"resumes": resumes})


class NewResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, f"resume/new.html")

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        description = request.POST.get("description")
        author = request.user
        make_resume(author, description)
        return redirect("/")
