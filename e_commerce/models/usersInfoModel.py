import uuid as ui

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from e_commerce.connections import Base


class UsersInfo(Base):
    __tablename__ = "users_info"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[ui.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    email: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)

