from django.urls import path

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name = 'main'),
    path('tasks', views.viewTypeTasks, name = 'tasksType'),
    path('tasks/<slug:subtype>', views.viewTasks, name = 'tasks')

]
    #path('/tasks/<int:task_id>', views.task, name = 'task')