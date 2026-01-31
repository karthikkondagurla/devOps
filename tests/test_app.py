import pytest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the root endpoint returns a success message."""
    rv = client.get('/')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert "Hello, World!" in json_data["message"]
    assert json_data["status"] == "success"

def test_health_check(client):
    """Test the health check endpoint."""
    rv = client.get('/health')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data["status"] == "healthy"
