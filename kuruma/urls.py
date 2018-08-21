"""kuruma URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from . import view
from calc import views as calc_views
from popele import views as popele_views
from rest_framework import routers
from popele.views import BookInfoViewset

router = routers.DefaultRouter()
router.register(u'BookInfo',BookInfoViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^calc/$',calc_views.index,name='calc'),
    path('admin/', admin.site.urls),
    path('add/<int:a>/<int:b>/',calc_views.add1,name='add1'),

    url(r'^index/$',popele_views.index),
    url(r'^addBook/$',popele_views.addBook),
    url(r'^delBook(\d+)/$',popele_views.delBook),
    url(r'^add/(\d+)/(\d+)/$', calc_views.add_redirect),
    url(r'^$',view.hello),
    url(r'^api-auth/$',include('rest_framework.urls', namespace='rest_framwork')),
    url(r'^api_list/$',popele_views.api_list),
    url(r'^api_list/(?P<pk>[0-9]+)/$',popele_views.api_act),
]
