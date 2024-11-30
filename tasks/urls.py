from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('update_order/', views.update_task_order, name='update_task_order'),
    path('statistics/', views.task_statistics, name='task_statistics'),
    path('tasks/toggle-status/', views.toggle_task_status, name='toggle_task_status'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
]
