"""djangodocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
import xadmin
# from goods.views_base import GoodsListView
from rest_framework.documentation  import include_docs_urls
from goods.views import GoodsListView,CategoryViewset
from user.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewSet,LeavingMssageViewset,AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()  
  
# 配置goods的url  
router.register(r'goods', GoodsListView, base_name="goods")  
  
# 配置category的url  
router.register(r'categorys', CategoryViewset, base_name="categorys") 

# 配置codes的url  
router.register(r'codes', SmsCodeViewset, base_name="codes")  

# 配置User的url  
router.register(r'User', UserViewset, base_name="User")  

# 配置UserFav的url  
router.register(r'UserFav', UserFavViewSet, base_name="UserFav")  

# 配置Message的url  
router.register(r'Message', LeavingMssageViewset, base_name="Message")

# 配置Address的url  
router.register(r'Address', AddressViewset, base_name="Address")  

# 配置ShoppingCart的url  
router.register(r'ShoppingCart', ShoppingCartViewset, base_name="ShoppingCart") 
 
# 配置orders的url  
router.register(r'orders', OrderViewset, base_name="orders")

# goods_list = GoodsListView.as_view({  
#     'get': 'list',  
# })  



urlpatterns = [
    url(r'^',include(router.urls)),  
    #path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='mtianyan超市文档')),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # path('goods/',GoodsListView.as_view(),name="goods-list"),
    path('api-auth/', include('rest_framework.urls')),
    # url(r'goods/$',goods_list,name="goods-list"),  
    path('api-token-auth/',views.obtain_auth_token),
    
    path('login/', obtain_jwt_token )



]
