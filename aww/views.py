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

def project(request, id):
    date = dt.date.today
    project = []
    projects = Project.objects.get(id=id)
    print(project)
    return render(request,  'project.html', {"date": date, "projects": projects})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
