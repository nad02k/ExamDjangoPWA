# api/urls.py
from django.urls import path
from .views import RegisterServiceWorker, GetAssets

urlpatterns = [
    path('register-sw/', RegisterServiceWorker.as_view()),
    path('assets/', GetAssets.as_view()),
]