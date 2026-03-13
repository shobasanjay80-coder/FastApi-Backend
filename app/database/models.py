from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


# -------------------------
# USER TABLE
# -------------------------
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, index=True)

    password = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    interviews = relationship("Interview", back_populates="user")

    resumes = relationship("Resume", back_populates="user")

    assignments = relationship("Assignment", back_populates="user")


# -------------------------
# INTERVIEW TABLE
# -------------------------
class Interview(Base):

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    role = Column(String(100))

    video_path = Column(String(255))

    transcript = Column(Text)

    confidence_score = Column(Float)

    fluency_score = Column(Float)

    body_language_score = Column(Float)

    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interviews")


# -------------------------
# RESUME TABLE
# -------------------------
class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    file_path = Column(String(255))

    extracted_text = Column(Text)

    score = Column(Float)

    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="resumes")


# -------------------------
# ASSIGNMENT TABLE
# -------------------------
class Assignment(Base):

    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    question = Column(Text)

    answer = Column(Text)

    score = Column(Float)

    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="assignments")