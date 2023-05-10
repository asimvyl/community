from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import *
from . forms import ProjectForm

# Create your views here.

def home(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    projects=Project.objects.filter(title__icontains=search_query)
    context={'projects':projects,'search_query':search_query}
    return render(request,"projects/projects.html",context)


def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    context={'projectobj':projectobj,'tags':tags}
    return render(request,'projects/single-project.html',context)

@login_required(login_url="login_page")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("projects")
        else:
            print(form.errors)

        
    
    context={'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login_page")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project = form.save()
            return redirect("account")
        else:
            print(form.errors)    
    context={'form':form,'project':project}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login_page")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("home")
    context={'object':project}
    return render(request,"projects/delete.html",context)







