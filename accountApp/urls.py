from django.contrib import admin
from django.urls import path, include

from accountApp.views import hello_world

app_name = 'accountApp'
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
