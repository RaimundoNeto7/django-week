from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from todo.core.forms import TaskForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:home'))
        return render(request, 'tasks/home.html', {'form': form}, status=400)
    return render(request, 'tasks/home.html')