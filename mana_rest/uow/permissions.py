from rest_framework.permissions import BasePermission
from .models import UserRoles

class IsAdminUser(BasePermission):
    """Permite acceso solo a administradores"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRoles.ADMIN

class IsEmployeeEUser(BasePermission):
    """Permite acceso solo a empleados"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRoles.EMPLOYEE