from random import choice

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
# 但是当第三方模块根本不知道你的user model在哪里如何导入呢
from django.contrib.auth import get_user_model
# 这个方法会去setting中找AUTH_USER_MODEL
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from djangodocs.settings import APIKEY
from rest_framework.response import Response
from rest_framework import mixins, permissions, authentication
from rest_framework import viewsets, status
from .models import VerifyCode
from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer
from apps.utils.yunpian import YunPian

User = get_user_model()
# 发送验证码是创建model中一条记录的操作
from rest_framework.mixins import CreateModelMixin
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self,username=None,password=None,**kwags):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.chenck_password(password):
                return user
                
        except Exception as e:
            return None
            
class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializer
    
    def generate_code(self):
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)
        
        
    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        if sms_status["code"] !=0:
            return Response({
                "mobile":sms_status["msg"]
            },status=status.HTTP_400_BAD_REQUEST)
            
        else:
            code_record = VerifyCode(code=code,moblie=mobile)
            code_record.save()
            return Response({
                "mobile":mobile
            },status=status.HTTP_201_CREATED)
            
class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # 重写该方法，不管传什么id，都只返回当前用户
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
        
    
