from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json
import time
import random


# Create your views here.
def children(request):
    return render(request,'children.html')

def index(request):
    return render(request,'index.html')

def members(request):
    return render(request,'members.html')
    
    
def user(request):
    return render(request,'userManage.html')

