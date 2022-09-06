from accounts.views import AcccountDetailView, AccountView
from rest_framework.authtoken import views
from django.urls import path

urlpatterns = [
    path("accounts/login/", views.obtain_auth_token),
    path("accounts/", AccountView.as_view()),
    path("accounts/<pk>/", AcccountDetailView.as_view()),
]