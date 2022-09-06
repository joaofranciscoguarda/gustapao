from rest_framework import permissions


class UpdateAndDelete(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
      
      if request.method in permissions.SAFE_METHODS:
        return True
      
      if request.user == obj or request.user.is_superuser:
        return True
      
      return False