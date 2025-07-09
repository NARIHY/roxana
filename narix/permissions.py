# ou narix/permissions.py

from rest_framework import permissions
from django.conf import settings

class AllowAllIfDebug(permissions.BasePermission):
    def has_permission(self, request, view):
        if settings.DEBUG:
            return True
        return False  # Bloquer ou autoriser selon besoin en prod
