import pytest
from app import app, db
import json


@pytest.fixture
def client():
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@db:3306/flask"
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client


def test_get_plant(client):
    response = client.get("/api/v1/plants")
    assert response.status_code == 200


def test_get_plant_by_id(client):
    response = client.get("/api/v1/plants/3")
    assert response.status_code == 200
    assert json.loads(response.data)['name'] == 'Plant1'

def test_plant_delete(client):
    response = client.delete("/api/v1/plants/3")
    assert response.status_code == 204

def test_get_employee(client):
    response = client.get("/api/v1/employees")
    assert response.status_code == 200


def test_get_employee_by_id(client):
    response = client.get("/api/v1/employees/1")
    assert response.status_code == 200
    assert json.loads(response.data)['name'] == 'Petro2'

def test_employee_delete(client):
    response = client.delete("/api/v1/employees/1")
    assert response.status_code == 204

def test_get_salon(client):
    response = client.get("/api/v1/salons")
    assert response.status_code == 200

def test_get_salon_by_id(client):
    response = client.get("/api/v1/salons/1")
    assert response.status_code == 200
    assert json.loads(response.data)['name'] == 'Salon1'

def test_salon_delete(client):
    response = client.delete("/api/v1/salons/1")
    assert response.status_code == 204
