import sqlite3
from app.config import DB_PATH




def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def create_assets_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_unique_id TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            picture TEXT
        )
    """)

    conn.commit()
    conn.close()

def create_procurements_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS procurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER NOT NULL,
            units INTEGER NOT NULL,
            cost INTEGER NOT NULL,
            purchase_date TEXT NOT NULL,
            invoice_image TEXT,
            FOREIGN KEY (asset_id) REFERENCES assets(id)
        )
    """)

    conn.commit()
    conn.close()

def create_maintenance_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER NOT NULL,
            warranty_proof TEXT,
            maintenance_frequency TEXT,
            date_of_maintenance TEXT,
            sent_for_maintenance INTEGER DEFAULT 0,
            date_of_sending TEXT,
            date_of_returning TEXT,

            FOREIGN KEY (asset_id) REFERENCES assets(id)
        )
    """)

    conn.commit()
    conn.close()

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL UNIQUE,
        user_name TEXT NOT NULL,
        email TEXT UNIQUE,
        role TEXT
    );""")

    conn.commit()
    conn.close()


def create_assignments_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER NOT NULL,

            location TEXT NOT NULL,
            assigned_user_id INTEGER,

            status TEXT NOT NULL,

            assigned_date TEXT,
            return_date TEXT,

            FOREIGN KEY (asset_id) REFERENCES assets(id),
            FOREIGN KEY (assigned_user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()

