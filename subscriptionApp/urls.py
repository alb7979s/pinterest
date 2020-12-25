from django.urls import path

from subscriptionApp.views import SubscriptionView

app_name = 'subscriptionApp'

urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
]