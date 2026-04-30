from app.database.db_init import get_connection

def create_asset(asset_unique_id: str, description: str, picture: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO assets (asset_unique_id, description, picture)
            VALUES (?, ?, ?)
        """, (
            asset_unique_id,
            description,
            picture
        ))

        conn.commit()

        return cursor.lastrowid

    finally:
        conn.close()


def get_all_assets():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM assets")
        assets = cursor.fetchall()

        return [dict(asset) for asset in assets]

    finally:
        conn.close()


def get_asset_by_id(asset_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM assets
            WHERE id = ?
        """, (asset_id,))

        asset = cursor.fetchone()

        if asset:
            return dict(asset)

        return None

    finally:
        conn.close()


def get_asset_by_unique_id(asset_unique_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM assets
            WHERE asset_unique_id = ?
        """, (asset_unique_id,))

        asset = cursor.fetchone()

        if asset:
            return dict(asset)

        return None

    finally:
        conn.close()

def update_asset(asset_id: int, asset_unique_id: str, description: str, picture: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE assets
            SET asset_unique_id = ?, description = ?, picture = ?
            WHERE id = ?
        """, (
            asset_unique_id,
            description,
            picture,
            asset_id
        ))

        conn.commit()

        return cursor.rowcount  # number of rows updated

    finally:
        conn.close()

def delete_asset(asset_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM assets
            WHERE id = ?
        """, (asset_id,))

        conn.commit()

        return cursor.rowcount  # rows deleted

    finally:
        conn.close()

def delete_all_assets():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM assets")
        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()

        