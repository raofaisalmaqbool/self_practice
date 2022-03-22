from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    data = {
        'heading0' : 'helow yahan djnago sy data html page pr ha raha ha'
    }
    return render(request, "index.html", data)

def home(request):
    return HttpResponse("welcome to home")

def courses(request):
    return HttpResponse("welcome to courses")

def coursedetails(request, productid):
    return HttpResponse(productid)