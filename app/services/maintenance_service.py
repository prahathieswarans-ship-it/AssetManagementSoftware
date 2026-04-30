from fastapi import HTTPException
from repositories import maintenance_repository, asset_repository,user_repository

def create_maintenance_service(data):
    asset = asset_repository.get_asset_by_id(data.asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    maintenance_id = maintenance_repository.create_maintenance(data)

    return {
        "message": "Maintenance record created",
        "maintenance_id": maintenance_id
    }

def get_all_maintenance_service():
    records = maintenance_repository.get_all_maintenance()

    if not records:
        return {
            "message": "No maintenance records found in the system",
            "data": []
        }

    return {
        "message": "Maintenance records retrieved successfully",
        "data": records
    }


def get_maintenance_by_id_service(maintenance_id: int):
    record = maintenance_repository.get_maintenance_by_id(maintenance_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    return record

def get_maintenance_by_college_user_id_service(college_user_id: str):
    # ✅ Check user exists
    user = user_repository.get_user_by_user_id(college_user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found with given college_user_id"
        )

    data = maintenance_repository.get_maintenance_by_college_user_id(
        college_user_id
    )

    if not data:
        return {
            "message": "No maintenance records found for this user",
            "data": []
        }

    return {
        "message": "Maintenance records retrieved successfully",
        "data": data
    }

def update_maintenance_service(maintenance_id: int, data):
    existing = maintenance_repository.get_maintenance_by_id(maintenance_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Record not found")

    asset = asset_repository.get_asset_by_id(data.asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    updated = maintenance_repository.update_maintenance(maintenance_id, data)

    if updated == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "Maintenance updated successfully"}


def delete_maintenance_service(maintenance_id: int):
    record = maintenance_repository.get_maintenance_by_id(maintenance_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    maintenance_repository.delete_maintenance(maintenance_id)

    return {"message": "Maintenance deleted successfully"}



def get_assets_with_maintenance_service():
    # ✅ Step 1: Check if any assets exist
    assets = asset_repository.get_all_assets()

    if not assets:
        raise HTTPException(
            status_code=404,
            detail="No assets found in the system"
        )

    # ✅ Step 2: Fetch joined data
    data = maintenance_repository.get_assets_with_maintenance()

    # ⚠️ Step 3: Handle case where assets exist but no maintenance records
    if not data:
        return {
            "message": "Assets exist but no maintenance records found",
            "data": []
        }

    return data