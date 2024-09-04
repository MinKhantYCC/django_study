from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<month>", views.monthly_challenge),
]