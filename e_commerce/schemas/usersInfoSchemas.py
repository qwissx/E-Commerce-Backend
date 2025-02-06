from pydantic import BaseModel, EmailStr, UUID4


class SUserInfoCreate(BaseModel):
    email: EmailStr | None = None
    phone_number: str | None = None


class SUserInfoUpdate(BaseModel):
    email: EmailStr | None = None
    phone_number: str | None = None


class SUserInfoDisplay(BaseModel):
    id: UUID4
    username: str
    password: str
    email: EmailStr | None = None
    phone_number: str | None = None