from profileApp.views import ProfileCreateView, ProfileUpdateView
from django.urls import path
app_name = 'profileApp'
urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]