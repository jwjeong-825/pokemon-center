import os
import psycopg
from psycopg.rows import dict_row


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "pokemon_center")
DB_USER = os.getenv("DB_USER", "pokemon_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "pokemon_password")


def get_connection():
    return psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        row_factory=dict_row
    )


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemon (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                level INTEGER NOT NULL
            )
            """)


def add_pokemon_db(name, level):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pokemon (name, level) VALUES (%s, %s)",
                (name, level)
            )


def get_pokemon_db():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pokemon ORDER BY id")
            rows = cursor.fetchall()
            return rows


def get_one_pokemon_db(pokemon_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM pokemon WHERE id = %s",
                (pokemon_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return row


def delete_pokemon_by_name_db(name):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM pokemon WHERE name = %s",
                (name,)
            )

            deleted_count = cursor.rowcount
            return deleted_count
