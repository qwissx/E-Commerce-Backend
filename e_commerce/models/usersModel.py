import uuid as ui

from sqlalchemy.orm import Mapped, mapped_column

from e_commerce.connections import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
