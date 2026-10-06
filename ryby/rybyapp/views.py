from urllib import request
from django.shortcuts import render
from .models import Ryba,OkresOchronny


def index(request):
    ryby = Ryba.objects.all()
    okres = OkresOchronny.objects.all()
    return render(request, 'index.html',{"ryby":ryby,"okres":okres})