from django.urls import path, include
from .views import task, edit_task, delete_task, details,list_view

urlpatterns = [
    path('', task, name='new'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('details/<int:pk>', details, name='details'),
    path('list_view/', list_view, name='list_view'),  # For all tasks
    path('list_view/<int:pk>/', list_view, name='single_task_view'),  # For single task
    path('auth/', include('auth_app.urls')),
] 
