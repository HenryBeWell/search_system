# encoding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('search_candidates/', views.CandidatesSearchAPIView.as_view(), name='candidates'),
]
