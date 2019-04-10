from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import PostQuote, PostComment


# Create your views here.

def index(request):
    quotes = PostQuote.objects.all()
    return render(request, 'favourite/index.html', {'quotes': quotes})

class PostQuoteCreateView(CreateView):
    model = PostQuote
    fields = ['title', 'quote', 'author', 'date']

    def form_valid(self, form):
        return super().form_valid(form)

class PostCommentCreateView(CreateView):
    model = PostComment
    fields = ['quote', 'comment', 'date']

    def form_valid(self, form):
        return super().form_valid(form)

class UpdateQuoteUpdateView(UpdateView):
    model = PostQuote
    fields = ['title', 'quote', 'author', 'date']
    template_name = 'favourite/postquote_form.html'