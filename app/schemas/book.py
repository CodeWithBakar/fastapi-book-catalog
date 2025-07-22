from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    """
    Base Pydantic model for a book, containing common attributes.
    """

    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    published_year: int = Field(..., gt=0, lt=3000)  # Realistic year validation
    summary: Optional[str] = None


class BookCreate(BookBase):
    """
    Pydantic model for creating a new book. Inherits from BookBase.
    """

    pass


class BookUpdate(BookBase):
    """
    Pydantic model for updating an existing book. Inherits from BookBase.
    """

    pass


class BookInDB(BookBase):
    """
    Pydantic model for representing a book as it is stored in the database.
    Includes the 'id' and timestamp fields.
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        # This allows the model to be created from ORM instances.
        from_attributes = True
