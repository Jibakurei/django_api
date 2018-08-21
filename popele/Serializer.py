from rest_framework import serializers
from popele.models import BookInfo,HeroInfo
from django.contrib.auth.models import User
from django.forms import widgets
class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

    pass

class HeroinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        filter = '__all__'
    pass