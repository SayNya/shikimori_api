from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.AnimeForMainMenuView.as_view(), name='anime-list'),
    path('anime/<slug:slug>', views.AnimeDetailsView.as_view(), name='anime-detail'),
]
