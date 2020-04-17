from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path(r"", views.MatchListView.as_view()),
    path(r"<int:pk>/", views.MatchView.as_view()),
]