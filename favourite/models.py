from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostQuote(models.Model):
    title = models.CharField(max_length=50)
    quote = models.TextField()
    author = models.CharField(max_length=25)
    date = models.DateField()

class PostComment(models.Model):
    quote = models.ForeignKey(PostQuote, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField()