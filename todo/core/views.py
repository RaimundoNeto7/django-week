from django.shortcuts import render
from django.http.response import HttpResponse
from todo.core.forms import TaskForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/home.html')