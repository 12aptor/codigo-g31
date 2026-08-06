import pytest
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status

faker = Faker()

API_PREFIX = '/api/v1'

@pytest.fixture
def client_with_auth():
    client = APIClient()

    register_payload = {
        "username": faker.user_name(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "password": faker.password(),
        "phone": faker.phone_number(),
        "address": faker.address(),
    }
    register_response = client.post(f'{API_PREFIX}/auth/register/', register_payload, format='json')
    assert register_response.status_code == status.HTTP_201_CREATED

    login_payload = {
        'username': register_payload['username'],
        'password': register_payload['password']
    }
    login_response = client.post(f'{API_PREFIX}/auth/login/', login_payload, format='json')
    login_json = login_response.data
    assert login_response.status_code == status.HTTP_200_OK

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_json['access']}')
    return client

@pytest.mark.django_db
def test_create_workspace(client_with_auth):
    payload = {
        'name': faker.name(),
        'slug': faker.slug(),
    }
    response = client_with_auth.post(f'{API_PREFIX}/workspaces/', payload, format='json')
    response_json = response.data
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response_json, dict)
    assert isinstance(response_json['id'], int)
    assert isinstance(response_json['members'], list)