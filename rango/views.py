from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contex_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=contex_dict)


def about(request):
    contex_dict = {'name': 'Jiangyi'}
    return render(request, 'rango/about.html', context=contex_dict)
