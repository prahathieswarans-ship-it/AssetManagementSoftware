from fastapi import HTTPException
from repositories import assignment_repository, asset_repository, user_repository


VALID_STATUS = ["Available", "Assigned", "Under Maintenance"]


def create_assignment_service(data):
    asset = asset_repository.get_asset_by_id(data.asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    if data.status not in VALID_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid status. Use Available, Assigned, or Under Maintenance"
        )

    if data.status == "Assigned" and data.assigned_user_id is None:
        raise HTTPException(
            status_code=400,
            detail="assigned_user_id is required when status is Assigned"
        )

    if data.assigned_user_id is not None:
        user = user_repository.get_user_by_id(data.assigned_user_id)

        if not user:
            raise HTTPException(status_code=404, detail="Assigned user not found")

    active_assignment = assignment_repository.get_active_assignment_by_asset_id(
        data.asset_id
    )

    if active_assignment and data.status in ["Assigned", "Under Maintenance"]:
        raise HTTPException(
            status_code=400,
            detail="This asset already has an active assignment"
        )

    assignment_id = assignment_repository.create_assignment(data)

    return {
        "message": "Assignment created successfully",
        "assignment_id": assignment_id
    }


def get_all_assignments_service():
    assignments = assignment_repository.get_all_assignments()

    if not assignments:
        return {
            "message": "No assignments found in the system",
            "data": []
        }

    return {
        "message": "Assignments retrieved successfully",
        "data": assignments
    }


def get_assignment_by_id_service(assignment_id: int):
    assignment = assignment_repository.get_assignment_by_id(assignment_id)

    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    return assignment

def get_assignments_by_college_user_id_service(college_user_id: str):
    user = user_repository.get_user_by_user_id(college_user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found with given college_user_id"
        )

    assignments = assignment_repository.get_assignments_by_college_user_id(
        college_user_id
    )

    if not assignments:
        return {
            "message": "No assignments found for this college_user_id",
            "data": []
        }

    return {
        "message": "Assignments retrieved successfully",
        "data": assignments
    }
def get_assignments_with_asset_and_user_service():
    data = assignment_repository.get_assignments_with_asset_and_user()

    if not data:
        return {
            "message": "No assignment records found",
            "data": []
        }

    return {
        "message": "Assignments with asset and user retrieved successfully",
        "data": data
    }

def update_assignment_service(assignment_id: int, data):
    existing_assignment = assignment_repository.get_assignment_by_id(assignment_id)

    if not existing_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    asset = asset_repository.get_asset_by_id(data.asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    if data.status not in VALID_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid status. Use Available, Assigned, or Under Maintenance"
        )

    if data.status == "Assigned" and data.assigned_user_id is None:
        raise HTTPException(
            status_code=400,
            detail="assigned_user_id is required when status is Assigned"
        )

    if data.assigned_user_id is not None:
        user = user_repository.get_user_by_id(data.assigned_user_id)

        if not user:
            raise HTTPException(status_code=404, detail="Assigned user not found")

    active_assignment = assignment_repository.get_active_assignment_by_asset_id(
        data.asset_id
    )

    if (
        active_assignment
        and active_assignment["id"] != assignment_id
        and data.status in ["Assigned", "Under Maintenance"]
    ):
        raise HTTPException(
            status_code=400,
            detail="This asset already has another active assignment"
        )

    rows_updated = assignment_repository.update_assignment(assignment_id, data)

    if rows_updated == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {
        "message": "Assignment updated successfully"
    }


def delete_assignment_service(assignment_id: int):
    assignment = assignment_repository.get_assignment_by_id(assignment_id)

    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    assignment_repository.delete_assignment(assignment_id)

    return {
        "message": "Assignment deleted successfully"
    }