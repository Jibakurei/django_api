from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello")
    pass

def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
    
    pass

