import sqlite3
from database import connect

print("Testing SQLite database constraints...")

tests = [
    ("Invalid training type", "2026-10-27", "Invalid", 60, "Test"),
    ("Negative duration", "2026-10-27", "Hitting", -10, "Test"),
    ("Missing date", None, "Hitting", 60, "Test"),
]

with connect() as conn:
    for name, training_date, training_type, duration, notes in tests:
        try:
            conn.execute("SAVEPOINT test_case")
            conn.execute(
                """
                INSERT INTO training_sessions
                (training_date, training_type, duration, notes)
                VALUES (?, ?, ?, ?)
                """,
                (training_date, training_type, duration, notes)
            )
            print(f"FAILED: {name} was accepted")
        except sqlite3.IntegrityError:
            print(f"PASSED: {name} was rejected")
        finally:
            conn.execute("ROLLBACK TO SAVEPOINT test_case")
            conn.execute("RELEASE SAVEPOINT test_case")

print("Testing completed.")