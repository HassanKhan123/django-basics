from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
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
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>Invalid month number</h1>")
    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]

        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })

    except:
        raise Http404()
