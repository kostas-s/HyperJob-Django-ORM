from django.shortcuts import render
from django.views import View
from .models import get_resumes


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = get_resumes()
        return render(request, f"resume/index.html", context={"resumes": resumes})