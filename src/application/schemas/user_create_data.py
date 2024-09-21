from typing import Optional, Self

from pydantic import BaseModel, EmailStr, Field

from .user_input_data import UserInputData

__all__ = [
    "UserCreateData"
]


class UserCreateData(BaseModel):
    username: str = Field(min_length=3, max_length=255)
    email: EmailStr = Field(min_length=3, max_length=320)
    hashed_password: bytes
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    @classmethod
    def get_from_register_data(cls, user_register_data: UserInputData, hashed_password: bytes) -> Self:
        return UserCreateData(
            username=user_register_data.username,
            email=user_register_data.email,
            hashed_password=hashed_password,
            is_active=user_register_data.is_active,
            is_superuser=user_register_data.is_superuser,
            is_verified=user_register_data.is_verified
        )
