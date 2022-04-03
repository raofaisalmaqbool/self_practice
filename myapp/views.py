from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForms
from myapp.models import *
from http.client import HTTPResponse
from urllib import request


# Create your views here.

def index(request):
    data = {
        'heading0': 'helow yahan djnago sy data html page pr ha raha ha',
        'clist': ['php', 'java', 'python', 'djanago'],
        'students': [
            {'name': 'ali', 'phone': '789475987'},
            {'name': 'ahmad', 'phone': '457475987'}
        ],
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render(request, "index.html", data)


def home(request):
    # assending and descending by id and service_title,,, by alphabet and number(id)
    # service_data = Service.objects.all().order_by('-service_title')
    service_data = Service.objects.all().order_by('-id')[1:4]  # negitive index not supported
    news_data = News.objects.all()

    # for i in service_data:            # console per data print karwany ky liya
    #     print(i.service_title)

    context ={
        'service_data' : service_data,
        'news_data' : news_data
    }
    return render(request, "home.html", context)


def courses(request):
    return HttpResponse("welcome to courses")


def coursedetails(request, productid):
    return HttpResponse(productid)


def base(request):
    return render(request, "base.html")


def about_us(request):
    global output
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "about_us.html", {'output': output})


def contact_us(request):  # form sy data lana or osko print krwana secreen pr
    finalans = 0
    variable1 = UserForms

    data = {'form': variable1}
    try:
        if request.method == "POST":
            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])

            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))

            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))

            finalans = n1 + n2
            data = {
                'n1': n1,
                'n2': n2,
                'form': variable1,  # form model waly ky liya
                'output': finalans}

            # Mehthods for rediract
            # return HttpResponseRedirect('/about_us/')
            # return redirect('/about_us/')
            url = "/about_us/?output={}".format(finalans)
            return redirect(url)
            # return render(request, "contact_us.html", data)

    except:
        pass
    # return render(request, "contact_us.html", {'output':finalans})
    return render(request, "contact_us.html", data)


def submitform(request):
    return HttpResponse(request)


def calculator(request):
    context = {}
    output = None
    try:
        if request.method == "POST":
            value1 = eval(request.POST.get('num1'))
            value2 = eval(request.POST.get('num2'))
            operator = request.POST.get('opr')
            if operator == '+':
                output = value1 + value2
            elif operator == '-':
                output = value1 - value2
            elif operator == '*':
                output = value1 * value2
            elif operator == '/':
                output = value1 / value2

            context = {
                'value1': value1,
                'value2': value2,
                'output': output
            }

    except:
        output = "something is wrong!"

    return render(request, 'calculator.html', context)


def even_odd(request):
    context ={}
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request, 'even_odd.html', {'error':True})

        n1 = eval(request.POST.get('num1'))

        n2 = n1*n1

        even_odd_var = UserForms
        context = {
            'n1': n1,
            'n2' : n2,
            'even_odd_var': even_odd_var
        }
        return render(request, 'even_odd.html', context)
    return render(request, 'even_odd.html')
