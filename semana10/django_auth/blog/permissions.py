from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        if not request or not request.user.is_authenticated:
            return False

        role = request.user.role.name

        return role == 'Admin'