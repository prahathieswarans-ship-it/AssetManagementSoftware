from fastapi import APIRouter
from schemas.maintenance_schema import MaintenanceCreate, MaintenanceUpdate
from services import maintenance_service

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])

@router.post("/")
def create(data: MaintenanceCreate):
    return maintenance_service.create_maintenance_service(data)
@router.get("/all")
def get_all():
    return maintenance_service.get_all_maintenance_service()
@router.get("/with-assets")
def get_assets_with_maintenance():
    return maintenance_service.get_assets_with_maintenance_service()
@router.get("/by-college-user-id/{college_user_id}")
def get_maintenance_by_college_user_id(college_user_id: str):
    return maintenance_service.get_maintenance_by_college_user_id_service(
        college_user_id
    )
@router.get("/{maintenance_id}")
def get_one(maintenance_id: int):
    return maintenance_service.get_maintenance_by_id_service(maintenance_id)
@router.put("/{maintenance_id}")
def update(maintenance_id: int, data: MaintenanceUpdate):
    return maintenance_service.update_maintenance_service(maintenance_id, data)
@router.delete("/{maintenance_id}")
def delete(maintenance_id: int):
    return maintenance_service.delete_maintenance_service(maintenance_id)