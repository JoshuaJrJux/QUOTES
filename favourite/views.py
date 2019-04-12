from django.shortcuts import render, get_object_or_404, redirect
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
    fields = ['comment']

    def form_valid(self, form, **kwargs):
        quote = get_object_or_404(PostQuote, pk=self.kwargs.get('pk'))
        form.instance.quote = quote
        return super().form_valid(form)


class UpdateQuoteUpdateView(UpdateView):
    model = PostQuote
    fields = ['title', 'quote', 'author', 'date']
    template_name = 'favourite/postquote_form.html'

def allcomment(request, quote_id):
    quote = get_object_or_404(PostQuote, pk=quote_id)
    return render(request, 'favourite/postcomment_list.html', {'quote': quote})

def delete_quote (request, quote_id):
    quote = get_object_or_404(PostQuote, pk=quote_id)
    quote.delete()
    return redirect('/')

def delete_comment(request, quote_id, comment_id):
    quote = get_object_or_404(PostQuote, pk=quote_id)
    comment = get_object_or_404(PostComment, pk=comment_id)
    comment.delete()
    return render(request, 'favourite/postcomment_list.html', {'quote': quote})

class UpdateCommentUpdateView(UpdateView):
    model = PostComment
    fields = ['comment']
    template_name = 'favourite/postcomment_form.html'

