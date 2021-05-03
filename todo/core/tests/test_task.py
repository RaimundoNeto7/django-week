from django.urls import reverse
from pytest_django.asserts import assertContains

def test_home_status_code(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200

def test_contains_form(client):
    response = client.get(reverse('core:home'))
    assertContains(response, '<form')

def test_contains_submit_btn(client):
    response = client.get(reverse('core:home'))
    assertContains(response, '<button type="submit"')