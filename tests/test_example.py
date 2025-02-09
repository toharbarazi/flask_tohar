import sys
import os

# הוסף את הנתיב של תיקיית הבסיס ל-Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# עכשיו ייבא את app
import pytest
from app import app

def test_example():
    # הגדרת מצב הבדיקות עבור האפליקציה
    app.config['TESTING'] = True

    # יצירת לקוח בדיקה
    client = app.test_client()

    # שליחת בקשה לנתיב '/'
    response = client.get('/')

    # בדיקה שהסטטוס שהתקבל הוא 200
    assert response.status_code == 200

