from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Djannnngo!</h1>')

def about(request):
    return HttpResponse('<h1>About us :</h1> <p>This is a webapplication made with django by Cubouyaka </p>')

def contactus(request):
    return HttpResponse('<h1>Contact us :</h1> <p>Soon</p>')

def listing(request):
    return HttpResponse('<h1>Listing :</h1> <p>There will be a list</p>')