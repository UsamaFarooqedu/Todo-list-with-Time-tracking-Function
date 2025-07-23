from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import User_Details_Form
from datetime import datetime
from django.utils import timezone
from .serializer import TaskSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

# Create your views here.

def task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completion_time_str = request.POST.get('completion_time')


        completion_time = None
        if completion_time_str:
            try:
                completion_time = datetime.strptime(completion_time_str, "%Y-%m-%dT%H:%M")
            except ValueError:

                return render(request, 'new.html', {
                    'tasks': tasks,
                    'error': 'Invalid completion time format.'
                })

        task = Task(title=title, description=description, completion_time=completion_time)
        task.save()
        return redirect('new')

    return render(request, 'new.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('new')
    return render(request, 'edit.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('new')

 
def details(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks)
    json_data = JSONRenderer().render(serializer.data)

    return render(request, 'details.html', {'tasks': tasks})

def list_view(request, pk=None):
    if pk:
        task = get_object_or_404(Task, pk=pk)
        tasks = [task] 
    else:
        tasks = Task.objects.all()
    return render(request, 'details.html', {'tasks': tasks})

