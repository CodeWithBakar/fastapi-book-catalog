from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite.
# The database file will be created in the same directory.
SQLALCHEMY_DATABASE_URL = (
    "sqlite:///C:/Users/User/OneDrive/Desktop/book-catalog-api/app/db/book_catalog.db"
)

# Create the SQLAlchemy engine.
# connect_args is needed only for SQLite to allow multithreaded access.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class, which will be a factory for new Session objects.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency function to get a database session.
    It ensures the database connection is always closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
