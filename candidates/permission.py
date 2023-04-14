# encoding: utf-8

from rest_framework import permissions

from search_system.settings import APP_ID


class CandidatesSearchPermission(permissions.BasePermission):
    """
    Global permission check for CandidatesSearchAPIView
    """

    def has_permission(self, request, view):
        appid = request.data['appid']
        return appid in APP_ID
