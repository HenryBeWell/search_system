from django.core.paginator import Paginator
from django.db.models import QuerySet

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from candidates.models import CandidateSkillScores
from candidates.pagenate import CustomPagination
from candidates.permission import CandidatesSearchPermission
from candidates.serializers import CandidateSkillSearchSerializer


class CandidatesSearchAPIView(generics.CreateAPIView):
    """
    CandidatesSearchAPIView
    post:
        Displays all candidates who meet the criteria
    """
    queryset = CandidateSkillScores.objects.all()
    serializer_class = CandidateSkillSearchSerializer
    pagination_class = CustomPagination
    permission_classes = (CandidatesSearchPermission, )

    def get_queryset(self, skill_name=None):
        """
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(skill=skill_name).order_by("-score")
        return queryset

    def post(self, request, *args, **kwargs):
        skill_name = request.data.get("skill_name")
        queryset = self.get_queryset(skill_name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
