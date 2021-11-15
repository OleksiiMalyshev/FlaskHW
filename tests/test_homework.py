import pytest
from app import app,db

@pytest.fixture
def client():
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@db:3306/flask'
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client