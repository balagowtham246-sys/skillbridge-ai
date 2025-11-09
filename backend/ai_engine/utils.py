<<<<<<< HEAD
import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_domain(query):
    prompt = f"Given this skill or interest '{query}', which tech domain (like AI, Web Dev, Cybersecurity, etc.) does it belong to?"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an expert career guide."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
=======
"""
SkillBridge AI - Domain Detection Utility
"""

def detect_domain(text: str) -> str:
    """
    Detect the professional domain based on input text.
    Currently using a simple keyword-based approach.
    
    Args:
        text (str): Input text to analyze (job role, skills, etc.)
        
    Returns:
        str: Detected domain (e.g., "Software Development", "Data Science", etc.)
    """
    # Convert to lowercase for case-insensitive matching
    text = text.lower()
    
    # Domain keywords mapping
    domain_keywords = {
        "Software Development": ["developer", "software", "web", "frontend", "backend", "fullstack", "programming"],
        "Data Science": ["data", "analytics", "machine learning", "ai", "statistics", "ml"],
        "DevOps": ["devops", "cloud", "aws", "azure", "kubernetes", "docker", "ci/cd"],
        "Design": ["ui", "ux", "designer", "graphic", "interface", "user experience"],
        "Product": ["product manager", "product owner", "scrum", "agile"],
        "Security": ["security", "cybersecurity", "penetration", "ethical hacking", "cryptography"]
    }
    
    # Check each domain's keywords
    for domain, keywords in domain_keywords.items():
        if any(keyword in text for keyword in keywords):
            return domain
            
    return "General"  # Default domain if no match found
>>>>>>> 686041933804193522e48a97c6023f7b2132512f
