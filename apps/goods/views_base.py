from django.db import models
from .models import Goods
from django.views.generic import View
class GoodsListView(View):
    def get(self,request):  
        json_list = []
        goods = Goods.objects.all()[:10]
        from django.forms.models import model_to_dict 
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        import json
        from django.core import serializers
        json_date = serializers.serialize('json',goods)
        json_date = json.loads(json_date)
        from django.http import HttpResponse,JsonResponse
        return JsonResponse(json_date,safe=False)