import sqlite3
from fastapi import HTTPException
from app.repositories import asset_repository,procurement_repository

def create_asset_service(asset):
    existing_asset = asset_repository.get_asset_by_unique_id(
        asset.asset_unique_id
    )

    if existing_asset:
        raise HTTPException(
            status_code=400,
            detail="Asset Unique ID already exists"
        )

    try:
        asset_id = asset_repository.create_asset(
            asset.asset_unique_id,
            asset.description,
            asset.picture
        )

        return {
            "message": "Asset created successfully",
            "asset_id": asset_id
        }

    except sqlite3.Error as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


def get_all_assets_service():
    assets = asset_repository.get_all_assets()

    if not assets:
        return {
            "message": "No assets found in the system",
            "data": []
        }

    return {
        "message": "Assets retrieved successfully",
        "data": assets
    }

def get_asset_by_id_service(asset_id: int):
    asset = asset_repository.get_asset_by_id(asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return asset


def update_asset_service(asset_id: int, asset):
    # ✅ Check if asset exists
    existing_asset = asset_repository.get_asset_by_id(asset_id)

    if not existing_asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    # ✅ Check unique constraint (avoid duplicate unique ID)
    asset_with_same_uid = asset_repository.get_asset_by_unique_id(
        asset.asset_unique_id
    )

    if asset_with_same_uid and asset_with_same_uid["id"] != asset_id:
        raise HTTPException(
            status_code=400,
            detail="Asset Unique ID already exists"
        )

    # ✅ Perform update
    rows_updated = asset_repository.update_asset(
        asset_id,
        asset.asset_unique_id,
        asset.description,
        asset.picture
    )

    if rows_updated == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {
        "message": "Asset updated successfully"
    }


def delete_asset_service(asset_id: int):
    # ✅ Check asset exists
    asset = asset_repository.get_asset_by_id(asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    # ⚠️ IMPORTANT: Check if procurement exists
    procurements = procurement_repository.get_all_procurements()

    for p in procurements:
        if p["asset_id"] == asset_id:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete asset. Procurement exists for this asset."
            )

    # ✅ Delete
    rows_deleted = asset_repository.delete_asset(asset_id)

    if rows_deleted == 0:
        raise HTTPException(status_code=400, detail="Delete failed")

    return {
        "message": "Asset deleted successfully"
    }

def delete_all_assets_service():
    # First delete child table data
    procurement_repository.delete_all_procurements()

    # Then delete parent table data
    deleted_assets = asset_repository.delete_all_assets()

    return {
        "message": "All assets and related procurements deleted successfully",
        "deleted_assets": deleted_assets
    }