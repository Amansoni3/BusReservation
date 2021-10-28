from django.shortcuts import render
from . import Pool

def AboutUs(request):
    return render(request, "AboutUs.html")

def ContactUs(request):
    return render(request,"ContactUs.html")

def Index(request):
    return render(request,"index.html")
