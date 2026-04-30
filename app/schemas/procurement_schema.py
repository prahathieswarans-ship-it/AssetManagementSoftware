from pydantic import BaseModel, Field
from typing import Optional


class ProcurementCreate(BaseModel):
    asset_id: int
    units: int
    cost: int
    purchase_date: str
    invoice_image: Optional[str] = None

class ProcurementResponse(BaseModel):
    id: int
    asset_id: int
    units: int
    cost: int
    purchase_date: str
    invoice_image: Optional[str] = None



class ProcurementUpdate(BaseModel):
    asset_id: int
    units: int = Field(..., gt=0)
    cost: int = Field(..., gt=0)
    purchase_date: str
    invoice_image: Optional[str] = None

    
class ProcurementCreate(BaseModel):
    asset_id: int
    units: int = Field(..., gt=0)
    cost: int = Field(..., gt=0)
    purchase_date: str
    invoice_image: Optional[str] = None