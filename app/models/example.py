from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, func, String, text
from sqlalchemy.dialects.postgresql import UUID as DB_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.schemas.example import ExampleType


class Example(Base):
    __tablename__ = 'examples'

    id: Mapped[UUID] = mapped_column(DB_UUID, primary_key=True, server_default=text('gen_random_uuid()'))  # noqa: A003
    name: Mapped[str] = mapped_column(String(256), nullable=False, unique=True, index=True)
    description: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    example_type: Mapped[ExampleType] = mapped_column(Enum(ExampleType, native_enum=False, validate_strings=True,
                                                        values_callable=lambda x: [i.value for i in x]),
                                                   nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(),
                                                 nullable=False)
