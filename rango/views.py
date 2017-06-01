from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/about.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/'>Rango</a>.")
