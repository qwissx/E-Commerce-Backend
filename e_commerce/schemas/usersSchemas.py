import uuid as ui

from pydantic import BaseModel


class SUserCreate(BaseModel):
    username: str


class SUserDisplay(BaseModel):
    id: ui.UUID
    username: str
