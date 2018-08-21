from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

#from popele.models import Person,Hon




def index(request):
   #Persons = Person.objects.all()
   arr=[1,2,3,4]

         
   #return render(request,'calc.html',{'athlete_list':arr,})
   #json_data = json.dumps(arr,separators=(',', ':'))
   return render(request,'calc.html',{'arry': arr})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add1(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
    
    pass
def add_redirect(request,a,b):
    return HttpResponseRedirect(
        reversed('add',args=(a,b))
    )
    pass


# Create your views here.
