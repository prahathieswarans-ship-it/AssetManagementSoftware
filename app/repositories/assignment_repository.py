from database.db_init import get_connection


def create_assignment(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO assignments (
                asset_id, location, assigned_user_id,
                status, assigned_date, return_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.asset_id,
            data.location,
            data.assigned_user_id,
            data.status,
            data.assigned_date,
            data.return_date
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        conn.close()


def get_all_assignments():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM assignments")
        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()


def get_assignment_by_id(assignment_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM assignments WHERE id = ?", (assignment_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()


def get_active_assignment_by_asset_id(asset_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM assignments
            WHERE asset_id = ?
            AND return_date IS NULL
            AND status IN ('Assigned', 'Under Maintenance')
        """, (asset_id,))

        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()

def get_assignments_by_college_user_id(college_user_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                assignments.id AS assignment_id,
                assignments.location,
                assignments.status,
                assignments.assigned_date,
                assignments.return_date,

                assets.id AS asset_id,
                assets.asset_unique_id,
                assets.description,
                assets.picture,

                users.id AS user_db_id,
                users.user_id AS college_user_id,
                users.user_name,
                users.email,
                users.role

            FROM assignments

            INNER JOIN assets
                ON assignments.asset_id = assets.id

            INNER JOIN users
                ON assignments.assigned_user_id = users.id

            WHERE users.user_id = ?
        """, (college_user_id,))

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()

def get_assignments_with_asset_and_user():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                assignments.id AS assignment_id,
                assignments.location,
                assignments.status,
                assignments.assigned_date,
                assignments.return_date,

                assets.id AS asset_id,
                assets.asset_unique_id,
                assets.description,
                assets.picture,

                users.id AS user_db_id,
                users.user_id AS college_user_id,
                users.user_name,
                users.email,
                users.role

            FROM assignments

            INNER JOIN assets
                ON assignments.asset_id = assets.id

            LEFT JOIN users
                ON assignments.assigned_user_id = users.id
        """)

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()

def update_assignment(assignment_id: int, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE assignments
            SET asset_id = ?,
                location = ?,
                assigned_user_id = ?,
                status = ?,
                assigned_date = ?,
                return_date = ?
            WHERE id = ?
        """, (
            data.asset_id,
            data.location,
            data.assigned_user_id,
            data.status,
            data.assigned_date,
            data.return_date,
            assignment_id
        ))

        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()


def delete_assignment(assignment_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM assignments WHERE id = ?", (assignment_id,))
        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()