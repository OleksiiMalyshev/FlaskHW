from tests.conftest import client, todos
import json, jsonify


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.get("/todos", json=todos)
    assert response.status_code == 200

