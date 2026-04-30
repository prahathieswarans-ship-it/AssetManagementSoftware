from database.db_init import get_connection


def create_procurement(asset_id: int, units: int, cost: int, purchase_date: str, invoice_image: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO procurements (
                asset_id, units, cost, purchase_date, invoice_image
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            asset_id,
            units,
            cost,
            purchase_date,
            invoice_image
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        conn.close()


def get_all_procurements():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM procurements")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()

def get_assets_with_procurements():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT 
                assets.id AS asset_id,
                assets.asset_unique_id,
                assets.description,
                assets.picture,

                procurements.id AS procurement_id,
                procurements.units,
                procurements.cost,
                procurements.purchase_date,
                procurements.invoice_image
            FROM assets
            INNER JOIN procurements
                ON assets.id = procurements.asset_id
        """)

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    finally:
        conn.close()
        

def get_procurement_by_id(procurement_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM procurements
            WHERE id = ?
        """, (procurement_id,))

        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()

def update_procurement(
    procurement_id: int,
    asset_id: int,
    units: int,
    cost: int,
    purchase_date: str,
    invoice_image: str | None
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE procurements
            SET asset_id = ?,
                units = ?,
                cost = ?,
                purchase_date = ?,
                invoice_image = ?
            WHERE id = ?
        """, (
            asset_id,
            units,
            cost,
            purchase_date,
            invoice_image,
            procurement_id
        ))

        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()


def delete_procurement(procurement_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM procurements
            WHERE id = ?
        """, (procurement_id,))

        conn.commit()

        return cursor.rowcount

    finally:
        conn.close()

def delete_all_procurements():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM procurements")
        conn.commit()
        return cursor.rowcount

    finally:
        conn.close()
