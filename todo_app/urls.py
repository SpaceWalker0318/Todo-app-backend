from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='todo-home'),
    path('todo-list', views.todoList, name='todo-list')
]