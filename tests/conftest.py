import pytest
from app import app
from flask import Flask


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def todos():
    yield {
        "title": "test_title",
        "text": "test_text"
    }