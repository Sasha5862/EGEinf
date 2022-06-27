from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name = 'main'),
    path('tasks', views.viewTypeTasks, name = 'tasksType'),
    path('tasks/<slug:subtype>', views.viewTasks, name = 'tasks'),
    path('training/', views.viewTraining, name = 'training'),
    path('training/<slug:subtype>', views.viewTrainingTasks, name = 'training_tasks'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='home:main'), name='logout'),
    path('accounts/profile/', views.Profile, name='profile'),

]
    #path('/tasks/<int:task_id>', views.task, name = 'task')