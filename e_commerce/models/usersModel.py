from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

from e_commerce.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
