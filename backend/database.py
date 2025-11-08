"""
SkillBridge AI - Simple Database Module
Currently using JSON file storage for simplicity
"""

import json
import os
from datetime import datetime
from typing import Dict, Any

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