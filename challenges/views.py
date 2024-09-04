from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse("Welcome, Challenger!")

def monthly_challenge(request, month):
    # month is identifier assigned in urls.py
    challenge_text = None
    if month == "january":
        challenge_text = "Don't Eat Sugar"
    elif month == "february":
        challenge_text = "Walk 1 hour"
    elif month == "march":
        challenge_text = "Exercise 1 hour"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
