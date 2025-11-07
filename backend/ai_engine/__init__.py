def detect_domain(goal: str) -> str:
    goal_lower = goal.lower()
    if "data" in goal_lower:
        return "Data Science"
    elif "web" in goal_lower or "frontend" in goal_lower or "developer" in goal_lower:
        return "Web Development"
    elif "cloud" in goal_lower or "devops" in goal_lower:
        return "Cloud Engineering"
    elif "ai" in goal_lower or "ml" in goal_lower:
        return "AI Engineering"
    else:
        return "Software Engineering"
