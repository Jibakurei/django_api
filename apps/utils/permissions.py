from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_objects_permisson(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
