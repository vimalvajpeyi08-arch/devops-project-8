import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_trigger_alert(client):
    rv = client.post('/alert', json={"title": "Test Alert", "severity": "HIGH"})
    assert rv.status_code == 201
    assert b"INC-101" in rv.data