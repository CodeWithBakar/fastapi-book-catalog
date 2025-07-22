from sqlalchemy import Column, Integer, String
from app.db.base import Base
from app.models.mixin import Timestamp


class Book(Base, Timestamp):
    """
    SQLAlchemy model for the 'books' table.
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    published_year = Column(Integer, nullable=False)
    summary = Column(String, nullable=True)
