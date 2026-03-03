from fastapi import FastAPI
from pydantic import BaseModel
from src.core.checker import analyze_password

app = FastAPI(title="SecuraWord API")

class PasswordRequest(BaseModel):
    password: str

@app.post("/analyze")
def analyze(request: PasswordRequest):
    result = analyze_password(request.password)
    return result