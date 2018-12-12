from rest_framework import serializers
from .models import Goods,GoodsCategory,GoodsImage

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = "__all__"
        

class GoodsSerializer(serializers.ModelSerializer):
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"
