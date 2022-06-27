
from django.shortcuts import render, HttpResponseRedirect
from .models import Task, typeTask, subType, Profile
from django.urls import reverse

def home(request):
    return render(request, "home.html", {})

def viewTypeTasks(request):
    types = typeTask.objects.all()
    subtypes = subType.objects.all()
    return render(request, "tasksType.html", {'types': types, 'subtypes': subtypes})

def viewTasks(request, subtype):
    type = subType.objects.get(slug=subtype)

    tasks = Task.objects.filter(type=type)

    return render(request, "tasks.html", {'tasks': tasks, 'type': type})

def Profile(request):
    return render(request, "profile.html", {'user': request.user})

def viewTraining(request):
    types = typeTask.objects.all()
    subtypes = subType.objects.all()
    return render(request, "tasksType.html", {'types': types, 'subtypes': subtypes})
