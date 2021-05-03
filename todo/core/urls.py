from django.urls.conf import path
from todo.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home')
]