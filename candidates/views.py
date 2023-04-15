from django.db.models import QuerySet
from django.core.cache import cache

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from candidates.models import CandidateSkillScores
from candidates.pagenate import CustomPagination
from candidates.permission import CandidatesSearchPermission
from candidates.serializers import CandidateSkillSearchSerializer
from search_system.settings import CACHE_TTL

class CandidatesSearchAPIView(generics.CreateAPIView):
    """
    CandidatesSearchAPIView
    post:
        Displays all candidates who meet the criteria
    """
    queryset = CandidateSkillScores.objects.all()
    serializer_class = CandidateSkillSearchSerializer
    pagination_class = CustomPagination
    permission_classes = (CandidatesSearchPermission,)

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
        cache_key = f"{skill_name}-{request.data['page']}-{request.data['page_size']}"
        data = cache.get(cache_key)
        if data is None:
            queryset = self.get_queryset(skill_name)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                cache.set(cache_key, serializer.data, CACHE_TTL)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set(cache_key, serializer.data, CACHE_TTL)
            return Response(serializer.data)

        return Response(data)
