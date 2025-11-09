import os
import json
from fastapi import FastAPI, Query, HTTPException, Body, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime, timedelta
from jose import JWTError, jwt
from ai_engine.recommender import detect_domain, generate_learning_path
from database import init_db, log_event, get_all_analytics, create_user, get_user_by_email, verify_password, User

# JWT settings
SECRET_KEY = "your-secret-key"  # In production, use a secure key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

<<<<<<< HEAD
=======
# Initialize FastAPI app
app = FastAPI(title="SkillBridge AI", version="2.1")

# 🔹 Initialize database at startup
init_db()

# 🔹 Allow frontend to communicate with backend
>>>>>>> 686041933804193522e48a97c6023f7b2132512f
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
init_db()

security = HTTPBearer()

# Pydantic models
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

<<<<<<< HEAD
class Token(BaseModel):
    access_token: str
    token_type: str
=======
# ---------------------------------------------
#  API 1: Generate Learning Path  (POST)
# ---------------------------------------------
@app.post("/generate_path")
def generate_path(data: SkillInput):
    domain = detect_domain(data.goal_role)
    courses = recommend_courses(data.current_skills)
    summary = generate_summary(data.goal_role, data.current_skills, domain)
>>>>>>> 686041933804193522e48a97c6023f7b2132512f

# JWT functions
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

<<<<<<< HEAD
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return email
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
=======
    # Log every user request (JSON + DB)
    log_user_request(data, result)
    log_event("/generate_path", {"goal_role": data.goal_role, "current_skills": data.current_skills}, result)
    return result
>>>>>>> 686041933804193522e48a97c6023f7b2132512f

# Auth endpoints
@app.post("/register")
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        create_user(user.name, user.email, user.password)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "name": user.name,
                "email": user.email
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    try:
        access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "name": db_user.name,
                "email": db_user.email
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/profile")
def get_profile(email: str = Depends(verify_token)):
    user = get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

# Existing endpoints
@app.get("/recommend")
def recommend(skill: str = Query(..., description="user provided skill text")):
    domain = detect_domain(skill)
    # generate_learning_path returns a list of dicts: {"step": "...", "url": "...", "notes": "..."}
    try:
        learning_path = generate_learning_path(skill, domain)
    except Exception as e:
        # fallback: deterministic suggestions if AI fails
        print("AI error:", e)
        learning_path = [
            {"step": f"Intro to {domain} ({skill})", "url": "https://www.youtube.com", "notes": "Fallback resource"},
            {"step": f"Hands-on project in {skill}", "url": "https://www.udemy.com", "notes": "Build a project"},
        ]
    return {"skill": skill, "domain": domain, "learning_path": learning_path}

@app.get("/analytics")
def analytics():
    return {"analytics": get_all_analytics()}

<<<<<<< HEAD
=======

# ---------------------------------------------
#  API 3: Detect Domain  (POST)
# ---------------------------------------------
@app.post("/detect_domain")
def get_domain(data: dict):
    text = data.get("text", "")
    result = detect_domain(text)
    log_event("/detect_domain", {"text": text}, {"domain": result})
    return {"domain": result}


# ---------------------------------------------
#  API 4: Recommend Courses  (POST)
# ---------------------------------------------
@app.post("/recommend")
def recommend(data: dict):
    skills = data.get("skills", [])
    result = recommend_courses(skills)
    log_event("/recommend", {"skills": skills}, result)
    return result


# ---------------------------------------------
#  API 5: Generate Summary  (POST)
# ---------------------------------------------
@app.post("/summarize")
def summarize(data: dict):
    text = data.get("text", "")
    result = generate_summary(text, [], "General")
    log_event("/summarize", {"text": text}, {"summary": result})
    return {"summary": result}


# ---------------------------------------------
#  API 6: Predict Role and Career Path  (POST)
# ---------------------------------------------
@app.post("/predict_role")
def predict(data: dict):
    skills = data.get("skills", [])
    result = predict_role(skills)
    log_event("/predict_role", {"skills": skills}, result)
    return result


# ---------------------------------------------
#  Root & Health Routes
# ---------------------------------------------
>>>>>>> 686041933804193522e48a97c6023f7b2132512f
@app.get("/")
def root():
    return {"message": "SkillBridge AI backend is running ✅"}

@app.get("/health")
def health():
    return {"status": "ok"}
