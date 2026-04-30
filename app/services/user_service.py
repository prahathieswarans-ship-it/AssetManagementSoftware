import sqlite3
from fastapi import HTTPException
from repositories import user_repository

def create_user_service(user):
    existing = user_repository.get_user_by_user_id(user.user_id)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User ID already exists"
        )

    user_id = user_repository.create_user(
        user.user_id,
        user.user_name,
        user.email,
        user.role
    )

    return {
        "message": "User created successfully",
        "user_id": user_id
    }


def get_all_users_service():
    users = user_repository.get_all_users()

    if not users:
        return {
            "message": "No users found in the system",
            "data": []
        }

    return {
        "message": "Users retrieved successfully",
        "data": users
    }


def get_user_by_id_service(user_id: int):
    user = user_repository.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def get_user_by_college_id_service(college_user_id: str):
    user = user_repository.get_user_by_user_id(college_user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found with given college_user_id"
        )

    return user