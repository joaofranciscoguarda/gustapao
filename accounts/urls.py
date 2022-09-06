from accounts.views import AcccountDetailView, AccountView
from django.urls import path

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<id>/", AcccountDetailView.as_view())
]