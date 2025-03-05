import uuid as ui

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from e_commerce.connections import Base


class UsersInfo(Base):
    __tablename__ = "users_info"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[ui.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    email: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)

    user = relationship("Users", back_populates="info")

    def __str__(self):
        return f"email '{self.email}', phone number '{self.phone_number}'"