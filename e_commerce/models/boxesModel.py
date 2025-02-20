import uuid as ui

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from e_commerce.connections import Base


class Boxes(Base):
    __tablename__ = "boxes"

    id: Mapped[ui.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[ui.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    good_id: Mapped[ui.UUID] = mapped_column(ForeignKey("goods.id"), nullable=False)
    