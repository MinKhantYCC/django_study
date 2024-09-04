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
    "december": "Study Django",
}

# index page
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())        # get month names

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>\n'
    print(list_items)
    respond_data = f"<ul>{list_items}</ul>"
    return HttpResponse(respond_data)

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
        challenge_text = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
