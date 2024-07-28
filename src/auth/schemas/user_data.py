from typing import Optional

from pydantic import BaseModel, EmailStr, Field

__all__ = [
    "UserData"
]


class UserData(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=255)
    email: EmailStr = Field(min_length=3, max_length=320)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
