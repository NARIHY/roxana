# accounts/permissions.py
from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):
    """
    Autorise uniquement les utilisateurs dont role.name == 'Admin'.
    """
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role
            and request.user.role.name == 'Admin'
        )
