from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.book_service import BookService
from app.schemas.book import BookCreate, BookUpdate, BookInDB
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.post("/", response_model=BookInDB, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Create a new book."""
    service = BookService(db)
    return service.create_book(book)


@router.get("/", response_model=List[BookInDB])
async def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all books (asynchronously)."""
    service = BookService(db)
    return await service.get_all_books(skip, limit)


@router.get("/{book_id}", response_model=BookInDB)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Retrieve a single book by its ID."""
    service = BookService(db)
    db_book = service.get_book(book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put("/{book_id}", response_model=BookInDB)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book."""
    service = BookService(db)
    db_book = service.update_book(book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/{book_id}", response_model=BookInDB)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book."""
    service = BookService(db)
    db_book = service.delete_book(book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
