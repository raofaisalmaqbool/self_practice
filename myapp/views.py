from django.shortcuts import render, redirect, HttpResponse
  

# Create your views here.

def home(request):
    return HttpResponse("welcome to home")

def courses(request):
    return HttpResponse("welcome to courses")

def coursedetails(request, productid):
    return HttpResponse(productid)