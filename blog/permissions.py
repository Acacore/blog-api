from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only (GET) for everyone, but only author can edit/delete
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user