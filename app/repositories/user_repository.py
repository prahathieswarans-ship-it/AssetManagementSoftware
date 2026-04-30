from database.db_init import get_connection


def create_user(user_id: str, user_name: str, email: str | None, role: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (user_id, user_name, email, role)
            VALUES (?, ?, ?, ?)
        """, (user_id, user_name, email, role))

        conn.commit()
        return cursor.lastrowid

    finally:
        conn.close()


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()


def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()


def get_user_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()

def get_user_by_user_id(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    finally:
        conn.close()
