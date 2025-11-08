# ai_engine/recommender.py

def recommend_courses(skills: list):
    """
    Simple recommender: takes user's skills and returns learning suggestions.
    """
    suggestions = []

    for skill in skills:
        if "python" in skill.lower():
            suggestions.append("Learn Advanced Python for Data Science")
        elif "machine learning" in skill.lower():
            suggestions.append("Complete ML Certification - Coursera/IBM")
        elif "data" in skill.lower():
            suggestions.append("Study SQL + PowerBI for Data Analytics")
        elif "ai" in skill.lower():
            suggestions.append("Explore Deep Learning and NLP fundamentals")
        else:
            suggestions.append(f"Explore advanced topics related to {skill}")

    return {
        "input_skills": skills,
        "recommended_courses": suggestions,
        "next_step": "Focus on your strongest interest area first."
    }
