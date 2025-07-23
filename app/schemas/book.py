from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    """
    Base Pydantic model for a book, containing common attributes.
    """

    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    published_year: int = Field(..., gt=0, lt=3000)
    summary: Optional[str] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookInDB(BookBase):
    """
    Pydantic model for representing a book as it is stored in the database.
    """

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
