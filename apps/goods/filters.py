from django_filters import rest_framework as filters
from .models import Goods

class GoodsFilter(filters.FilterSet):
    price_min = filters.NumberFilter(name='shop_price',lookup_expr='get')
    price_max = filters.NumberFilter(name='shop_price',lookup_expr='lte')
    class Meta:
        model = Goods
        fields = ['price_min','price_max', 'name', 'is_hot']
        pass
    pass