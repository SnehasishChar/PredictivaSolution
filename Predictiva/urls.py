from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("industry_solutions/", views.industry_solutions, name="industry_solutions"),
    path(
        "optimization_solutions/",
        views.optimization_solutions,
        name="optimization_solutions",
    ),
    path(
        "team/",
        views.team,
        name="team",
    ),
]
