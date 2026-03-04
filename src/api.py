# from fastapi import FastAPI
# from pydantic import BaseModel
# from src.core.checker import analyze_password

# app = FastAPI(title="SecuraWord API")

# class PasswordRequest(BaseModel):
#     password: str

# @app.post("/analyze")
# def analyze(request: PasswordRequest):
#     result = analyze_password(request.password)
#     return result

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from src.core.checker import analyze_password

app = FastAPI(title="SecuraWord API")

# Serve frontend folder
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


class PasswordRequest(BaseModel):
    password: str


@app.post("/analyze")
def analyze(request: PasswordRequest):
    result = analyze_password(request.password)
    return result


@app.get("/")
def home():
    return FileResponse("frontend/index.html")