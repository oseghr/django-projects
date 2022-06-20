from pyexpat import model
from django.conf import settings
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created_date')
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


