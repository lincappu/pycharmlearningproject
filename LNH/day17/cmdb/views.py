from django.shortcuts import render,HttpResponse

def host(request):
    return HttpResponse('cmdb的host页面')
