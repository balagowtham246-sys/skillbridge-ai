"""
SkillBridge AI - Role Prediction Module
"""

def predict_role(skills: list[str]) -> dict:
    """
    Predict potential roles and career paths based on current skills.
    
    Args:
        skills (list[str]): List of user's current skills
        
    Returns:
        dict: Dictionary containing predicted roles and career paths
    """
    # Convert skills to lowercase for matching
    skills = [skill.lower() for skill in skills]
    
    # Role definitions with required skills
    roles = {
        "Frontend Developer": {
            "required_skills": ["html", "css", "javascript", "react", "vue", "angular"],
            "career_path": ["Junior Frontend Developer", "Senior Frontend Developer", "UI/UX Engineer", "Technical Lead"],
            "match_threshold": 0.4
        },
        "Backend Developer": {
            "required_skills": ["python", "java", "node.js", "sql", "mongodb", "api"],
            "career_path": ["Junior Backend Developer", "Senior Backend Developer", "System Architect", "Technical Lead"],
            "match_threshold": 0.4
        },
        "Data Scientist": {
            "required_skills": ["python", "r", "statistics", "machine learning", "sql", "pandas"],
            "career_path": ["Junior Data Scientist", "Senior Data Scientist", "ML Engineer", "AI Architect"],
            "match_threshold": 0.5
        },
        "DevOps Engineer": {
            "required_skills": ["linux", "docker", "kubernetes", "aws", "ci/cd", "terraform"],
            "career_path": ["DevOps Engineer", "Site Reliability Engineer", "Cloud Architect", "DevOps Lead"],
            "match_threshold": 0.4
        }
    }
    
    # Calculate role matches
    matches = []
    for role, requirements in roles.items():
        matched_skills = [skill for skill in skills if any(req in skill for req in requirements["required_skills"])]
        match_ratio = len(matched_skills) / len(requirements["required_skills"])
        
        if match_ratio >= requirements["match_threshold"]:
            matches.append({
                "role": role,
                "match_percentage": round(match_ratio * 100, 1),
                "career_path": requirements["career_path"],
                "missing_skills": [skill for skill in requirements["required_skills"] 
                                if not any(user_skill in skill for user_skill in skills)]
            })
    
    # Sort by match percentage
    matches.sort(key=lambda x: x["match_percentage"], reverse=True)
    
    return {
        "predicted_roles": matches,
        "total_matches": len(matches)
    }