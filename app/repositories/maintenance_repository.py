from database.db_init import get_connection

def create_maintenance(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO maintenance (
                asset_id, warranty_proof, maintenance_frequency,
                date_of_maintenance, sent_for_maintenance,
                date_of_sending, date_of_returning
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.asset_id,
            data.warranty_proof,
            data.maintenance_frequency,
            data.date_of_maintenance,
            data.sent_for_maintenance,
            data.date_of_sending,
            data.date_of_returning
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        conn.close()


def get_all_maintenance():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM maintenance")
        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()


def get_maintenance_by_id(maintenance_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM maintenance WHERE id = ?
        """, (maintenance_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()

def get_maintenance_by_college_user_id(college_user_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                maintenance.id AS maintenance_id,
                maintenance.warranty_proof,
                maintenance.maintenance_frequency,
                maintenance.date_of_maintenance,
                maintenance.sent_for_maintenance,
                maintenance.date_of_sending,
                maintenance.date_of_returning,

                assets.id AS asset_id,
                assets.asset_unique_id,
                assets.description,
                assets.picture,

                users.user_id AS college_user_id,
                users.user_name,
                users.email,
                users.role

            FROM maintenance

            INNER JOIN assets
                ON maintenance.asset_id = assets.id

            INNER JOIN assignments
                ON assets.id = assignments.asset_id

            INNER JOIN users
                ON assignments.assigned_user_id = users.id

            WHERE users.user_id = ?
        """, (college_user_id,))

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()

def update_maintenance(maintenance_id: int, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE maintenance
            SET asset_id = ?, warranty_proof = ?, maintenance_frequency = ?,
                date_of_maintenance = ?, sent_for_maintenance = ?,
                date_of_sending = ?, date_of_returning = ?
            WHERE id = ?
        """, (
            data.asset_id,
            data.warranty_proof,
            data.maintenance_frequency,
            data.date_of_maintenance,
            data.sent_for_maintenance,
            data.date_of_sending,
            data.date_of_returning,
            maintenance_id
        ))

        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()


def delete_maintenance(maintenance_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM maintenance WHERE id = ?", (maintenance_id,))
        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()

def get_assets_with_maintenance():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
                       SELECT assets.id      AS asset_id,
                              assets.asset_unique_id,
                              assets.description,
                              assets.picture,

                              maintenance.id AS maintenance_id,
                              maintenance.warranty_proof,
                              maintenance.maintenance_frequency,
                              maintenance.date_of_maintenance,
                              maintenance.sent_for_maintenance,
                              maintenance.date_of_sending,
                              maintenance.date_of_returning
                       FROM assets
                                LEFT JOIN maintenance
                                          ON assets.id = maintenance.asset_id
                       """)

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()