import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.db.database import get_db


from tests.fixtures.db_fixtures import *
from tests.fixtures.book_fixtures import create_book


@pytest.fixture
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
