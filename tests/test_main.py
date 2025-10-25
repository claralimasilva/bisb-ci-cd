import json
from app.main import app

def test_health_endpoint_returns_ok():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "a Archon Systems manda alora"}


def test_average_ticket_endpoint_success():
    client = app.test_client()
    payload = {
        "services": [
            {"price": 120.0},
            {"price": 80.0},
            {"price": 100.0},
        ]
    }
    response = client.post(
        "/metrics/average-ticket",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 200
    data = response.get_json()
    # média = (120 + 80 + 100) / 3 = 300 / 3 = 100
    assert data["average_ticket"] == 100.0


def test_average_ticket_endpoint_error_on_empty_list():
    client = app.test_client()
    payload = {"services": []}

    response = client.post(
        "/metrics/average-ticket",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data