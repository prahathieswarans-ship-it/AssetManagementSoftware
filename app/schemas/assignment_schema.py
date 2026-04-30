from pydantic import BaseModel
from typing import Optional


class AssignmentCreate(BaseModel):
    asset_id: int
    location: str
    assigned_user_id: Optional[int] = None
    status: str
    assigned_date: Optional[str] = None
    return_date: Optional[str] = None


class AssignmentUpdate(BaseModel):
    asset_id: int
    location: str
    assigned_user_id: Optional[int] = None
    status: str
    assigned_date: Optional[str] = None
    return_date: Optional[str] = None