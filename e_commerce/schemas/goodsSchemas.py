from pydantic import BaseModel, UUID4


class SGoodCreate(BaseModel):
    name: str
    type: str


class SGoodDisplay(BaseModel):
    id: UUID4
    name: str
    type: str
