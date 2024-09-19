from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# challenges
monthly_challenges = {
    "january": "Don't Eat Sugar",
    "february": "Walk 1 hour",
    "march": "Exercise 1 hour",
    "april": "Study Django",
    "may": "Don't Eat Sugar",
    "june": "Walk 1 hour",
    "july": "Exercise 1 hour",
    "august": "Study Django",
    "september": "Don't Eat Sugar",
    "october": "Walk 1 hour",
    "november": "Exercise 1 hour",
    # "december": "Study Django",
    "december": None,
}

# index page
def index(request):
    months = list(monthly_challenges.keys())        # get month names

    return render(
        request,
        "challenges/index.html",
        context = {
            "months": months
        }
    )

# route by number
def monthly_challenge_by_number(request, month):
    
    # validate month
    if month > 12:
        return HttpResponseNotFound("Invalid Month")
    
    # redirect
    forward_month = list(monthly_challenges.keys())[month-1]

    # if url route changes unexpectedly, this will change as well
    redirect_path = reverse("month-challenge", args=[forward_month]) # /challenges/january
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    # month is identifier assigned in urls.py
    try:
        challenge_text = monthly_challenges[month]
        challenge_data = render(
            request, 
            "challenges/challenge.html", 
            context={
                "text": challenge_text,
                "month": month
            }
        )
        return HttpResponse(challenge_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
