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

# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse

# from src.core.checker import analyze_password

# app = FastAPI(title="SecuraWord API")

# # Serve frontend folder
# app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# class PasswordRequest(BaseModel):
#     password: str


# @app.post("/analyze")
# def analyze(request: PasswordRequest):
#     result = analyze_password(request.password)
#     return result


# @app.get("/")
# def home():
#     return FileResponse("frontend/index.html")

# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse

# from src.core.checker import analyze_password

# app = FastAPI(title="SecuraWord API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # allow React frontend
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Serve frontend folder
# app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# class PasswordRequest(BaseModel):
#     password: str


# @app.post("/analyze")
# def analyze(request: PasswordRequest):
#     result = analyze_password(request.password)
#     return result


# @app.get("/")
# def home():
#     return FileResponse("frontend/index.html")



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.core.checker import analyze_password

app = FastAPI(title="SecuraWord API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    password: str

@app.post("/analyze")
def analyze(request: PasswordRequest):
    return analyze_password(request.password)