from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings, create_upload_dirs
from app.database.db import engine
from app.database import models

from app.api import auth, interview, resume, assignment, analytics


# ---------------------------
# CREATE DATABASE TABLES
# ---------------------------

models.Base.metadata.create_all(bind=engine)


# ---------------------------
# CREATE FASTAPI APP
# ---------------------------

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Interview Preparation Platform",
    version="1.0.0"
)


# ---------------------------
# CREATE UPLOAD DIRECTORIES
# ---------------------------

create_upload_dirs()


# ---------------------------
# CORS SETTINGS
# ---------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------
# INCLUDE API ROUTERS
# ---------------------------

app.include_router(auth.router)
app.include_router(interview.router)
app.include_router(resume.router)
app.include_router(assignment.router)
app.include_router(analytics.router)


# ---------------------------
# ROOT ENDPOINT
# ---------------------------

@app.get("/")
def root():
    return {
        "message": "AI Interview Platform API is running 🚀"
    }


# ---------------------------
# HEALTH CHECK
# ---------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }