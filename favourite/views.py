from django.shortcuts import render
from .models import PostQuote, PostComment

# Create your views here.

def index(request):
    quotes = PostQuote.objects.all()
    return render(request, 'favourite/index.html', {'quotes': quotes})

