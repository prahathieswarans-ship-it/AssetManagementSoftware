from fastapi import APIRouter
from schemas.user_schema import UserCreate
from services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserCreate):
    return user_service.create_user_service(user)


@router.get("/all")
def get_all_users():
    return user_service.get_all_users_service()

@router.get("/by-college-id/{college_user_id}")
def get_user_by_college_id(college_user_id: str):
    return user_service.get_user_by_college_id_service(college_user_id)

@router.get("/{user_id}")
def get_user(user_id: int):
    return user_service.get_user_by_id_service(user_id)