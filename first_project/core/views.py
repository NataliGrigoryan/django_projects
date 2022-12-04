from django.shortcuts import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("<h1>hello</h1>")

def introduction(request):
    return HttpResponse("my name is djangooo")

def time(request):
    t = datetime.now()
    return HttpResponse(t)

def dictionary(request):
    d = dict()
    for x in range(1, 16):
        d[x] = x ** 2
    return HttpResponse([d])
