import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_list(client):
    response = client.get(reverse('post'))
    assert response.status_code == 200
