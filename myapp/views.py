from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
    data = {
        'heading0' : 'helow yahan djnago sy data html page pr ha raha ha',
        'clist': ['php', 'java', 'python', 'djanago'],
        'students': [
            {'name': 'ali', 'phone': '789475987'},
            {'name': 'ahmad', 'phone': '457475987'}
        ],
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render(request, "index.html", data)


def home(request):
    return HttpResponse("welcome to home")


def courses(request):
    return HttpResponse("welcome to courses")


def coursedetails(request, productid):
    return HttpResponse(productid)


def base(request):
    return render(request, "base.html")


def about_us(request):
    return render(request, "about_us.html")