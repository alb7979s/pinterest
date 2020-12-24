from django.views.generic import TemplateView
from django.urls import path

from articleApp.views import ArticleUpdateView, ArticleCreateView, ArticleDetailView, ArticleDeleteView

app_name = 'articleApp'
urlpatterns =[
    path('list/', TemplateView.as_view(template_name='articleApp/list.html'), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]