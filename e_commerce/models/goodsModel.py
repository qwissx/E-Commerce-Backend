import uuid as ui

from sqlalchemy.orm import Mapped, mapped_column

from e_commerce.database import Base


class Goods(Base):
    __tablename__ = "goods"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    