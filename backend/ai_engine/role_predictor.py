# ai_engine/role_predictor.py

def predict_role(skills: list):
    """
    Predicts a career role based on given skills.
    This is a rule-based placeholder version (can be replaced with ML later).
    """
    skills_lower = [s.lower() for s in skills]
    
    if any(word in skills_lower for word in ["python", "machine learning", "ai", "tensorflow"]):
        role = "Machine Learning Engineer"
        path = [
            "Learn Deep Learning (TensorFlow/PyTorch)",
            "Master Data Structures for ML",
            "Work on Kaggle Projects",
        ]
    elif any(word in skills_lower for word in ["javascript", "react", "frontend"]):
        role = "Frontend Developer"
        path = [
            "Learn Advanced React or Next.js",
            "Practice UI/UX design principles",
            "Build portfolio web apps"
        ]
    elif any(word in skills_lower for word in ["java", "spring", "backend"]):
        role = "Backend Developer"
        path = [
            "Learn Microservices architecture",
            "Study database optimization",
            "Deploy APIs using Docker"
        ]
    elif any(word in skills_lower for word in ["data", "sql", "excel", "tableau"]):
        role = "Data Analyst"
        path = [
            "Master Excel and SQL",
            "Learn PowerBI or Tableau",
            "Understand data storytelling"
        ]
    else:
        role = "General Software Engineer"
        path = [
            "Explore full-stack development",
            "Work on open-source contributions",
            "Enhance problem-solving and algorithms"
        ]

    return {
        "predicted_role": role,
        "recommended_path": path
    }
