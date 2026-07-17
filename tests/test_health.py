from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_response_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_url_rejects_invalid_url():
    response = client.post(
        "/urls",
        json={"original_url": "not-a-url"}
    )

    assert response.status_code == 422

def test_create_url_returns_short_code():
    response = client.post(
        "/urls",
        json={"original_url": "https://example.com"}
    )

    body = response.json()

    assert response.status_code == 201
    assert "short_code" in body
    assert len(body["short_code"]) == 6
    assert body["short_code"].isalnum()

def test_short_code_redirects_to_original_url():
    original_url = "https://example.com/"

    create_response = client.post(
        "/urls",
        json={"original_url": original_url}
    )
    short_code = create_response.json()["short_code"]

    redirect_response = client.get(
        f"/{short_code}",
        follow_redirects=False
    )

    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"] == original_url

def test_unknown_short_code_returns_not_found():
    response = client.get("/unknown-code", follow_redirects=False)

    assert response.status_code == 404
    assert response.json() == {"detail": "Short URL not found"}