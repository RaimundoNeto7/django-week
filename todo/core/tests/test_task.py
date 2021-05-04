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
def list_pending_tasks(db):
    tasks = [
        Task(title='Tarefa #1', done=False),
        Task(title='Tarefa #2', done=False),
    ]
    Task.objects.bulk_create(tasks)
    return tasks

def test_contains_pending_tasks(client, list_pending_tasks):
    response = client.get(reverse('core:home'))
    for task in list_pending_tasks:
        assertContains(response, task.title)

@pytest.fixture
def pending_task(db):
    return Task.objects.create(title='Tarefa #1', done=False)

def test_update_task_to_done(client, pending_task):
    response = client.post(reverse('core:detail', kwargs={'task_id': pending_task.id}), data={'done': 'true', 'title': pending_task.title})
    assert Task.objects.first().done

def test_update_task_to_done_status_code(client, pending_task):
    response = client.post(reverse('core:detail', kwargs={'task_id': pending_task.id}), data={'done': 'true', 'title': pending_task.title})
    assert response.status_code == 302

@pytest.fixture
def list_completed_tasks(db):
    tasks = [
        Task(title='Tarefa #3', done=True),
        Task(title='Tarefa #4', done=True),
    ]
    Task.objects.bulk_create(tasks)
    return tasks

def test_contains_completed_tasks(client, list_completed_tasks):
    response = client.get(reverse('core:home'))
    for task in list_completed_tasks:
        assertContains(response, task.title)

@pytest.fixture
def completed_task(db):
    return Task.objects.create(title='Tarefa #1', done=True)

def test_update_task_to_pending(client, completed_task):
    response = client.post(reverse('core:detail', kwargs={'task_id': completed_task.id}), data={'title': completed_task.title})
    assert not Task.objects.first().done

def test_update_task_to_pending_status_code(client, completed_task):
    response = client.post(reverse('core:detail', kwargs={'task_id': completed_task.id}), data={'title': completed_task.title})
    assert response.status_code == 302