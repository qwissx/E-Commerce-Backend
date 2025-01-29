import uuid as ui

from pydantic import BaseModel


class SBoxCreate(BaseModel):
    user_id: ui.UUID
    good_id: ui.UUID


class SBoxDisplay(BaseModel):
    id: ui.UUID
    good_name: str
    good_type: str
