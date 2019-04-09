from django.contrib import admin
from .models import PostQuote, PostComment

# Register your models here.

admin.site.register(PostQuote)
admin.site.register(PostComment)