
from django.shortcuts import render
from .models import Task, typeTask
# Create your views here.
from .models import Task
def home(request):
    return render(request, "home.html", {})

def viewTasks(request):
    types = typeTask.objects.order_by('id')
    return render(request, "tasksType.html", {'types': types})