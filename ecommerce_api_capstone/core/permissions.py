from rest_framework import permissions

class ProductPermissions(permissions.BasePermission):
    """
    Custom permission to only allow admin to delete it.
    anyone read and authenticated create and update
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the product.
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the product.
        if request.method == "DELETE":
            return request.user.is_staff

        return request.user.is_authenticated
    
class CategoryPermissions(permissions.BasePermission):
    """
    Custom permission to only allow admin to create, update, delete categories.
    anyone can read categories.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        return request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff