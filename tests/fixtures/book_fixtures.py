# tests/fixtures/book_fixtures.py

import pytest
from app.models.book import Book


@pytest.fixture
def create_book(db):
    """
    A factory fixture to create book instances for testing.
    This makes setting up test data clean and reusable.
    """

    def _create_book(
        title: str = "Default Test Book",
        author: str = "Default Author",
        published_year: int = 2023,
        summary: str = "A default summary.",
    ) -> Book:
        book = Book(
            title=title, author=author, published_year=published_year, summary=summary
        )
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    return _create_book
