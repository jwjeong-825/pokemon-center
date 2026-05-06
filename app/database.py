import sqlite3

DB_FILE = "pokemon.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        level INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_pokemon_db(name, level):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pokemon (name, level) VALUES (?, ?)",
        (name, level)
    )

    conn.commit()
    conn.close()


def get_pokemon_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pokemon")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_one_pokemon_db(pokemon_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return dict(row)


def delete_pokemon_by_name_db(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM pokemon WHERE name = ?",
        (name,)
    )

    deleted_count = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted_count
