# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from .models import details


from django.shortcuts import render,redirect

# Create your views here.
def login_view(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        if u=='deepak' and p=='deepak@1':
            return redirect('company:homepage')
        else:
            messages.warning(request, 'username or password wrong')

    return render(request,'login.html')

def index(request):
    return render(request,'homepage.html')

def manager(request):
    obj=details.objects.all()
    context={
        'data':obj
    }

    return render(request,'manager_view.html',context)

def other(request,x):
    if x=='1':
        obj = details.objects.filter(Location__in=["Delhi", "Gurgaon"])
        context = {
            'data': obj
        }
        return render(request,'other_view.html',context)
    if x=='2':
        obj=details.objects.filter(Location__in=["Jaipur","Kota"])
        context = {
            'data': obj
        }
        return render(request,'other_view.html',context)
    if x=='3':
        obj=details.objects.filter(Location="Delhi")
        context = {
            'data': obj
        }
        return render(request,'other_view.html',context)

    return render(request, 'other_view.html')

def customer(request,x):
    obj=details.objects.get(id=x)
    context = {
        'data': obj
    }
    return render(request,'customer_detail.html',context)