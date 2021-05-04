from django.urls.conf import path
from todo.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:task_id>', views.detail, name='detail'),
    path('delete/<int:task_id>', views.delete, name='delete')
]