from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import app as api_app

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to restrict origins if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_app)
