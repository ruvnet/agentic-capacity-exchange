import pytest
from central_server.app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_startup_event():
    response = client.get("/")
    assert response.status_code == 200
    assert "Starting up the central server..." in response.text

def test_shutdown_event():
    # This is a placeholder test for the shutdown event
    # In a real application, you would simulate a shutdown event and test the response
    assert True
