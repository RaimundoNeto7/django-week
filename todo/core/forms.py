from django.forms.models import ModelForm
from todo.core.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'done']