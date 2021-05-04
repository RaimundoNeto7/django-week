import pytest

from django.urls import reverse
from pytest_django.asserts import assertContains
from todo.core.models import Task

def test_home_status_code(client, db):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200

def test_contains_form(client, db):
    response = client.get(reverse('core:home'))
    assertContains(response, '<form')

def test_contains_submit_btn(client, db):
    response = client.get(reverse('core:home'))
    assertContains(response, '<button type="submit"')

def test_valid_task_exists_in_db(client, db):
    response = client.post(reverse('core:home'), data={'title': 'task#1'})
    assert Task.objects.exists()

def test_valid_task_status_code(client, db):
    response = client.post(reverse('core:home'), data={'title': 'task#1'})
    assert response.status_code == 302

def test_invalid_task_not_in_db(client, db):
    response = client.post(reverse('core:home'), data={'title': ''})
    assert not Task.objects.exists()

def test_invalid_task_status_code(client, db):
    response = client.post(reverse('core:home'), data={'title': ''})
    assert response.status_code == 400


@pytest.fixture
def pending_tasks(db):
    tasks = [
        Task(title='Tarefa #1', done=False),
        Task(title='Tarefa #2', done=False),
    ]
    Task.objects.bulk_create(tasks)
    return tasks

def test_contains_list_tasks(client, pending_tasks):
    response = client.get(reverse('core:home'))
    for task in pending_tasks:
        assertContains(response, task.title)