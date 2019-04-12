from django.urls import path
from . import views

app_name = 'favourite'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_quote', views.PostQuoteCreateView.as_view(), name='create_quote'),
    path('<int:pk>/comment', views.PostCommentCreateView.as_view(), name='comment'),
    path('<int:pk>/update-quote', views.UpdateQuoteUpdateView.as_view(), name='update-quote'),
    path('(?p<quote_id>[0-9]+)/', views.allcomment, name='all-comment'),
    path('(?p<quote_id>[0-9]+)/delete-quote', views.delete_quote, name='delete-quote'),
    path('?p<quote_id>[0-9]+)/delete-comment/?p<comment_id>[0-9]+)/', views.delete_comment, name='delete-comment'),
    path('<int:pk>/update-comment', views.UpdateCommentUpdateView.as_view(), name='update-comment')

]