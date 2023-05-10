from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from  . models import Profile

from projects . models import Project
from . forms import  custom_user_creation
from . forms import profile_form
# Create your views here.

def profile(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,"users/profiles.html",context)


def user_profile(request,pk):
    profile = Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request,"users/user-profile.html",context)

def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user is not exist")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "user was logged")
            return redirect("profile")
        else:
            messages.error(request, "username or password dosent exist")
    context={'page':page}
    return render(request,'users/login_register.html',context)


def register_page(request):
    page="register"
    form = custom_user_creation()

    if request.method == "POST":
        form = custom_user_creation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"user was created")
            login(request,user)
            return redirect("edit_account")
        else:
            messages.error(request,"an error found")
    context={'page':page,'form':form}
    return render(request,"users/login_register.html",context)


def log_out(request):
    logout(request)
    messages.success(request, "user was logged out")
    return redirect('profile')



@login_required(login_url='login_page')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile':profile,'skills':skills,'projects':projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login_page')
def edit_account(request):
    profile =request.user.profile
    form = profile_form(instance=profile)
    if request.method == "POST":
        form =profile_form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user_account")

    context={'form':form}
    return render(request,"users/profile_form.html",context)