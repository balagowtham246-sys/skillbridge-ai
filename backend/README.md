# SkillBridge AI — Backend

Run instructions:

1. Activate virtual environment (Windows PowerShell):

```powershell
cd 'C:\Users\valasai A\Desktop\skillbridge-ai\backend'
& '..\venv\Scripts\Activate.ps1'
```

2. Install dependencies (if not already):

```powershell
pip install -r requirements.txt
```

3. Start the development server (uses Uvicorn):

```powershell
python -m uvicorn main:app --reload
```

4. Health check:

```powershell
Invoke-WebRequest -Uri 'http://127.0.0.1:8000/health' -UseBasicParsing
```

Notes:
- The app's endpoints are in `backend/main.py`.
- Log entries are appended to `logs/usage_log.json`.
- If you see a `ModuleNotFoundError`, make sure your virtualenv is activated before starting the server.
