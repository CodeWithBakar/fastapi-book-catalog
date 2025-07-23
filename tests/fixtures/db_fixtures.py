import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/User/OneDrive/Desktop/book-catalog-api/tests/test_book_catalog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """
    A session-scoped fixture to create all database tables once before any tests run,
    and drop them all after all tests have completed.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db():
    """
    A function-scoped fixture that provides a transactional scope for each test.
    This pattern ensures that each test runs in isolation and any changes are
    rolled back after the test completes.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
