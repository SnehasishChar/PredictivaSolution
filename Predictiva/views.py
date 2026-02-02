from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def industry_solutions(request):
    context = {}
    return render(request, "industry_solutions.html", context)


def optimization_solutions(request):
    context = {}
    return render(request, "optimization_solutions.html", context)


def team(request):
    context = {}
    return render(request, "team.html", context)
