from django.urls import reverse
from pytest_django.asserts import assertContains
from todo.core.models import Task

def test_home_status_code(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200

def test_contains_form(client):
    response = client.get(reverse('core:home'))
    assertContains(response, '<form')

def test_contains_submit_btn(client):
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
