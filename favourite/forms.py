from django import forms
from . models import PostComment, PostQuote

class PostQuoteForm(forms.ModelForm):
    class Meta:
        model = PostQuote
        fields = ['title', 'quote', 'author', 'date']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['quote', 'comment', 'date']