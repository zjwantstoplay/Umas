from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect



# Create your views here.
from .models import *

def home(request):
    return render(request,"home.html",context={"current_tab":"home"})

def readers(request):
    return render(request,"readers.html",context={"current_tab":"readers"})

def shopping(request):
    return HttpResponse ("Welcome to shopping")

def save_student(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})

def readers_tab(request):
    readers = reader.objects.all()
    return render(request,"readers.html",context={"current_tab":"readers","readers":readers})