from typing import Optional

from pydantic import BaseModel


class SUserCreate(BaseModel):
    username: str


class SUserDisplay(BaseModel):
    id: int
    username: str


class SUserDelete(BaseModel):
    id: Optional[int]
    username: Optional[str]
