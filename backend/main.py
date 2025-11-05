from fastapi import FastAPI
from pydantic import BaseModel

# Initialize app
app = FastAPI(
    title="SkillBridge AI",
    description="AI-powered platform that generates personalized upskilling paths using IBM watsonx",
    version="1.0"
)

# Define input structure
class SkillInput(BaseModel):
    current_skills: list[str]
    goal_role: str

@app.get("/")
def read_root():
    return {"message": "Welcome to SkillBridge AI 🚀"}

@app.post("/generate_path")
def generate_learning_path(data: SkillInput):
    # Placeholder response (AI logic will come later)
    return {
        "goal": data.goal_role,
        "missing_skills": ["Python", "Data Analysis", "Machine Learning"],
        "recommended_courses": [
            {"title": "Python for Beginners", "duration": "2 weeks"},
            {"title": "SQL for Data Analytics", "duration": "3 weeks"},
            {"title": "Intro to Machine Learning", "duration": "4 weeks"}
        ],
        "message": "This is a sample SkillBridge AI response."
    }
