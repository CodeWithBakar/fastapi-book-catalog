import time
from datetime import datetime
from app.services.book_service import BookService
from app.schemas.book import BookCreate, BookUpdate


class TestBookService:
    """Test suite for the Book Service layer."""

    def test_create_book(self, db):
        """Test creating a book via the service."""
        service = BookService(db)
        book_data = BookCreate(
            title="Service Test Book", author="Service Author", published_year=2023
        )
        book = service.create_book(book_data)
        assert book.title == "Service Test Book"  # type: ignore
        assert book.id is not None
        assert isinstance(book.created_at, datetime)
        assert isinstance(book.updated_at, datetime)

    def test_get_book(self, db, create_book):
        """Test retrieving a book."""
        created_book = create_book(
            title="Another Service Book", author="Another Author"
        )
        service = BookService(db)

        retrieved_book = service.get_book(created_book.id)
        assert retrieved_book is not None
        assert retrieved_book.id == created_book.id
        assert retrieved_book.author == "Another Author"  # type: ignore

    def test_update_book(self, db, create_book):
        """Test updating a book and verifying the onupdate timestamp."""
        book = create_book(title="Original Title")
        original_updated_at = book.updated_at
        service = BookService(db)

        # Wait a moment to ensure the timestamp will be different
        time.sleep(0.01)

        update_data = BookUpdate(
            title="Updated Title", author="Updated Author", published_year=2021
        )
        updated_book = service.update_book(book.id, update_data)

        assert updated_book is not None
        assert updated_book.title == "Updated Title"  # type: ignore
        assert updated_book.published_year == 2021  # type: ignore
        assert updated_book.updated_at > original_updated_at

    def test_delete_book(self, db, create_book):
        """Test deleting a book."""
        book = create_book(title="To Be Deleted")
        service = BookService(db)

        deleted_book = service.delete_book(book.id)
        assert deleted_book is not None

        retrieved_book = service.get_book(book.id)
        assert retrieved_book is None
