from pydantic import BaseModel
from typing import Optional


class MaintenanceCreate(BaseModel):
    asset_id: int
    warranty_proof: Optional[str] = None
    maintenance_frequency: Optional[str] = None
    date_of_maintenance: Optional[str] = None
    sent_for_maintenance: int = 0
    date_of_sending: Optional[str] = None
    date_of_returning: Optional[str] = None


class MaintenanceUpdate(BaseModel):
    asset_id: int
    warranty_proof: Optional[str] = None
    maintenance_frequency: Optional[str] = None
    date_of_maintenance: Optional[str] = None
    sent_for_maintenance: int = 0
    date_of_sending: Optional[str] = None
    date_of_returning: Optional[str] = None