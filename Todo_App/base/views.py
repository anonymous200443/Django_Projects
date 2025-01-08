from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from base.models import Task
from django.http import HttpResponse, Http404

# Home View
def home_view(request):
    return render(request, "home.html", {})

# All Tasks View (Create and List Tasks)
def all_tasks(request):
    tasks = Task.objects.all().order_by('-id')
    task_form = TaskForm(request.POST or None)

    if request.method == "POST":
        if task_form.is_valid():
            task_form.save()
            return redirect("all_tasks")

    context = {
        'form': task_form,
        'form2': tasks
    }
    return render(request, "all_tasks.html", context)

# Update Task View
# def update_view(request, id):
#     task = get_object_or_404(Task, id=id)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return render(request,'task_update.html',{'form':form})
#     else:
#         form = TaskForm(instance=task)

#     context = {
#         'form': form
#     }
#     return render(request, 'task_update.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task

def update_view(request, id):

    task = get_object_or_404(Task, id=id)  # Fetch the task to be updated
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  # Bind form with the existing task instance
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('all_tasks')  # Redirect to the page that lists all tasks
    else:
        form = TaskForm(instance=task)  # Pre-fill the form with existing task data

    context = {
        'form': form,
        'task': task,
    }
    print(context)
    return render(request, 'task_update.html', context)  # Use a dedicated update template


# Delete Task View
def delete_view(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        from django.contrib import messages
        messages.success(request, "Task deleted successfully")
        return redirect("all_tasks")
    except Task.DoesNotExist:
        raise Http404("Task not found.")
