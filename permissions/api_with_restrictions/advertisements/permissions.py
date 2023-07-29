from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_staff:
            return True
        return request.user == obj.creator


class IsOwnerForFavorite(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
