from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import UserFavSerializer,UserFavDetailSerializer,AddressSerializer,LeavingMessageSerializer
from .models import UserFav,UserAddress,UserLeavingMessage
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from apps.utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

class UserFavViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer

class LeavingMssageViewset(mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

class AddressViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
        pass