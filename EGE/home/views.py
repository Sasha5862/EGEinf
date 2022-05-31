
from django.shortcuts import render
from .models import Task, typeTask, subType
# Create your views here.
from .models import Task
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