from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def get_resumes():
    return Resume.objects.all()


def make_resume(author, description):
    Resume.objects.create(description=description, author=author)
