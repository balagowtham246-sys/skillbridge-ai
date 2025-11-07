import sqlite3
from datetime import datetime

# Initialize database connection
def get_db_connection():
    conn = sqlite3.connect("analytics.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create analytics table (if not exists)
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            endpoint TEXT,
            input_data TEXT,
            output_data TEXT
        )
    """)
    conn.commit()
    conn.close()

# Log event into database
def log_event(endpoint: str, input_data: dict, output_data: dict):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO analytics (timestamp, endpoint, input_data, output_data) VALUES (?, ?, ?, ?)",
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            endpoint,
            str(input_data),
            str(output_data),
        ),
    )
    conn.commit()
    conn.close()

# Retrieve all analytics
def get_all_analytics():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM analytics ORDER BY id DESC")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows
