from sqlalchemy import Column, Integer, String, Text
from database import Base

class MockInterview(Base):
    __tablename__ = "mockInterview"

    id = Column(Integer, primary_key=True, index=True)
    jsonMockResp = Column(Text, nullable=False)
    jobPosition = Column(String, nullable=False)
    jobDesc = Column(String, nullable=False)
    jobExperience = Column(String, nullable=False)
    createdBy = Column(String, nullable=False)
    createdAt = Column(String, nullable=False)
    mockId = Column(String, nullable=False, unique=True, index=True)

class UserAnswer(Base):
    __tablename__ = "userAnswer"

    id = Column(Integer, primary_key=True, index=True)
    mockIdRef = Column(String, nullable=False)
    question = Column(String, nullable=False)
    correctAns = Column(Text)
    userAns = Column(Text)
    feedback = Column(Text)
    rating = Column(String)
    userEmail = Column(String)
    createdAt = Column(String)
