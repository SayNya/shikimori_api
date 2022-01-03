from django.urls import path
from .views import *

urlpatterns = [
    path('anime/', AnimeForMainMenuView.as_view()),
    path('anime/<slug:slug>', AnimeDetailsView.as_view()),
]
