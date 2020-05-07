from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Object-level permission to only allow the user to see their user object.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user