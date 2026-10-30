import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env.local")

api_key = os.getenv("NEXT_PUBLIC_GEMINI_API_KEY")
genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  generation_config=generation_config,
)

def generate_interview_questions(job_position: str, job_desc: str, job_experience: int) -> str:
    question_count = os.getenv("NEXT_PUBLIC_INTERVIEW_QUESTION_COUNT", "5")
    prompt = f"Job position: {job_position}, Job Description: {job_desc}, Years of Experience: {job_experience}, Depends on Job Position, Job Description & Years of Experience give us {question_count} Interview question along with Answer in JSON format, Give us question and answer field on JSON"
    chat = model.start_chat()
    response = chat.send_message(prompt)
    text = response.text
    # Clean up formatting if AI returned markdown
    text = text.replace("```json", "").replace("```", "").strip()
    return text

def generate_feedback(question: str, user_answer: str) -> str:
    prompt = f"Question: {question}, User Answer: {user_answer}, Based on Question and user answer for give interview question please give us rating for answer and feedback as area of improvement if any in just 3 to 5 lines to improve it in JSON format with rating field and feedback field"
    chat = model.start_chat()
    response = chat.send_message(prompt)
    text = response.text
    text = text.replace("```json", "").replace("```", "").strip()
    return text
