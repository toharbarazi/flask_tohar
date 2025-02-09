import sys
import os

# הוסף את הנתיב של תיקיית הבסיס ל-Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# עכשיו ייבא את app
import pytest
from app import app

def test_example():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

