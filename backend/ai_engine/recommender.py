# backend/ai_engine/recommender.py
import os
import json
from typing import List, Dict

def detect_domain(skill_text: str) -> str:
    """Very simple domain detection fallback (improve with embeddings later)."""
    s = skill_text.lower()
    if "data" in s or "pandas" in s or "ml" in s or "machine" in s:
        return "Data Science"
    if "react" in s or "frontend" in s or "javascript" in s or "vite" in s:
        return "Frontend Web"
    if "aws" in s or "cloud" in s or "devops" in s:
        return "Cloud / DevOps"
    if "python" in s:
        return "General Python"
    return "General Domain"

# Try to import OpenAI only when an API key is present
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def generate_learning_path(skill_text: str, domain: str) -> List[Dict]:
    """
    Return a list of steps where each step is a dict:
    {"step": "...", "url": "...", "notes": "..."}
    """
    # If no API key, return a deterministic fallback path
    if not OPENAI_KEY:
        return deterministic_learning_path(skill_text, domain)

    try:
        import openai
        openai.api_key = OPENAI_KEY

        prompt = f"""
You are an expert learning-path generator. Create a concise 4-step learning path for someone who entered this skill: "{skill_text}".
Return valid JSON array ONLY. Each array item must be an object with keys:
  - step: short title
  - url: one high-quality resource (Coursera / YouTube / free tutorial link)
  - notes: 1-sentence note

Example:
[
  {{ "step": "Intro to X", "url": "https://...", "notes": "..." }},
  ...
]

Domain: {domain}
Be pragmatic and prefer free resources (YouTube, docs) if available.
"""
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}],
            max_tokens=500,
            temperature=0.3,
        )
        text = resp["choices"][0]["message"]["content"]
        # Some models may wrap text in backticks — strip before parsing
        text = text.strip().strip("`")
        data = json.loads(text)
        # ensure each item has url field; if not, add placeholder
        for item in data:
            if "url" not in item or not item["url"]:
                item["url"] = "https://www.google.com/search?q=" + (item.get("step","").replace(" ", "+"))
        return data
    except Exception as e:
        print("OpenAI error:", e)
        # fallback deterministic
        return deterministic_learning_path(skill_text, domain)

def deterministic_learning_path(skill_text: str, domain: str):
    s = skill_text.lower()
    # craft some reasonable links per domain (simple)
    if "data" in s or "machine" in s or domain == "Data Science":
        return [
            {"step": "Python + numpy/pandas basics", "url": "https://www.youtube.com/results?search_query=python+for+data+analysis", "notes": "Start with data handling"},
            {"step": "Statistics & ML fundamentals", "url": "https://www.coursera.org/learn/machine-learning", "notes": "Andrew Ng intro"},
            {"step": "Hands-on projects (Kaggle)", "url": "https://www.kaggle.com/learn/overview", "notes": "Practice with datasets"},
            {"step": "Build a portfolio project", "url": "https://github.com", "notes": "Showcase on GitHub"}
        ]
    if "react" in s or domain == "Frontend Web":
        return [
            {"step": "HTML, CSS, JS fundamentals", "url": "https://developer.mozilla.org/en-US/docs/Learn", "notes": "Core web basics"},
            {"step": "React basics + hooks", "url": "https://react.dev/learn", "notes": "Official React docs"},
            {"step": "Build a SPA project", "url": "https://www.youtube.com/results?search_query=react+project+tutorial", "notes": "Follow a tutorial and clone"},
            {"step": "Deploy app (Vercel/Netlify)", "url": "https://vercel.com/docs", "notes": "Make your project live"}
        ]
    if domain == "General Python":
        return [
            {"step": "Python syntax & basics", "url": "https://docs.python.org/3/tutorial/index.html", "notes": "Official tutorial"},
            {"step": "Practical projects", "url": "https://www.youtube.com/results?search_query=python+projects+for+beginners", "notes": "Build small scripts"},
            {"step": "Libraries (requests, flask, pandas)", "url": "https://realpython.com", "notes": "Deep dive tutorials"},
            {"step": "Make a portfolio", "url": "https://github.com", "notes": "Host projects on GitHub"}
        ]
    # default
    return [
        {"step": f"Intro to {domain}", "url": "https://www.youtube.com", "notes": "Start with intro videos"},
        {"step": f"Core concepts for {skill_text}", "url": "https://www.google.com", "notes": "Read articles"},
        {"step": "Hands-on guided project", "url": "https://www.youtube.com", "notes": "Follow along"},
        {"step": "Showcase work", "url": "https://github.com", "notes": "Publish on GitHub"}
    ]
