from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only (GET) for everyone, but only author can edit/delete
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.author == request.user) or (request.user.role == 'ADMIN')


class IsStaffOrAdminOrReadOnly(permissions.BasePermission):
    """
    Allows only staff or superusers to create/edit/delete.
    Everyone can read (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        # Allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user is authenticated and is either staff or admin
        return bool(
            request.user and 
            request.user.is_authenticated and 
            (request.user.is_staff or request.user.is_superuser)
        )


