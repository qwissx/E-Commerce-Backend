from pydantic import BaseModel, EmailStr, UUID4


class SUserInfoCreate(BaseModel):
    user_id: UUID4
    email: EmailStr | None = None
    phone_number: str | None = None


class SUserInfoUpdate(BaseModel):
    email: EmailStr | None = None
    phone_number: str | None = None


class SUserInfoDisplay(BaseModel):
    id: UUID4
    email: EmailStr | None = None
    phone_number: str | None = None
