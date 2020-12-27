from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy, get_vacancies, make_entry
from django.http import HttpResponse, HttpResponseForbidden


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = get_vacancies()
        return render(request, f"vacancy/index.html", context={"vacancies": vacancies})


class NewVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, f"vacancy/new.html")


    def post(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_authenticated:
            return HttpResponseForbidden()
        description = request.POST.get("description")
        author = request.user
        make_entry(author, description)
        return redirect("/")
