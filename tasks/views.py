# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
import json

def task_list(request):
    category = request.GET.get('category', 'all')

    if category == 'all':
        tasks = Task.objects.all().order_by('date')  # Сортування тільки за датою
    else:
        tasks = Task.objects.filter(category=category).order_by('date')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'selected_category': category,
    })

def completed_tasks(request):
    tasks = Task.objects.filter(status='completed').order_by('date')
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})

def toggle_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get('id')
        task = get_object_or_404(Task, id=task_id)

        if task.status == 'pending':
            task.status = 'completed'
        else:
            task.status = 'pending'

        task.save()

        return JsonResponse({
            'id': task.id,
            'new_status': task.status,
            'status_display': task.get_status_display()
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_task_order(request):
    if request.method == 'POST':
        order = json.loads(request.POST.get('order'))
        for index, task_id in enumerate(order):
            task = Task.objects.get(id=task_id)
            task.order = index
            task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_statistics(request):
    completed_tasks = Task.objects.filter(status='completed').count()
    pending_tasks = Task.objects.filter(status='pending').count()
    return render(request, 'tasks/statistics.html', {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    })

def task_list(request, category=None):
    tasks = Task.objects.all()
    if category:
        tasks = tasks.filter(category=category)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})