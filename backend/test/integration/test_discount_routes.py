import pytest
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_calculate_discount_endpoint():
    payload = {
        "original_price": 100.0,
        "discount_percentage": 15.0,
        "cupom": "EXTRA10"
    }
    response = client.post("/api/discounts/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["original_price"] == 100.0
    assert data["discount_percentage"] == 25.0
    assert data["final_price"] == 75.0

