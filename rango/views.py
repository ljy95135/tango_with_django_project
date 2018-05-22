from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contex_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=contex_dict)


def about(request):
    return HttpResponse("Rango says hey there is the about page.")
