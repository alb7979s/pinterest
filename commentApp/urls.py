from commentApp.views import CommentCreateView
from django.urls import path
app_name = 'commentApp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]