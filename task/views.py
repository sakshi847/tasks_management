from django.shortcuts import get_object_or_404, render, redirect
from .models import Task, TaskAssignment
from .forms import TaskForm, TaskAssignmentForm

def task_dashboard(request):
    tasks = TaskAssignment.objects.all()
    employees = set(task.employee for task in tasks)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status="Completed").count()
    in_progress_tasks = tasks.filter(status="In Progress").count()
    pending_tasks = tasks.filter(status="Pending").count()

    context = {
        'tasks': tasks,
        'employees': employees,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'pending_tasks': pending_tasks
    }
    
    return render(request, 'task/dashboard.html', context)

def task_dashboard(request):
    tasks = Task.objects.all()
    task_assignments = TaskAssignment.objects.all()
    return render(request, 'task/dashboard.html', {'tasks': tasks, 'task_assignments': task_assignments})

def assign_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.task = task
            assignment.assigned_by = request.user.employee  
            assignment.save()
            return redirect('task_dashboard')
    else:
        form = TaskAssignmentForm()
    
    return render(request, 'task/assign_task.html', {'form': form, 'task': task})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/update_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_dashboard')

