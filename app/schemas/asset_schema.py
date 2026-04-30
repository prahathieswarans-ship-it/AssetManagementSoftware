from pydantic import BaseModel
class AssetCreate(BaseModel):

    asset_unique_id: str
    description: str
    picture: str | None = None

class AssetUpdate(BaseModel):
    asset_unique_id: str
    description: str
    picture: str | None = None