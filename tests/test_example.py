import pytest
from app import app

def test_example():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

