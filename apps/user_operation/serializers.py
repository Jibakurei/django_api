from rest_framework import serializers
from .models import UserFav,UserLeavingMessage,UserAddress
from goods.serializers import GoodsSerializer
from rest_framework.validators import UniqueTogetherValidator

class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ("goods","id")
    
class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")
                
class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%D %H:%M')
    class Meta:
        model = UserLeavingMessage
        fields = ("user","message_type","id","subject","message","file","add_time")

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%D %H:%M')
    class Meta:
        model = UserAddress
        fields = ("user","add_time","city","province","district","address","signer_name","id","signer_mobile")
        pass
    pass