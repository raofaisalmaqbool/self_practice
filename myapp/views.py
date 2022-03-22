from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect


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
    return HttpResponse("welcome to home")


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
    return render(request, "about_us.html", {'output':output})


def contact_us(request, finalans=None):             #form sy data lana or osko print krwana secreen pr
    finalans=0
    data = {}
    try:
        if request.method == "POST":
        #n1 = int(request.GET['num1'])
        #n2 = int(request.GET['num2'])

            #n1 = int(request.GET.get('num1'))
            #n2 = int(request.GET.get('num2'))

            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))

            finalans= n1 + n2
            data = {
            'n1' : n1,
            'n2' : n2,
            'output' : finalans}

            #Mehthods for rediract
            #return HttpResponseRedirect('/about_us/')
            #return redirect('/about_us/')
            url = "/about_us/?output={}".format(finalans)
            return redirect(url)

    except:
        pass
    #return render(request, "contact_us.html", {'output':finalans})
    return render(request, "contact_us.html", data)
