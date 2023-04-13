from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from candidates.models import CandidateSkillScores
from candidates.serializers import CandidateSkillScoresSerializer


class CandidatesListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    CandidatesListViewSet
    list:
        Displays all candidates who meet the criteria
    retrieve:
        Displays the specified candidate information
    """

    queryset = CandidateSkillScores.objects.all()
    serializer_class = CandidateSkillScoresSerializer
