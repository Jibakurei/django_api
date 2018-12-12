from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import mixins  
from rest_framework import generics  
from rest_framework.pagination import PageNumberPagination  
from rest_framework import viewsets  
from rest_framework import status  
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from .models import Goods,GoodsCategory
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100
    pass

class GoodsListView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):  
    """ 
    List all snippets, or create a new snippet. 
    """  
    queryset = Goods.objects.all()
    serializer_class =  GoodsSerializer
    pagination_class = GoodsPagination
    filter_fields = ('name', 'shop_price')
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)  
    # filter_class = GoodsFilter
    # search_fields = ('name', 'goods_brief', 'goods_desc')  
    # ordering_fields=('sold_num','add_time')  
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    #     pass
  
    # def get(self, request, format=None):  
    #     goods = Goods.objects.all()[:10]  
    #     goods_serializer = GoodsSerializer(goods, many=True)  
    #     return Response(goods_serializer.data)  

    # def post(self, request, format=None):
    #         serializer = GoodsSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    authentication_classes = (TokenAuthentication,)
class CategoryViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    pass