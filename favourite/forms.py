from django import forms
from . models import PostComment, PostQuote

class PostQuoteForm(forms.ModelForm):
    class Meta:
        model = PostQuote
        fields = ['title', 'quote', 'author']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']