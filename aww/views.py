from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def index(request):
    date = dt.date.today
    return render(request, 'index.html', {"date": date})

def profile(request):
    date = dt.date.today
    return render(request, {"date": date})

def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    day = days[day_number]
    return day

def project(request):
    date = dt.date.today
    return render(request, {"date": date})
    
