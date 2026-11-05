from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TaskForm()

    tasks = Task.objects.all()

    return render(request, 'main/home.html', {
        'form': form,
        'tasks': tasks
    })

def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.is_done = True
        task.save()

    return redirect('home')

# https://github.com/Iskender-developer/Todo-django
