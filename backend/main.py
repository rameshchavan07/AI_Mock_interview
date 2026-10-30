import datetime
import uuid
import json
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import engine, Base, get_db
import models
import ai_service

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    jobPosition: str
    jobDesc: str
    jobExperience: str
    userEmail: str

class AnswerRequest(BaseModel):
    question: str
    userAns: str
    userEmail: str

@app.post("/api/interview/generate")
def generate_interview(request: GenerateRequest, db: Session = Depends(get_db)):
    mock_json_resp = ai_service.generate_interview_questions(
        request.jobPosition, request.jobDesc, int(request.jobExperience)
    )
    
    mock_id = str(uuid.uuid4())
    created_at = datetime.datetime.now().strftime("%d-%m-%Y")
    
    new_mock = models.MockInterview(
        mockId=mock_id,
        jsonMockResp=mock_json_resp,
        jobPosition=request.jobPosition,
        jobDesc=request.jobDesc,
        jobExperience=request.jobExperience,
        createdBy=request.userEmail,
        createdAt=created_at
    )
    db.add(new_mock)
    db.commit()
    db.refresh(new_mock)
    return {"mockId": new_mock.mockId}

@app.get("/api/user/{email}/interviews")
def get_user_interviews(email: str, db: Session = Depends(get_db)):
    interviews = db.query(models.MockInterview).filter(models.MockInterview.createdBy == email).order_by(models.MockInterview.id.desc()).all()
    return interviews

@app.get("/api/interview/{mock_id}")
def get_interview(mock_id: str, db: Session = Depends(get_db)):
    interview = db.query(models.MockInterview).filter(models.MockInterview.mockId == mock_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    return interview

@app.get("/api/interview/{mock_id}/answers")
def get_interview_answers(mock_id: str, db: Session = Depends(get_db)):
    answers = db.query(models.UserAnswer).filter(models.UserAnswer.mockIdRef == mock_id).all()
    return answers

@app.post("/api/interview/{mock_id}/answer")
def save_answer(mock_id: str, request: AnswerRequest, db: Session = Depends(get_db)):
    feedback_text = ai_service.generate_feedback(request.question, request.userAns)
    try:
        feedback_json = json.loads(feedback_text)
        rating = str(feedback_json.get('rating', ''))
        feedback = feedback_json.get('feedback', '')
    except json.JSONDecodeError:
        rating = "0"
        feedback = "Could not parse AI feedback: " + feedback_text

    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_answer = models.UserAnswer(
        mockIdRef=mock_id,
        question=request.question,
        userAns=request.userAns,
        feedback=feedback,
        rating=rating,
        userEmail=request.userEmail,
        createdAt=created_at
    )
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return {"status": "success", "id": new_answer.id}
