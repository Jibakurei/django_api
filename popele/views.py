from django.shortcuts import render,redirect
from datetime import time
from popele.models import BookInfo, HeroInfo
from var_dump import var_dump
from django.http import HttpResponse,JsonResponse

from datetime import date
from .Serializer import BookInfoSerializer,HeroinfoSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.parsers import JSONParser
from django_filters import rest_framework
import json
from django.core import serializers
from .form import PostForm
#from popele.serializer import BookInfoSerializer
class BookInfoViewset(viewsets.ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def perform_Bookinfo(self,serializer):
        serializer.save()



def index(request):
    #books=serializers.serialize("json",BookInfo.objects.all())
    books=BookInfo.objects.all()
    heros=HeroInfo.objects.all()
    return render(request,'index.html',{'books':books,'heros':heros})
    #return HttpResponse(books)
    #return render(request,'index.html',{'books':json.dumps(books),'heros':json.dumps(heros)})

# def addBook(request):
#     if request.method == 'POST':
#         book=PostForm(request.POST)
#         if book.is_valid():
#             post = book.save(commit=False)
#             post.save()
#             return redirect('book_add.html',{'book':book})
#     else:
#         return redirect('/index/')

def addBook(request):
    if request.method == 'GET':
        return render (request,'book_add.html')
    elif request.method == 'POST':
        btitle = request.POST['btitle']
        bread = request.POST['bread']
        bcomment = request.POST['bcomment']
        booklist = BookInfo.objects.Create(btitle=btitle,bread=bread,bcomment=bcomment)
        booklist = BookInfo.objects.all()
        return render(request,'book_add.html',{'booklist':booklist})
    else:
        return redirect('index.html')

# 根据图书id删除一本书的视图函数
def delBook(request,bid):
    # 查询出图书
    b=BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index/')
# Create your views here.

def upbook(request):
    if request.metthod == 'POST':
        b = BookInfo.objects.get('id')
        booklist = BookInfo.objects.filters(id=b).frist()
        return render(request,'book_list')
    else:
        return redirect('index')
    pass

def api_list(request):
    if request.method=='GET':
        api = BookInfo.objects.all()
        Serializer = BookInfoSerializer(api,many=True)
        return JsonResponse(Serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        Serializer = BookInfoSerializer(data=data)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data,status=201)
        return JsonResponse(Serializer.errors,status=400)
    pass

def api_act(request,pk):
    try:
        api = BookInfo.objects.get(pk=pk)
    except BookInfo.DoesNotExist:
        return HttpResponse(status=404)
        pass
    pass
    if request.method=='GET':
        serializer = BookInfoSerializer(api)
        return JsonResponse(serializer.data)
        pass
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookInfoSerializer(api,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        api.delete()
        return HttpResponse(status=200)