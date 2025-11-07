# backend/models/analytics_model.py

import os
import json
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime


class AnalyticsRequest(BaseModel):
    start_date: str  # ISO format date string, e.g., "2023-01-01"
    end_date: str    # ISO format date string, e.g., "2023-12-31"


class AnalyticsResponse(BaseModel):
    total_requests: int
    popular_domains: Dict[str, int]
    top_domain: str
    request_trends: List[Dict[str, Any]]  # List of daily request counts
    average_skills_per_request: float
    generated_at: datetime


def log_event(endpoint: str, request_data: dict, response_data: dict):
    """
    Log an event to the usage log file.
    """
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoint": endpoint,
        "request": request_data,
        "response": response_data
    }
    with open("logs/usage_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


def get_all_analytics(start_date: Optional[str] = None, end_date: Optional[str] = None) -> AnalyticsResponse:
    """
    Retrieve analytics data from the log file, optionally filtered by date range.
    """
    log_file = "logs/usage_log.json"
    if not os.path.exists(log_file):
        return AnalyticsResponse(
            total_requests=0,
            popular_domains={},
            top_domain=None,
            request_trends=[],
            average_skills_per_request=0.0,
            generated_at=datetime.now()
        )

    with open(log_file, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f]

    # Filter by date if provided
    if start_date or end_date:
        filtered_entries = []
        for e in entries:
            entry_date = datetime.strptime(e["timestamp"], "%Y-%m-%d %H:%M:%S").date()
            if start_date and entry_date < datetime.strptime(start_date, "%Y-%m-%d").date():
                continue
            if end_date and entry_date > datetime.strptime(end_date, "%Y-%m-%d").date():
                continue
            filtered_entries.append(e)
        entries = filtered_entries

    total_requests = len(entries)

    # Popular domains (assuming response has "domain" for relevant endpoints)
    domain_counts = {}
    for e in entries:
        domain = e.get("response", {}).get("domain")
        if domain:
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    most_popular_domain = (
        max(domain_counts, key=domain_counts.get) if domain_counts else None
    )

    # Request trends: daily counts
    daily_counts = {}
    for e in entries:
        date = e["timestamp"].split()[0]  # YYYY-MM-DD
        daily_counts[date] = daily_counts.get(date, 0) + 1
    request_trends = [{"date": date, "count": count} for date, count in daily_counts.items()]

    # Average skills per request (for /recommend endpoint)
    skills_counts = []
    for e in entries:
        if e.get("endpoint") == "/recommend":
            skills = e.get("request", {}).get("skills", [])
            skills_counts.append(len(skills))
    average_skills = sum(skills_counts) / len(skills_counts) if skills_counts else 0.0

    return AnalyticsResponse(
        total_requests=total_requests,
        popular_domains=domain_counts,
        top_domain=most_popular_domain,
        request_trends=request_trends,
        average_skills_per_request=average_skills,
        generated_at=datetime.now()
    )
