from fastapi import APIRouter
from app.schemas.asset_schema import AssetCreate,AssetUpdate

from app.services import service_asset

router = APIRouter(prefix="/assets", tags=["Assets"])



@router.post("/")
def create_asset(asset: AssetCreate):
    return service_asset.create_asset_service(asset)

@router.get("/")
def get_assets():
    return service_asset.get_all_assets_service()

@router.get("/{asset_id}")
def get_asset(asset_id: int):
    return service_asset.get_asset_by_id_service(asset_id)

@router.put("/{asset_id}")
def update_asset(asset_id: int, asset: AssetUpdate):
    return service_asset.update_asset_service(asset_id, asset)

@router.delete("/all")
def delete_all_assets():
    return service_asset.delete_all_assets_service()

@router.delete("/{asset_id}")
def delete_asset(asset_id: int):
    return service_asset.delete_asset_service(asset_id)


