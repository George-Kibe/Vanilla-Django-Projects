from django.urls import path, include
from home import views

app_name='home'

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks', views.tasks, name="tasks"),
    path('test', views.test, name="test"),
    path('delete_task/<str:pk>/', views.deleteTask, name="deletetask"),
    path('update_task/<str:pk>/', views.updateTask, name="updatetask"),
    ]
