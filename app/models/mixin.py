from sqlalchemy import Column, TIMESTAMP, func
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    """
    A mixin that adds timezone-aware created_at and updated_at columns.
    """

    created_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
