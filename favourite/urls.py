from django.urls import path
from . import views

app_name = 'favourite'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_quote', views.PostQuoteCreateView.as_view(), name='create_quote'),
    path('comment', views.PostCommentCreateView.as_view(), name='comment'),
    path('<int:pk>/update-quote', views.UpdateQuoteUpdateView.as_view(), name='update-quote'),

]