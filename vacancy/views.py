from django.shortcuts import render
from django.views import View
from .models import Vacancy, get_vacancies, make_entry


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        make_entry()
        vacancies = get_vacancies()
        return render(request, f"vacancy/index.html", context={"vacancies": vacancies})