# app/repositories/book_repo.py

from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from typing import List, Optional


class BookRepo:
    """
    Repository for all database operations related to the Book model.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_book(self, book_id: int) -> Optional[Book]:
        """Fetches a single book by its ID."""

        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_all_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """Fetches all books with pagination."""

        return self.db.query(Book).offset(skip).limit(limit).all()

    def create_book(self, book: BookCreate) -> Book:
        """Creates a new book in the database."""

        db_book = Book(**book.dict())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        """Updates an existing book."""

        db_book = self.get_book(book_id)
        if db_book:
            update_data = book_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_book, key, value)
            self.db.commit()
            self.db.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int) -> Optional[Book]:
        """Deletes a book from the database."""

        db_book = self.get_book(book_id)
        if db_book:
            self.db.delete(db_book)
            self.db.commit()
        return db_book
