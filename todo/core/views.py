from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from todo.core.models import Task
from todo.core.forms import TaskForm

# Create your views here.
def home(request):
    pending_tasks = Task.objects.filter(done=False)
    completed_tasks = Task.objects.filter(done=True)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:home'))
        return render(
            request, 'tasks/home.html', 
            {
                'form': form, 
                'pending_tasks': pending_tasks,
                'completed_tasks': completed_tasks
            },
            status=400
        )
    return render(
        request, 'tasks/home.html', 
        {
            'pending_tasks': pending_tasks,
            'completed_tasks': completed_tasks
        })

def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('core:home'))