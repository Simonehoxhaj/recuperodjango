from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'libroOspiti/home.html')


def messaggi(request):
    return render(request,"libroOspiti/messaggi.html")