from django.urls import path
from .views import *

urlpatterns = [
    path('anime/', AnimeView.as_view())
]
