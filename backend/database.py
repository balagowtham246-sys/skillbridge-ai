import sqlite3
from datetime import datetime
from passlib.context import CryptContext
from pydantic import BaseModel

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User model
class User(BaseModel):
    id: int = None
    name: str
    email: str
    password: str

# Initialize database connection
def get_db_connection():
    conn = sqlite3.connect("analytics.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create analytics and users tables (if not exists)
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
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# User functions
def create_user(name: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, hashed_password),
    )
    conn.commit()
    conn.close()

def get_user_by_email(email: str):
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row["id"], name=row["name"], email=row["email"], password=row["password"])
    return None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

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
