from sqlalchemy import Column, String, Integer, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable

from src.database import Base

__all__ = [
    "User"
]


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, unique=True)  # type: ignore
    username: str = Column(String(length=32), nullable=False)
    email: str = Column(String(length=64), nullable=False)  # type: ignore
    hashed_password: str = Column(String(length=1024), nullable=False)  # type: ignore
    is_active = Column(Boolean, server_default='true', nullable=False)  # type: ignore
    is_superuser = Column(Boolean, server_default='false', nullable=False)  # type: ignore
    is_verified = Column(Boolean, server_default='false', nullable=False)  # type: ignore