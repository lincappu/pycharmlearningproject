from django.shortcuts import render,HttpResponse

def host(request):
    return HttpResponse('openstack的host页面')
