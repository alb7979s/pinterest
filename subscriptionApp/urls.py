from django.urls import path

from subscriptionApp.views import SubscriptionView, SubscriptionListView

app_name = 'subscriptionApp'

urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]