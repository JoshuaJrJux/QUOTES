from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


# Create your models here.

class PostQuote(models.Model):
    title = models.CharField(max_length=50)
    quote = models.TextField()
    author = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('favourite:index')


class PostComment(models.Model):
    quote = models.ForeignKey(PostQuote, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('favourite:all-comment',  args=[str(self.pk)])