from pydantic import BaseModel, UUID4


class SUserCreate(BaseModel):
    username: str
    password: str


class SUserDisplay(BaseModel):
    id: UUID4
    username: str
    password: str


class SUserAuth(BaseModel):
    username: str
    password: str