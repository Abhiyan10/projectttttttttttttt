from django.shortcuts import render, redirect
from django.views import generic

from django.views.generic import TemplateView

from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .models import student, attendance_history
from datetime import date
# Create your views here.

def login(request):
    return render(request, 'login.html')





def home(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username ,password=password )
        
        if User is not None:
            auth.login(request, User)
            return render(request,'home.html')
        else:
            messages.info(request,'invalid credentials') 
            return render(request,'login.html')  
    else:
        return render(request,'login.html')    

def bluetooth(request):
    return render(request, 'bluetooth.html')



def about(request):
    return render(request, 'about.html')

def refresh(request): 
    records = student.objects.all()
    for i in records:
        if i.attendence_stat == True:
            a = attendance_history(student = i.full_name, date=date.today(), attendance=i.attendence_stat)
            a.save()
            i.attendence_stat = False
            i.save()
    return render(request, 'home.html')
    


# def count(request): 
#     records = attendance_history.objects.all()
#     count1=0
#     for i in records:
#         for j in records:
#             if i.full_name == j.full_name:
#                 count1= count1 + 1
#             # a = attendance_history(student = i.full_name, date=date.today(), attendance=i.attendence_stat)
#             # a.save()
#             # i.attendence_stat = False
#             # i.save()
#     return render(request, 'home.html')    