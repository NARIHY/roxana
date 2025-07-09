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
    
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Autorise seulement les modifications aux utilisateurs admins.
    La lecture est autorisée à tous les utilisateurs authentifiés.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # création ouverte sans auth

        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Méthodes modifiant (PUT, PATCH, DELETE)
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role
            and request.user.role.name == 'Admin'
        )
