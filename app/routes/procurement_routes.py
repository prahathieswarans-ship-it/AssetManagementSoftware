from fastapi import APIRouter

from schemas.procurement_schema import ProcurementCreate,ProcurementUpdate
from services import procurement_service

router = APIRouter(prefix="/procurements", tags=["Procurements"])


@router.post("/")
def create_procurement(procurement: ProcurementCreate):
    return procurement_service.create_procurement_service(procurement)


@router.get("/all")
def get_procurements():
    return procurement_service.get_all_procurements_service()

@router.get("/with-assets")
def get_assets_with_procurements():
    return procurement_service.get_assets_with_procurements_service()


@router.get("/{procurement_id}")
def get_procurement(procurement_id: int):
    return procurement_service.get_procurement_by_id_service(procurement_id)

@router.put("/{procurement_id}")
def update_procurement(procurement_id: int, procurement: ProcurementUpdate):
    return procurement_service.update_procurement_service(
        procurement_id,
        procurement
    )

@router.delete("/all")
def delete_all_procurements():
    return procurement_service.delete_all_procurements_service()

@router.delete("/{procurement_id}")
def delete_procurement(procurement_id: int):
    return procurement_service.delete_procurement_service(procurement_id)

