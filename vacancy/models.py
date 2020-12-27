from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def get_vacancies():
    return Vacancy.objects.all()


def make_entry(author, description):
    Vacancy.objects.create(author=author, description=description)
