from django.views.generic import TemplateView
from django.urls import path
urlpatterns =[
    path('list/', TemplateView.as_view(template_name='articleApp/list.html'), name='list')
]