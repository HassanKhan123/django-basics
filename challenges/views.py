from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    months = {
        "january": "New Year",
        "february": "Valentine's Day",
        "march": "St. Patrick's Day",
        "april": "April Fools' Day",
        "may": "May Day",
        "june": "Summer Solstice",
        "july": "Independence Day",
        "august": "Back to School",
        "september": "Labor Day",
        "october": "Halloween",
        "november": "Thanksgiving",
        "december": "Christmas"
    }

    month = month.lower()
    if month in months:
        return HttpResponse(f"<h1>{months[month]}</h1>")

    return HttpResponseNotFound("<h1>Month not found</h1>")
