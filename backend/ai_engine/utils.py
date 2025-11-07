# ai_engine/utils.py

def detect_domain(text: str):
    text = text.lower()
    if "data" in text:
        return "Data Science"
    elif "ai" in text or "machine learning" in text:
        return "Artificial Intelligence"
    elif "web" in text or "app" in text:
        return "Software Development"
    else:
        return "General Domain"
