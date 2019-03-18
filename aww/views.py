from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *

def index(request):
    date = dt.date.today
    projects = Project.objects.all()
    return render(request, 'index.html', {"date": date,'projects':projects})

def profile(request):
    date = dt.date.today
    profile = []
    profiles = Profile.objects.get(first_name=request.user.username)

    return render(request, 'profile.html', {"date": date, "profiles": profile})

def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    day = days[day_number]
    return day

@login_required(login_url='/accounts/login/')
def project(request):
    date = dt.date.today
    project = []
    projects = Project.objects.all()
    

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('project')
    else:
        form = NewsLetterForm()

    return render(request,  'project.html', {"date": date, "projects": projects, "letterForm": form})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
        return render(request,'success.html')
        
    else:
        form = SignupForm()
        return render(request, 'signup.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
    
