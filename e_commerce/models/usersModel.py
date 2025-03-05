import uuid as ui

from sqlalchemy.orm import Mapped, mapped_column, relationship

from e_commerce.connections import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    info = relationship("UsersInfo", back_populates="user")

    def __str__(self):
        return f"user {self.username}"
