import pytest
from fastapi.testclient import TestClient
from main import app

def test_read_posts_pagination_defaults():
    """
    Automated integration test verifying that the GET /posts endpoint 
    successfully responds with correct HTTP 200 status codes.
    Uses the context manager to trigger startup lifecycle events.
    """
    # Using 'with' explicitly triggers the @app.on_event("startup") hooks
    with TestClient(app) as client:
        response = client.get("/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_get_non_existent_post_returns_404():
    """
    Validates that querying an invalid primary key correctly throws 
    a safe 404 Exception handling block instead of crashing the engine.
    """
    # Ensures the Redis cache system initializes safely before hitting the path
    with TestClient(app) as client:
        response = client.get("/posts/999999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Post not found"
