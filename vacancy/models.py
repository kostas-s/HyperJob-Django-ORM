from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def get_vacancies():
    return Vacancy.objects.all()


def make_entry():
    u = User(username="ksmonos")
    u.save()
    v = Vacancy(description="Typical Job Description", author=u)
    v.save()
