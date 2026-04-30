from fastapi import APIRouter
from schemas.assignment_schema import AssignmentCreate, AssignmentUpdate
from services import assignment_service

router = APIRouter(prefix="/assignments", tags=["Assignments"])


@router.post("/")
def create_assignment(data: AssignmentCreate):
    return assignment_service.create_assignment_service(data)

@router.get("/all")
def get_all_assignments():
    return assignment_service.get_all_assignments_service()
@router.get("/with-asset-user")
def get_assignments_with_asset_and_user():
    return assignment_service.get_assignments_with_asset_and_user_service()

@router.get("/by-college-user-id/{college_user_id}")
def get_assignments_by_college_user_id(college_user_id: str):
    return assignment_service.get_assignments_by_college_user_id_service(
        college_user_id
    )
@router.get("/{assignment_id}")
def get_assignment(assignment_id: int):
    return assignment_service.get_assignment_by_id_service(assignment_id)


@router.put("/{assignment_id}")
def update_assignment(assignment_id: int, data: AssignmentUpdate):
    return assignment_service.update_assignment_service(assignment_id, data)


@router.delete("/{assignment_id}")
def delete_assignment(assignment_id: int):
    return assignment_service.delete_assignment_service(assignment_id)