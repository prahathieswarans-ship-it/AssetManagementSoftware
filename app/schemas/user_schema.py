from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    user_id: str
    user_name: str
    email: Optional[str] = None
    role: Optional[str] = None