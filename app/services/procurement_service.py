from fastapi import HTTPException
from repositories import procurement_repository
from repositories import asset_repository


def create_procurement_service(procurement):
    # 1. Check asset exists
    asset = asset_repository.get_asset_by_id(procurement.asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found. Cannot create procurement."
        )

    # 2. Create procurement
    procurement_id = procurement_repository.create_procurement(
        procurement.asset_id,
        procurement.units,
        procurement.cost,
        procurement.purchase_date,
        procurement.invoice_image
    )

    return {
        "message": "Procurement created successfully",
        "procurement_id": procurement_id
    }


def get_all_procurements_service():
    procurements = procurement_repository.get_all_procurements()

    if not procurements:
        return {
            "message": "No procurements found in the system",
            "data": []
        }

    return {
        "message": "Procurements retrieved successfully",
        "data": procurements
    }


def get_assets_with_procurements_service():
    return procurement_repository.get_assets_with_procurements()

def get_procurement_by_id_service(procurement_id: int):
    procurement = procurement_repository.get_procurement_by_id(procurement_id)

    if not procurement:
        raise HTTPException(
            status_code=404,
            detail="Procurement not found"
        )
    return procurement


def update_procurement_service(procurement_id: int, procurement):
    existing_procurement = procurement_repository.get_procurement_by_id(procurement_id)

    if not existing_procurement:
        raise HTTPException(
            status_code=404,
            detail="Procurement not found"
        )

    asset = asset_repository.get_asset_by_id(procurement.asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found. Cannot update procurement."
        )

    rows_updated = procurement_repository.update_procurement(
        procurement_id,
        procurement.asset_id,
        procurement.units,
        procurement.cost,
        procurement.purchase_date,
        procurement.invoice_image
    )

    if rows_updated == 0:
        raise HTTPException(
            status_code=400,
            detail="Update failed"
        )

    return {
        "message": "Procurement updated successfully"
    }

def delete_procurement_service(procurement_id: int):
    procurement = procurement_repository.get_procurement_by_id(procurement_id)

    if not procurement:
        raise HTTPException(
            status_code=404,
            detail="Procurement not found"
        )

    rows_deleted = procurement_repository.delete_procurement(procurement_id)

    if rows_deleted == 0:
        raise HTTPException(status_code=400, detail="Delete failed")

    return {
        "message": "Procurement deleted successfully"
    }

def delete_all_procurements_service():
    deleted_count = procurement_repository.delete_all_procurements()

    return {
        "message": "All procurements deleted successfully",
        "deleted_procurements": deleted_count
    }

