from pydantic import BaseModel, UUID4


class SBoxCreate(BaseModel):
    user_id: UUID4
    good_id: UUID4


class SBoxDisplay(BaseModel):
    id: UUID4
    good_name: str
    good_type: str
