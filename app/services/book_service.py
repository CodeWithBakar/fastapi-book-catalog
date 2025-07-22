from sqlalchemy.orm import Session
from app.repositories.book_repo import BookRepo
from app.schemas.book import BookCreate, BookUpdate
from app.models.book import Book
from typing import List, Optional


class BookService:
    """
    Service layer containing the business logic for managing books.
    """

    def __init__(self, db: Session):
        self.repo = BookRepo(db)

    def get_book(self, book_id: int) -> Optional[Book]:
        """Retrieves a single book by its ID."""
        return self.repo.get_book(book_id)

    async def get_all_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """Asynchronously retrieves all books."""
        # In a real-world scenario with an async database driver (like asyncpg),
        # this is where you would use `await`. With SQLite, the async benefit
        # is primarily in allowing other non-blocking tasks to run.
        return self.repo.get_all_books(skip, limit)

    def create_book(self, book: BookCreate) -> Book:
        """Creates a new book."""
        return self.repo.create_book(book)

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        """Updates an existing book."""
        return self.repo.update_book(book_id, book_update)

    def delete_book(self, book_id: int) -> Optional[Book]:
        """Deletes a book."""
        return self.repo.delete_book(book_id)
