from django.urls import path
from TasksApp import views


app_name = 'TasksApp'

urlpatterns = [
    path('', views.addtaskView, name='add_task'),
    path('tasks/', views.tasklistView, name='task_list'),
    path('search/', views.searchtasksView, name='search_tasks'),
]