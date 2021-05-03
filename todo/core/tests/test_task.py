from django.urls import reverse

def test_home_status_code(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200