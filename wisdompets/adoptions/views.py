from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h2>Home View</h2>')

def pet_detail(request, id):
    return HttpResponse('<h2>pet_detail view with id {}</h2>'.format(id))