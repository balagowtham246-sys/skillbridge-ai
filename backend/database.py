"""
SkillBridge AI - Simple Database Module
Currently using JSON file storage for simplicity
"""

import json
import os
from datetime import datetime
<<<<<<< HEAD
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
=======
from typing import Dict, Any
>>>>>>> 686041933804193522e48a97c6023f7b2132512f

# Constants
ANALYTICS_FILE = "logs/analytics.json"
DEFAULT_ANALYTICS = {
    "total_requests": 0,
    "paths_generated": 0,
    "domains_detected": 0,
    "summaries_generated": 0,
    "roles_predicted": 0,
    "popular_skills": {},
    "popular_roles": {},
    "api_usage": {
        "/generate_path": 0,
        "/detect_domain": 0,
        "/recommend": 0,
        "/summarize": 0,
        "/predict_role": 0,
        "/analytics": 0
    }
}

<<<<<<< HEAD
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
=======
def init_db():
    """Initialize the database files if they don't exist"""
    os.makedirs("logs", exist_ok=True)
    
    if not os.path.exists(ANALYTICS_FILE):
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_ANALYTICS, f, indent=2)

def log_event(endpoint: str, input_data: Dict[str, Any], output_data: Dict[str, Any]):
    """
    Log an API event and update analytics
    
    Args:
        endpoint (str): The API endpoint called
        input_data (dict): The input data received
        output_data (dict): The output data returned
    """
    try:
        # Load current analytics
        with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
            analytics = json.load(f)
            
        # Update total requests
        analytics["total_requests"] += 1
        
        # Update endpoint-specific counters
        analytics["api_usage"][endpoint] = analytics["api_usage"].get(endpoint, 0) + 1
        
        # Update specific metrics based on endpoint
        if endpoint == "/generate_path":
            analytics["paths_generated"] += 1
            role = input_data.get("goal_role", "").lower()
            analytics["popular_roles"][role] = analytics["popular_roles"].get(role, 0) + 1
            
            # Track skills
            for skill in input_data.get("current_skills", []):
                skill = skill.lower()
                analytics["popular_skills"][skill] = analytics["popular_skills"].get(skill, 0) + 1
                
        elif endpoint == "/detect_domain":
            analytics["domains_detected"] += 1
        elif endpoint == "/summarize":
            analytics["summaries_generated"] += 1
        elif endpoint == "/predict_role":
            analytics["roles_predicted"] += 1
            
        # Save updated analytics
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(analytics, f, indent=2)
            
    except Exception as e:
        print(f"Error logging event: {str(e)}")
>>>>>>> 686041933804193522e48a97c6023f7b2132512f

def get_all_analytics():
    """
    Retrieve all analytics data
    
    Returns:
        dict: The complete analytics data
    """
    try:
        with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading analytics: {str(e)}")
        return DEFAULT_ANALYTICS