import sqlite3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "training.db"
JSON_FILE = BASE_DIR / "training_data.json"

VALID_TYPES = ("Hitting", "Fielding", "Throwing", "Conditioning")


def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS training_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                training_date TEXT NOT NULL,
                training_type TEXT NOT NULL
                    CHECK(training_type IN (
                        'Hitting', 'Fielding',
                        'Throwing', 'Conditioning'
                    )),
                duration INTEGER NOT NULL CHECK(duration > 0),
                notes TEXT NOT NULL DEFAULT ''
            )
        """)


def load_sessions():
    with connect() as conn:
        rows = conn.execute("""
            SELECT training_date AS date,
                   training_type AS type,
                   duration, notes
            FROM training_sessions
            ORDER BY id
        """).fetchall()
        return [dict(row) for row in rows]


def save_sessions(sessions):
    with connect() as conn:
        conn.execute("DELETE FROM training_sessions")
        conn.executemany("""
            INSERT INTO training_sessions
                (training_date, training_type, duration, notes)
            VALUES (?, ?, ?, ?)
        """, [
            (
                session["date"],
                session["type"],
                session["duration"],
                session.get("notes", "")
            )
            for session in sessions
        ])


def migrate_json():
    initialize_database()

    if not JSON_FILE.exists():
        return 0

    with connect() as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM training_sessions"
        ).fetchone()[0]

    if count > 0:
        return 0

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        sessions = json.load(file)

    if sessions:
        save_sessions(sessions)

    return len(sessions)


if __name__ == "__main__":
    migrated = migrate_json()
    print(f"Database ready. Migrated {migrated} sessions.")