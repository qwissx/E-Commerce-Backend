import uuid as ui

from pydantic import BaseModel


class SGoodCreate(BaseModel):
    name: str
    type: str


class SGoodDisplay(BaseModel):
    id: ui.UUID
    name: str
    type: str
