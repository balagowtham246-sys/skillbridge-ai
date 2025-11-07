# Helper script to activate venv and start uvicorn
# Usage: .\start.ps1

# Ensure we're in the backend directory
Set-Location -Path $PSScriptRoot

# Activate virtualenv (assuming venv is in parent directory)
& "..\venv\Scripts\Activate.ps1"

# Start uvicorn with reload
Write-Host "Starting SkillBridge AI backend on http://127.0.0.1:8000" -ForegroundColor Green
python -m uvicorn main:app --reload